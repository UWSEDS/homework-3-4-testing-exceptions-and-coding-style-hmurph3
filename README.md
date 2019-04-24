# Homework 3-4: Coding style and Unit tests.

**Note: This homework is double credit.**

In this homework, you will create two python modules.

1. Function code. (8 points) Last week you write python codes that read an online file and created a data frame that has at least 3 columns. For this module: (a) create a python module dataframe.py that reads the data in homework 2; (b) make the codes PEP8 compliant using pylint and (c) extend these codes to generate the following exceptions:

   - Check if the file exists. If it doesn't print a meaningful error message.
  
   - Check that the resulting dataframe has a minimum number of rows (specified by an optional argument). If it doesn't, generate an exception.

1. (6 points) Create a python file test_dataframe.py that has unit tests for dataframe.py. These codes should also be PEP8 complaint. Include at least 2 of the following tests:
  - You have the expected columns.
  - Values in the column are all of the expected type.
  - There are no nan values.
  - The dataframe has at least one row.
