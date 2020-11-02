from distutils.core import setup
import setuptools
setup(
  name = 'compare_df',
  packages = ['compare_df'],
  version = '0.6',
  license='MIT',
  description = 'A collection of function which can be used to compare two dataframes.',
  long_description_content_type="""text/x-rst""",
  author = 'Sanyam Gupta',
  author_email = 'sanyam15111@gmail.com',
  url = 'https://github.com/Sanyam15/compare_df',
  download_url = 'https://github.com/Sanyam15/compare_df/archive/v0.2.tar.gz',
  keywords = ['Machine Learning', 'Comparison', 'Excel','CSV','Pandas', 'DataFrame', 'Validation'],
  install_requires=['pandas'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
  long_description ="""
   **Project Description**

This package has collection of functions that can be used to compare two dataframes. These functions can help in validation, where there is a need to compare if any of the metrics value has been altered or to get matching records in the two dataframes. The package serves best when the two data frames have same schema and from the same source. 
In validation, if you are comparing two datas which may have changed over the time, this package can help you in the analysis and save the time spent in BI Tools for the analysis.

**IMPORT**:

from compare_df import *

 **Function I : getMatchingRecords(dataframe1=None,dataframe2=None,common_columns=None)**

This function returns a dataframe which contains identical records for the
passed list of columns (default :- all columns) in the two dataframes.

**The Parameters:**

Parameter - dataframe1: The first Input DataFrame(X)
Parameter - dataframe2:The second Input DataFrame(X)
Parameter - common_columns: The list of columns for which the two dataframes have to be compared. default : All columns of dataframe1

**Return**

This Returns a dataframe which holds the records which have identical value for the passed columns  in both dataframes. 


**Example**:
from compare_df import *
getMatchingRecords(df1,df2,common_columns=["Prduct_no","Product_Category"])

This returns df with the records of Values of columns ["Prduct_no","Product_Category"] which were found in both dataframes.


**Function 2 : getUniqueRecords(dataframe1=None,dataframe2=None,key=[])**

This function receives two dataframes and list of key attributes.
These attributes should identify a record in both dataframe uniquely.
It returns a dataframe with those records which are only present in either of the dataframe.
The dataframe has a column named 'Dataframe' which tells in which dataframe does the record exist

**The Parameters:**-

Parameter - dataframe1: The first Input DataFrame(X), also referred as left.
Parameter - dataframe2:The second Input DataFrame(X), also referred as right.
Parameter - key: The list of columns present in both dataframes which _must identify a record in both dataframes uniquely.

**Return**

This Returns a dataframe which holds the records which are uniquely present in the dataframe along with the dataframe name. 


**Example**:
from compare_df import *
getMatchingRecords(df1,df2,common_columns=["Department","Emp_id"])

This returns df for which the key attributes : ["Prduct_no","Product_Category"] are present in only one of the dataframe.


**Function 3 : getVariableRecords(dataframe1, dataframe2, key, metrics=[], unique=True)**

This function receives two dataframes and list of key attributes and metric attributes and a boolean attribute -> 'unique'.
These attributes should identify a record in both dataframe exclusively.
Metric attributes are those attributes for which you want to compare the value between the two dataframes.
The function returns the key values and the metric column for which irregularity was encountered.
It classify the irregularity into three classes-

Mismatch : If key values are present in both dataframe, but there is a mismatch for the column value.

left_only : If the key values are present only in the first/left dataframe but not in second dataframe.

right_only : If the key values are present only in the second/right dataframe but not in first dataframe.

If param - 'unique' is set to True:
    Only the Records tagged as "Mismatch" are returned
If param - 'unique' is set to False:
    All the Irregular Records are returned

**The Parameters:**-

Parameter - dataframe1: Pandas DataFrame : The first Input DataFrame(X), also referred as left.
Parameter - dataframe2: Pandas DataFrame : The second Input DataFrame(X), also referred as right.

Parameter - key: List :The list of columns present in both dataframes which must identify a record in dataframe uniquely.

Parameter - metrics: List :The list of columns for which comparison needs to be made.
                Default - Columns in dataframe1 other than the key columns.

Parameter - unique : Boolean : If True, returns only the records with Comparison tagged as Mismatch ;
                          
 If False, returns all the irregularities.
                 Default - True

**Return**

This Returns a dataframe which observe a difference in the value of any Metrics column passed 
between the two dataframes for the respective key values


**Example**:
from compare_df import *
getVariableRecords(df1,df2,key=["Department","Emp_id"],metrics=["ratings","contact"])

The function will check for each column in metrics for all key records, check if both dataframe has same values,
If the values are different then the key value, column name, value in the two dataframes would be returned.
Along with a Comparison column which state whether there is Mismatch in the values, or the value is present in only 
one dataframe.

LOG
==========

0.0.6 (02/11/2020)
-------------------
- First Release



""",
  
)
