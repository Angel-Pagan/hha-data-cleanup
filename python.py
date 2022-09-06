
""" Import necessary packages """

import pandas as pd
import datetime as dt
import numpy as np

""" Step 1. Loads the data into python """

df = pd.read_csv('data/raw/School_Learning_Modalities.csv') 
df # print csv

""" Step 2. Prints the count of columns and rows """

column_count = df.shape # assign the column_count variable 
column_count # Prints the count of columns and rows

""" Step 3. Provides a print out of the column names """
# First method
df.columns 
# Second method
cloumn_names = list(df)
cloumn_names # print column names

""" Step 4. Cleans the column names """

df.columns = df.columns.str.lower() # change all column names to lowercase

df.columns = df.columns.str.replace(' ', '_') # replace all whitespace in column names with an underscore

df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') # remove all special characters and whitespace ' ' from a specific column

df.columns # Print clean columns



""" Step 5. Cleans the strings that might exist within each column """

strings_columns = df.select_dtypes(object).columns # Assign all string data type to variable strings_columns

df[strings_columns] = df[strings_columns].apply(lambda x: x.str.lower()) # change all strings to lowercase

df[strings_columns] = df[strings_columns].apply(lambda x: x.str.replace(' ', '_')) # replace all whitespace in strings with an underscore

df[strings_columns] = df[strings_columns].apply(lambda x: x.str.replace('[^A-Za-z0-9]+', '_')) # remove all special characters and whitespace ' ' from a specific column

df.sample (25) # preview get random sample of 25 rows

""" Step 6. Assesses white space or special characters """

special_characters = df[strings_columns].apply(lambda x: x.str.count('[^A-Za-z0-9]+')) # assign a variable special_characters to assesses special characters 

special_characters # Print Special Characters

white_spaces = df[strings_columns].apply(lambda x: x.str.count(' ')) # assigns a variable count_white_spaces to assesses white spaces 

white_spaces # Print Special Characters



""" Step 7. Converts the column types to the correct types (e.g., DOB field is datetime and not object) """

df.dtypes # List all data types of columns

""" my line 66 code broke after i changed the location of my raw csv file from data to data/raw """
df['week'] = pd.to_datetime(df['week']) # changes the data type of column 'week' from a object (Str) into a DateTime 


# verify data type change by listing all datetime data types 

dates = df.select_dtypes(include=['datetime64[ns]']).columns

dates # Prints all DateTime Data types 


"""" Step 8. Look for duplicate rows and remove duplicate rows """"

df.drop_duplicates() # Removes duplicates 

""" Step 9. Assess missingness (count of missing values per column)"""

# replacing blank, empty cells with NaN

df.replace(to_replace='', value=np.nan, inplace=True)

df.replace(to_replace=' ', value=np.nan, inplace=True)

df.isnull().sum() # get a count of missing values in each column



""" Step 10.  New data field """

df['modality_inperson'] = (df['learning_modality'].apply(lambda x: 'true' if x == 'in_person' else 'false')) 

df.to_csv('data/clean/cleaned_School_Learning_Modalities.csv')