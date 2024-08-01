#!/usr/bin/env python3
import sys
import getopt
import csv
import pandas as pd


def calcdistance(oName, nName):
    distance = 0
    for index, x in enumerate(oName):
        try:
            if (x.lower() == nName[index].lower()):
                distance = distance + 1
        except:
            distance = distance
    return distance


def main(argv):
    orginalName = argv[0]
    name = []
    distance = []

    with open(argv[1]) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for index, row in enumerate(csvReader):
            if (index == 0 and (row[0] != "Rank" or row[1] != "Name" or row[2] != "Frequency" or row[3] != "Year")):
                print("File Columns Wrong!")
                return
            # Rank,Name,Frequency,Year
            # 0  1           2   3
            # 1,Christopher,821,1982
            name.append(row[1])
            distance.append(calcdistance(orginalName, row[1]))

    distanceObj = {'name': name, 'distance': distance, }
    distanceDF = pd.DataFrame(distanceObj)

    distanceDF.sort_values(["distance", "name"], axis=0, ascending=[
        False, True], inplace=True)

    result_df = distanceDF.drop_duplicates(subset=['name'])
    result_df.reset_index(drop=True, inplace=True)

    print(f"Top 10 similar names in {argv[1]} file")
    print("------------------------")
    print(result_df[:10])
    print("------------------------")


if __name__ == "__main__":
    main(sys.argv[1:])
