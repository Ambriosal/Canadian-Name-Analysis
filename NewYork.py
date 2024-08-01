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
                if (index == 0 and (row[0] != "Year of Birth" or row[1] != "Gender" or row[2] != "Ethnicity" or row[3] != "Child's First Name" or row[4] != "Count" or row[5] != "Rank")):
                    print("File Columns Wrong!")
                    return
                # Year of Birth,Gender,Ethnicity,Child's First Name,Count,Rank
                # 0       1               2               3    4   5
                # 2019,FEMALE,ASIAN AND PACIFIC ISLANDER,Chloe,131,1
                if (row[1] == "MALE"):
                    BoyArrRank.append(int(row[5]))
                    BoyArrName.append(row[3].title())
                    BoyArrFrequency.append(int(row[4]))
                    BoyArrYear.append(int(row[0]))
                elif (row[1] == "FEMALE"):
                    GirlArrRank.append(int(row[5]))
                    GirlArrName.append(row[3].title())
                    GirlArrFrequency.append(int(row[4]))
                    GirlArrYear.append(int(row[0]))

            BoyObj = {'Rank': BoyArrRank, 'Name': BoyArrName,
                      'Frequency': BoyArrFrequency, 'Year': BoyArrYear}
            BoyDF = pd.DataFrame(BoyObj)

            GirlObj = {'Rank': GirlArrRank, 'Name': GirlArrName,
                       'Frequency': GirlArrFrequency, 'Year': GirlArrYear}
            GirlDF = pd.DataFrame(GirlObj)

            BoyDF.to_csv("NewYorkBoy.csv", sep=',',
                         index=False, encoding='utf-8')
            GirlDF.to_csv("NewYorkGirl.csv", sep=',',
                          index=False, encoding='utf-8')
    except:
        print(f"{argv[0]} File Not Found!")


if __name__ == "__main__":
    main(sys.argv[1:])
