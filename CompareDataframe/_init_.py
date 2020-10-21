from CompareDataframe.MatchingRecords import *
from CompareDataframe.UniqueRecords import *
from CompareDataframe.VariableRecords import *

df1=pd.read_csv("/home/sanyam/Documents/df1.csv")
df2=pd.read_csv("/home/sanyam/Documents/df2.csv")

print(MatchingRecords.getMatchingRecords(df1,df2,common_columns=list(df1.columns)[0:4]))
print(UniqueRecords.getUniqueRecords(df1,df2,key=list(df1.columns)[0:3]))
print(VariableRecords.getVariableRecords(df1,df2,key=list(df1.columns)[0:2],metrics=list(df1.columns)[2:],unique=False))