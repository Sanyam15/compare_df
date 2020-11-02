from compare_df.MatchingRecords import *
from compare_df.UniqueRecords import *
from compare_df.VariableRecords import *



def getUniqueRecords(dataframe1, dataframe2, key=[]):
    return UniqueRecords.getUniqueRecords(dataframe1, dataframe2, key=[])

def getMatchingRecords(dataframe1=None,dataframe2=None,common_columns=None):
    return MatchingRecords.getMatchingRecords(dataframe1,dataframe2,common_columns)

def getVariableRecords(dataframe1, dataframe2, key, metrics=[], unique=True):
    return VariableRecords.getVariableRecords(dataframe1, dataframe2, key, metrics, unique)

