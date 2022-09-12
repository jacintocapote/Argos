#!/usr/bin/python3

import csv
import glob
import json
import os


def createJSON(CSVFile):
    """createJSON.

    Takes a CSVFile and returns a JSON

    Args:
        CSVFile: path to a CSV file

    Returns:
        A JSON object
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

    # # Once we have all our data, generate our output file JSONFile
    # with open(JSONFile, 'w', encoding='utf=8') as jsonFP:
    #     jsonFP.write(json.dumps(outputdict, indent=4))

    json_object = json.dumps(outputdict)
    return json_object  # TODO: return false if error


def get_input_files(input_directory):
    """get_input_files.

    Read input directory and look for csv files

    Args:
        input_directory:
    """

    # Find all csv in input_director
    # TODO: output logger if found any non csv file
    file_list = filter(os.path.isfile, glob.glob(input_directory + '*.csv'))
    # Sort them
    file_list = sorted(file_list, key=lambda x: os.stat(x).st_size)

    return file_list


def nestJson(mainJSON, newJSON):
    """nestJson.

    Nest newJSON into mainJSON. Both must exist and be well formed; i.e:
        - First branch of mainJSON must be 'CK'
        - CK field must exist in newJSON and be the first field

    CK keys can be duplicated and they will be nested under the same branch.

    :param mainJSON: One existing JSON to serve as foundation for our final
        dataset
    :param newJSON: new JSON file to be appended and nested under first  branch
    """
    main_dict = json.loads(mainJSON)
    print("This is my type")
    print(type(mainJSON))
    print()
    print(mainJSON)


def storeJSON(myJSON, myJSONFile):
    """storeJSON.

    Args:
        myJSON:
        myJSONFile:
    """
    pass


def main():
    csv_input_directory = 'input/'  # Must end with a /
    print(get_input_files(csv_input_directory))


if __name__ == "__main__":
    main()
