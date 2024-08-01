#!/usr/bin/env python3
import sys
import getopt
import csv
import pandas as pd


def main(argv):
    BoyArrRank = []
    BoyArrName = []
    BoyArrFrequency = []
    BoyArrYear = []
    GirlArrRank = []
    GirlArrName = []
    GirlArrFrequency = []
    GirlArrYear = []

    try:
        if (sum(1 for line in open(argv[0])) == 0):
            print("Empty File!")
            return
        with open(argv[0]) as csvDataFile:
            csvReader = csv.reader(csvDataFile, delimiter=',')
            for index, row in enumerate(csvReader):
                if (index == 0 and (row[0] != "Rank" or row[1] != "Name" or row[2] != "Count" or row[3] != "Gender" or row[4] != "Year")):
                    print("File Columns Wrong!")
                    return
                # Rank,Name,Count,Gender,Year
                # 0  1      2   3    4
                # 1,OLIVER,695,Male,2021
                if (row[3] == "Male"):
                    BoyArrRank.append(int(row[0]))
                    BoyArrName.append(row[1].title())
                    BoyArrFrequency.append(int(row[2]))
                    BoyArrYear.append(int(row[4]))
                elif (row[3] == "Female"):
                    GirlArrRank.append(int(row[0]))
                    GirlArrName.append(row[1].title())
                    GirlArrFrequency.append(int(row[2]))
                    GirlArrYear.append(int(row[4]))

            BoyObj = {'Rank': BoyArrRank, 'Name': BoyArrName,
                      'Frequency': BoyArrFrequency, 'Year': BoyArrYear}
            BoyDF = pd.DataFrame(BoyObj)

            GirlObj = {'Rank': GirlArrRank, 'Name': GirlArrName,
                       'Frequency': GirlArrFrequency, 'Year': GirlArrYear}
            GirlDF = pd.DataFrame(GirlObj)

            BoyDF.to_csv("AustraliaBoy.csv", sep=',',
                         index=False, encoding='utf-8')
            GirlDF.to_csv("AustraliaGirl.csv", sep=',',
                          index=False, encoding='utf-8')
    except:
        print(f"{argv[0]} File Not Found!")


if __name__ == "__main__":
    main(sys.argv[1:])
