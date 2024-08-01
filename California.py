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
                if (index == 0 and (row[0] != "Year" or row[1] != "Sex" or row[2] != "Rank" or row[3] != "Name" or row[4] != "Count" or row[5] != "Data_Revision_Date")):
                    print("File Columns Wrong!")
                    return
                # Year,Sex,Rank,Name,Count,Data_Revision_Date
                # 0      1    2   3   4       5
                # 1960,Female,1,SUSAN,3299,11/07/2022
                if (row[1] == "Male"):
                    BoyArrRank.append(int(row[2]))
                    BoyArrName.append(row[3].title())
                    BoyArrFrequency.append(int(row[4]))
                    BoyArrYear.append(int(row[0]))
                elif (row[1] == "Female"):
                    GirlArrRank.append(int(row[2]))
                    GirlArrName.append(row[3].title())
                    GirlArrFrequency.append(int(row[4]))
                    GirlArrYear.append(int(row[0]))

            BoyObj = {'Rank': BoyArrRank, 'Name': BoyArrName,
                      'Frequency': BoyArrFrequency, 'Year': BoyArrYear}
            BoyDF = pd.DataFrame(BoyObj)

            GirlObj = {'Rank': GirlArrRank, 'Name': GirlArrName,
                       'Frequency': GirlArrFrequency, 'Year': GirlArrYear}
            GirlDF = pd.DataFrame(GirlObj)

            BoyDF.to_csv("CaliforniaBoy.csv", sep=',',
                         index=False, encoding='utf-8')
            GirlDF.to_csv("CaliforniaGirl.csv", sep=',',
                          index=False, encoding='utf-8')
    except:
        print(f"{argv[0]} File Not Found!")


if __name__ == "__main__":
    main(sys.argv[1:])
