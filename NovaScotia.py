#!/usr/bin/env python3

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd


def main(argv):

    maleYears = []
    femaleYears = []
    setNames = {}
    maleNames = []
    femaleNames = []
    maleFrequency = []
    femaleFrequency = []
    maleRanks = []
    femaleRanks = []
    maleTotal = 1
    femaleTotal = 1
    total = 0

    try:
        if (sum(1 for line in open(argv[0])) == 0):
            print("Empty File!")
            return
        with open(argv[0]) as csvDataFile:
            csvReader = csv.reader(csvDataFile, delimiter=',')
            for row in csvReader:
                if row[1] == 'M':
                    maleYears.append(int(row[0]))
                    maleNames.append(row[2].title())
                    maleFrequency.append(int(row[3]))
                    maleRanks.append(maleTotal)
                    maleTotal = maleTotal + 1
                elif row[1] == 'F':
                    femaleYears.append(int(row[0]))
                    femaleNames.append(row[2].title())
                    femaleFrequency.append(int(row[3]))
                    femaleRanks.append(femaleTotal)
                    femaleTotal = femaleTotal + 1

                total = total + 1

            if total > 0:
                male = {'Name': maleNames,
                        'Frequency': maleFrequency, 'Year': maleYears}
                male_df = pd.DataFrame(male)
                male_df.sort_values(["Frequency", "Name"], axis=0, ascending=[
                                    False, True], inplace=True)
                male_df.insert(0, 'Rank', maleRanks)

                male_df.to_csv("NovaScotiaBoy.csv", sep=',',
                               index=False, encoding='utf-8')

                female = {'Name': femaleNames,
                          'Frequency': femaleFrequency, 'Year': femaleYears}
                female_df = pd.DataFrame(female)
                female_df.sort_values(["Frequency", "Name"], axis=0, ascending=[
                                      False, True], inplace=True)
                female_df.insert(0, 'Rank', femaleRanks)

                female_df.to_csv("NovaScotiaGirl.csv", sep=',',
                                 index=False, encoding='utf-8')
    except:
        print(f"{argv[0]} File Not Found")


if __name__ == "__main__":
    main(sys.argv[1:])
