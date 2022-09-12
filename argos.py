#!/usr/bin/python3

import csv
import glob
import json
import os
import pandas as pd


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


def pandas_create_JSON(CSV_file, outputdir):
    """pandas_create_JSON.

    This functions return a JSON file based on a CSV obtained from our main
    pool.

    Args:
        CSV_file: Origin CSV file
        outputdir: Directory which will store .json files

    Return:
        There's no return per-se, .json file named after CSV will be created
        inside outputdir
    """

    output_file_name = os.path.basename(CSV_file)
    output_file_name = outputdir + output_file_name + ".json"  # We DO want .csv.json
    print(f'Reading {CSV_file} and storing it in {output_file_name}')

    df = pd.DataFrame(pd.read_csv(CSV_file, header=0))
    df.to_json(output_file_name, orient="records")


def main():
    csv_input_directory = 'input/'  # Must end with a /
    json_output_directory = 'tmpJSON/'  # This directory will store tmp .json

    # Generate a JSON file per CSV
    for csv_file in get_input_files(csv_input_directory):
        pandas_create_JSON(csv_file, json_output_directory)

    # Read every JSON file and organize them into a dict



if __name__ == "__main__":
    main()
