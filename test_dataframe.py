"""
Unit tests for dataframe.py
These tests verify the created dataframe:
-- has expected columns.
-- the values in the column are all of the expected type.
-- there are no nan values.
-- the dataframe has at least one row.

The City of Seattle Wage data and has 5 columns and 12.1K rows.
The columns and their data types are listed below.
Department: String
Last Name: String
First Name: String
Job Title: String
Hourly Rate: Float
"""

from dataframe import dataframe


def test_col_names():
    """
    Tests the column names in the created dataframe are the same as
    in the Wage data
    """
    data = dataframe()
    column_titles = ["Department", "LastName", "FirstName", "JobTitle",
                     "HourlyRate"]
    data_col_titles = list(data)
    assert all(x in column_titles for x in data_col_titles)


def test_col_types():
    """
    Tests the data types match what is in the Wage Data
    """
    data = dataframe()
    assert (data.dtypes.Department == str and data.dtypes.LastName == str and
            data.dtypes.FirstName == str and data.dtypes.JobTitle == str and
            data.dtypes.HourlyRate == float)


def test_no_na():
    """
    tests that there are no empty values in the dataframe

    """
    data = dataframe()
    assert data.isnull.values.any()


def test_more_than_one_row():
    """
    tests that there is more than one row in the dataframe
    """
    data = dataframe()
    assert data.shape[1] >= 1
