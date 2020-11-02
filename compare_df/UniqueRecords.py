'''
This function receives two dataframes and list of key attributes.
These attributes should identify a record in both dataframe uniquely.
It returns a dataframe with those records which are only present in either of the dataframe.
The dataframe has a column named 'Dataframe' which tells in which dataframe does the record exist
'''

import pandas as pd

#Check for NaN values
def isNaN(string):
    return string != string

#Returns not null value for the column
def getValue(field, column):
    if isNaN(field[column + "_x"]):
        return field[column + "_y"]
    elif isNaN(field[column + "_y"]):
        return field[column + "_x"]


def checkErrors(dataframe1, dataframe2, key):
    #Passed argument should match the datatype

    if not isinstance(key, list):
        raise TypeError('Expects <list> for the parameter -> "metrics"')

    if len(key)<1:
        raise KeyError('The list was empty for the parameter -> "key"')

    #Columns in the parameter -> 'key' should be present in both the dataframes
    res1 = [ele for ele in key if ele not in list(dataframe1.columns)]
    res2 = [ele for ele in key if ele not in list(dataframe2.columns)]
    if len(res1) > 0 and len(res2) > 0:
        raise KeyError(
            "Data Error : Could not find Key columns: "
            + str(res1)
            + " in dataframe1 and columns:"
            + str(res2)
            + " in dataframe2"
        )
    elif len(res1) > 0:
        raise KeyError(
            "Data Error : Could not find Key columns: " + str(res1) + " in dataframe1"
        )
    elif len(res2) > 0:
        raise KeyError(
            "Data Error : Could not find Key columns: " + str(res2) + " in dataframe2"
        )

def getUniqueRecords(dataframe1, dataframe2, key=[]):

        """
            :rtype: Pandas DataFrame
            :param dataframe1: The first Input DataFrame(X), also referred as left.
            :param dataframe2:The second Input DataFrame(X), also referred as right.
            :param key: The list of columns present in both dataframes which must identify a record in dataframe uniquely.
                        default->all columns of dataframe1
        """
        if not isinstance(dataframe1, pd.DataFrame):
            raise TypeError('Expects pd.DataFrame for the parameter -> "dataframe1"')
        if not isinstance(dataframe2, pd.DataFrame):
            raise TypeError('Expects pd.DataFrame for the parameter -> "dataframe2"')

        if key==[]:
            key=list(dataframe1.columns)

        #Metrics has columns other than key attributes
        metrics = [ele for ele in list(dataframe1.columns) if ele not in key]

        checkErrors(dataframe1, dataframe2, key)

        # Key should uniquely identify records in both the dataframe
        if dataframe1.set_index(key).index.is_unique == False:
            raise KeyError(
                "Data Error : The set of key attributes does not uniquely identify records in dataframe1."
            )
        if dataframe2.set_index(key).index.is_unique == False:
            raise KeyError(
                "Data Error : The set of key attributes does not uniquely identify records in dataframe2."
            )

        #Selecting the Key attributes
        dataframe1_key = dataframe1[key]
        dataframe2_key = dataframe2[key]

        '''
        A join of the two dataframes on the key attributes to obtain the unique records 
        that are present in any one of the two dataframes only.
        '''

        joined_dataframe = pd.merge(
            dataframe1, dataframe2, on=key, how="outer", indicator=True
        ).query('_merge != "both"')

        #Selecting the original column values and ignoring the NaN values
        for col in metrics:
            joined_dataframe[col] = joined_dataframe.apply(
                lambda row: getValue(row, column=col), axis=1
            )

        ''' 
        Returning the dataframe with unique records with the column -> 'Dataframe'
        which states which dataframe does the records belong to.
        '''

        return_df = (
            joined_dataframe[key + metrics + ["_merge"]]
            .rename(columns={"_merge": "Dataframe"})
            .reset_index(drop=True)
        )
        return return_df
