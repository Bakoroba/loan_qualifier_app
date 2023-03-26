# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

#Save qualifying loans CSV data
def save_csv(qualifying_loans):
    #variable to store the output_fcsvfile_name 
    output_csvfile_name = questionary.text("Please enter a file path and file name for the qualifiyng loans (for exapmple data/myfile.csv)").ask()
    qualifying_loans_csvfile = Path(output_csvfile_name)
    with open(qualifying_loans_csvfile,"w",newline="") as savecsvfile:
        csvwriter=csv.writer(savecsvfile)
        for loan in qualifying_loans:
            #write loan value row in the csv file
            csvwriter.writerow(loan)