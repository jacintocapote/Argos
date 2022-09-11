#!/usr/bin/python3

import csv
import json


def createJSON(CSVFile, JSONFile):
    """createJSON.

    Args:
        CSVFile: path to a CSV file
        JSONFile: path to a JSON file our function will create as output
    """

    # output dict
    outputdict = {}

    # Open CSV for read and store it to our JSON
    with open(CSVFile, encoding='utf=8') as csvFP:
        csvReader = csv.DictReader(csvFP)

        for rows in csvReader:
            # First column must be "CK"
            key = rows['CK']
            outputdict[key] = rows

    # Once we have all our data, generate our output file JSONFile
    with open(JSONFile, 'w', encoding='utf=8') as jsonFP:
        jsonFP.write(json.dumps(outputdict, indent=4))


# Main routine

# Var init
myCSV = r'input/employees.csv'
myJSON = r'output/employees.json'

# Do the magic
createJSON(myCSV, myJSON)
