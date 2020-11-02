'''
This function receives two dataframes and list of key attributes and metric attributes and a boolean attribute -> 'unique'.
Metric attributes are those attributes for which you want to compare the value between the two dataframes.
Key along with each metric column should uniquely identify records in both the dataframe.
The function returns the key values and the metric column for which irregularity was encountered.
It classify the irregularity into three classes:
    Mismatch : If key values are present in both dataframe, but there is a mismatch for the column value
    left_only : If the key values are present only in the first/left dataframe but not in second dataframe.
    right_only : If the key values are present only in the second/right dataframe but not in first dataframe.
If param -> 'unique' is set to True:
    Only the Records tagged as "Mismatch" are returned
If param -> 'unique' is set to False:
    All the Irregular Records are returned
'''

import pandas as pd

#Import functions to checck for errors
from compare_df.UniqueRecords import isNaN, checkErrors

#Tag the irregularity for a key-column combination
def getRecords(row, column, key=[]):
    if row[column + "_x"] == row[column + "_y"]:
        return "Identical"
    else:
        if isNaN(row[column + "_x"]) == False and isNaN(row[column + "_y"]) == False:
            return "Mismatch"
        else:
            if isNaN(row[column + "_x"]) == True:
                return "right_only"
            elif isNaN(row[column + "_y"]) == True:
                return "left_only"
    return

#Check errors for parameter -> 'metrics'
def checkMetricsError(dataframe1, dataframe2, key, metrics):
    #Should be a non-empty list
    if not isinstance(metrics, list):
        raise TypeError('Expects <list> for the parameter -> "metrics"')
    if len(metrics) < 1:
        raise KeyError('The list was empty for the parameter -> "metrics"')

    # Columns in the parameter -> 'key' should be present in both the dataframes
    res1 = [ele for ele in metrics if ele not in list(dataframe1.columns)]
    res2 = [ele for ele in metrics if ele not in list(dataframe2.columns)]
    if len(res1) > 0 and len(res2) > 0:
        raise KeyError(
            "Data Error : Could not find Metrics columns: "
            + str(res1)
            + " in dataframe1 and columns:"
            + str(res2)
            + " in dataframe2"
        )
    elif len(res1) > 0:
        raise KeyError(
            "Data Error : Could not find Metrics columns: " + str(res1) + " in dataframe1"
        )
    elif len(res2) > 0:
        raise KeyError(
            "Data Error : Could not find Metrics columns: " + str(res2) + " in dataframe2"
        )

    #Elements in the metrics should be exclusive to the elements in key.
    intersection_key_metrics = [ele for ele in key if ele in metrics]
    if(len(intersection_key_metrics)>0):
        raise KeyError(
            "Data Error : Elements in key and metrics list should be exclusive. " +
            "Some columns were present in both: " + str(intersection_key_metrics) + "."
        )



def getVariableRecords(dataframe1, dataframe2, key, metrics=[], unique=True):
        """
            :rtype: Pandas DataFrame
            :param dataframe1: Pandas DataFrame : The first Input DataFrame(X), also referred as left.
            :param dataframe2: Pandas DataFrame : The second Input DataFrame(X), also referred as right.
            :param key: List :The list of columns present in both dataframes which must identify a record in dataframe uniquely.
            :param metrics: List :The list of columns for which comparison needs to be made.
                            default -> Columns in dataframe1 other than the key columns.
            :param unique : Boolean : If True, returns only the records with Comparison tagged as Mismatch ;
                                      If False, returns all the irregularities.
                            Default -> True
        """
        #Unique should have boolean values
        if unique not in [0, 1]:
            raise TypeError('Expects a boolean value for the parameter -> "unique"')

        # Seeting default value for metrics
        if(metrics==None):
            metrics = [ele for ele in list(dataframe1.columns) if ele not in key]

        # Check for Errors
        checkErrors(dataframe1, dataframe2, key=key)
        checkMetricsError(dataframe1, dataframe2, key=key, metrics=metrics)

        variable_dataframe = pd.DataFrame()

        # Iteratively take each metrics column and compare the values return by the two dataframes
        for col in metrics:

            # Key along with each metric column should uniquely identify records in both the dataframe
            if dataframe1.set_index(key+["col"]).index.is_unique == False:
                raise KeyError(
                    "Data Error : The set of key attributes does not uniquely identify records in dataframe1."
                )
            if dataframe2.set_index(key+["col"]).index.is_unique == False:
                raise KeyError(
                    "Data Error : The set of key attributes does not uniquely identify records in dataframe2."
                )

            left_dataframe = dataframe1[key + [col]]
            right_dataframe = dataframe2[key + [col]]
            temp_dataframe = pd.merge(
                left=left_dataframe, right=right_dataframe, on=key, how="outer"
            )

            #Tag the irregularity
            temp_dataframe["Comparison"] = temp_dataframe.apply(
                lambda row: getRecords(row, column=col, key=key), axis=1
            )
            temp_dataframe = temp_dataframe.rename(
                columns={col + "_x": "left_value", col + "_y": "right_value"}
            )
            temp_dataframe.loc[:, "Column"] = col
            # On basis of Unique attribute, select the return records.
            if unique == False:
                variable_dataframe = variable_dataframe.append(
                    temp_dataframe.query('Comparison != "Identical"')
                )
            else:
                variable_dataframe = variable_dataframe.append(
                    temp_dataframe.query('Comparison == "Mismatch"')
                )

        return (
            variable_dataframe[
                key + ["Column","left_value", "right_value","Comparison"]
            ]
            .sort_values(by=["Comparison", "Column"])
            .reset_index(drop=True)
        )
