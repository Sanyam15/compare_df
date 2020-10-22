'''
This function returns a dataframe which contains identical records for the
passed list of columns (default :- all columns) in the two dataframes.
'''


import pandas as pd

def checkError(dataframe1, dataframe2, common_columns):

    #Error : If no columns are there to compare
    if len(common_columns) == 0:
        raise ValueError(
            'Data Error : The parameter -> "common_columns" is empty or dataframe has no columns'
        )

    # Error : If the param -> 'common_columns' has column/s which do not exist
    res1 = [ele for ele in common_columns if ele not in list(dataframe1.columns)]
    res2 = [ele for ele in common_columns if ele not in list(dataframe2.columns)]
    if len(res1) > 0 and len(res2) > 0:
        raise KeyError(
            "Data Error : Could not find columns: "
            + str(res1)
            + " in dataframe1 and columns:"
            + str(res2)
            + " in dataframe2"
        )
    elif len(res1) > 0:
        raise KeyError(
            "Data Error : Could not find columns: " + str(res1) + " in dataframe1"
        )
    elif len(res2) > 0:
        raise KeyError(
            "Data Error : Could not find columns: " + str(res2) + " in dataframe2"
        )


def getMatchingRecords(
        dataframe1=None,
        dataframe2=None,
        common_columns=None,
    ):
        """
            :rtype: Pandas DataFrame
            :param dataframe1: The first Input DataFrame(X)
            :param dataframe2:The second Input DataFrame(X)
            :param common_columns: The list of columns for which the two dataframes have to be compared. default : All columns of dataframe1
        """
        # Error : If either of dataframe is not pandas dataframe
        if not isinstance(dataframe1, pd.DataFrame):
            raise TypeError('Expects pd.DataFrame for the parameter -> "dataframe1"')
        if not isinstance(dataframe2, pd.DataFrame):
            raise TypeError('Expects pd.DataFrame for the parameter -> "dataframe2"')

        #Setting default argument for common_columns
        if common_columns is None:
            common_columns = list(dataframe1.columns)

        #Check For Errors
        checkError(dataframe1, dataframe2, common_columns)

        #Selecting the required columns
        dataframe1 = dataframe1[common_columns]
        dataframe2 = dataframe2[common_columns]
        return pd.merge(dataframe1, dataframe2, on=list(dataframe1.columns))
