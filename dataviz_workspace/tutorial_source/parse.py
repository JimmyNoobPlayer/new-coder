"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.

Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with.

Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.
"""

import csv


#file to be read. not intended to be changed, so use all caps.
FILE = "..\data\sample_sfpd_incident_all.csv" #full (relative) file path of the csv file.



def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object (python list of dictionaries)"""


    #Open the CSV file.
    opened_file = open(raw_file)

    #Read the CSV file, put the data in the proper data structure
    csv_data = csv.reader(opened_file, delimiter=delimiter) #now csv_data is an iterator that returns lists of strings at each call, corresponding to the lines of the original csv file.
    fields = next(csv_data)
    parsed_data = []
	
    #nice little bit of python code.
    #for is like a foreach in c sharp
    #zip takes two iterables and smooshes them into a single iterable of tuples.
    #dict takes an iterator that can be interpreted as a dict and puts it in that form.
    for row in csv_data:
        parsed_data.append(dict(zip(fields,row)))

    #Close the CSV file
    opened_file.close()

    return parsed_data

def main():
    # Call our parse function and give it the needed parameters
    new_data = parse(FILE, ",")

    # Let's see what the data looks like!
    print(new_data[0])

    categories = []
    for dictrow in new_data:
        catname = dictrow["Category"]
        if (categories.count(catname)<1):
            categories.append(catname)
    print(categories)


if __name__ == "__main__":
    main()
