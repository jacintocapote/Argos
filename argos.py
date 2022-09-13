#!/usr/bin/python3

import glob
import json
import os
import pandas as pd
import pprint


# TODO: create debug mode (and others) with logger


def create_main_dict(input_directory, output_file_name):

    files_list = get_input_files(input_directory, "*.json")
    main_dict = {}  # This will contain the whole info stored in JSON files

    # loop over json files in given dir
    for json_file in files_list:
        with open(json_file) as file:
            # Generate name of child branch under CK
            # At the end of this block, datafile_origin value will be
            # name of original csv file and it'll be used as branch under CK
            # to give us scope of application which originated this info
            datafile_origin = os.path.splitext(os.path.basename(json_file))
            datafile_origin = os.path.splitext(datafile_origin[0])
            datafile_origin = datafile_origin[0]
            locals()[datafile_origin] = {}

            list_of_dicts = json.load(file)  # Each item is a full dict

            for one_dict in list_of_dicts:
                if one_dict['CK'] in main_dict.keys():
                    # TODO: if CK already exists nest it with filename as branch
                    print(f'reading {datafile_origin} since it exists')
                    main_dict[one_dict['CK']][datafile_origin] = one_dict
                else:
                    # if doest'n exist create and nest with filename as branch
                    print(f'reading {datafile_origin}')
                    main_dict[one_dict['CK']] = { datafile_origin: one_dict}
                # pprint.pprint(main_dict)

    # pprint.pprint(main_dict)

    # Dict to JSON and saving file
    json_string = json.dumps(main_dict)
    json_file = open('output/main.json', 'w')
    json_file.write(json_string)


def get_input_files(input_directory, extension):
    """get_input_files.

    Read input directory and look for csv files

    Args:
        input_directory: directory to be listed
        extension: type of files to be listed
    Output:
        file_list: list of files that match given pattern
    """

    # Find all csv in input_director
    # TODO: output logger if found any non csv file
    # print(f'Trying to find {input_directory} and extension {extension}')
    file_list = filter(os.path.isfile, glob.glob(input_directory + extension))
    # print(file_list)

    # Sort them
    file_list = sorted(file_list, key=lambda x: os.stat(x).st_size)

    return file_list


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

    df = pd.DataFrame(pd.read_csv(CSV_file, header=0))
    # TODO: add checks for field integrity
    #   - amount of columns == amount of fields
    #   - further injection checks (column and fields)
    df.to_json(output_file_name, orient="records")


def main():
    csv_input_directory = 'input/'  # Must end with a /
    json_output_directory = 'tmpJSON/'  # This directory will store tmp .json
    json_input_directory = json_output_directory  # Scalabilty purpose
    main_output_directory = 'output/'  # This directory will store main DB

    # Generate a JSON file per CSV
    for csv_file in get_input_files(csv_input_directory, "*.csv"):
        pandas_create_JSON(csv_file, json_output_directory)

    # Read every JSON file and organize them into a dict
    create_main_dict(json_input_directory, main_output_directory)


if __name__ == "__main__":
    main()
