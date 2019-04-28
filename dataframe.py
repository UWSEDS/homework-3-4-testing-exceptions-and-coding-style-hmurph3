"""
This module imports the City of Seattle Wage Data and creates a dataframe.
There are 5 columns and 12.1K rows.
The columns and their data types are listed below.
Department: String
Last Name: String
First Name: String
Job Title: String
Hourly Rate: Float

*** Note that there is a space at the end of Hourly Rate ***
"""
import pandas as pd


def dataframe():
    """
    This funciton crates a dataframe from the City of Seattle Wage data
    """
    wages = pd.read_csv('https://data.seattle.gov/api/views/2khk-5ukd/'
                        'rows.csv?accessType=DOWNLOAD', sep=',', header=0,
                        names=("Department", "LastName", "FirstName",
                               "JobTitle", "HourlyRate"),
                        dtype={"Department": str, "LastName": str,
                               "FirstName": str, "JobTitle": str,
                               "HourlyRate": float})
    column_titles = ["Department", "LastName", "FirstName", "JobTitle",
                     "HourlyRate"]
    wages_col_titles = list(wages)

    if all(x in column_titles for x in wages_col_titles):
        return wages
    else:
        raise ValueError("Unexpected column titles")
