#!/usr/bin/env python3

# Libraries
import os
import sys
import getopt
import csv
from collections import Counter
import pandas as pd

def main(argv):

    years1 = []
    numbers1 = []
    names1 = []
    ranks1 = []

    years2 = []
    numbers2 = []
    names2 = []
    ranks2 = []
    

    inputYear  =argv[2]



    print(argv[0])
    print(argv[1])
    print(argv[2])

    # X AREA LIST
    with open ( argv[0] ) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        next(csvReader)
        for row in csvReader:
                years1.append(int(row[3]))
                names1.append(row[1])
                numbers1.append(int(row[2]))
                ranks1.append(row[0])
             

#     #Y AREA list
    with open ( argv[1] ) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        next(csvReader)
        for row in csvReader:
                years2.append(int(row[3]))
                names2.append(row[1])
                numbers2.append(int(row[2]))
                ranks2.append(row[0])


    # read the CSV files into pandas dataframes
    X_df = pd.read_csv(argv[0])
    Y_df = pd.read_csv(argv[1])

    # extract the names from the dataframes
    X_names = set(X_df['Name'].values)
    Y_names = set(Y_df['Name'].values)

    # calculate the intersection of the names
    result = X_names.intersection(Y_names)

    if len(result) == 0:
        print('No matches found')
    else:
        print("Intersecting names in given files")
        # count the frequency of each name in the intersection
        name_counts = Counter(result)

        # sort the names by frequency in descending order
        top_names = sorted(name_counts, key=name_counts.get, reverse=True)[:10]

        # print the top 10 intersecting names
        for name in top_names:
            print(name)
            


if __name__ == "__main__":
    main ( sys.argv[1:] )