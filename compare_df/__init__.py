from compare_df.MatchingRecords import *
from compare_df.UniqueRecords import *
from compare_df.VariableRecords import *

def getUniqueRecords(dataframe1, dataframe2, key=[]):
    UniqueRecords.getUniqueRecords(dataframe1, dataframe2, key=[])

def getMatchingRecords(dataframe1=None,dataframe2=None,common_columns=None):
    MatchingRecords.getMatchingRecords(dataframe1,dataframe2,common_columns)

def getVariableRecords(dataframe1, dataframe2, key, metrics=[], unique=True):
    VariableRecords.getVariableRecords(dataframe1, dataframe2, key, metrics, unique)

