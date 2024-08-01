#!/usr/bin/env python3
import os

ContinueProgram = 1

while ContinueProgram == 1:
    print("1) Format Alberta CSV")
    print("2) Format Australia CSV")
    print("3) Format California CSV")
    print("4) Format New York CSV")
    print("5) Format Nova Scotia CSV")
    print("6) Exit")

    UserInput = input("Enter Choice : ")
    UserInput = int(UserInput)

    try:
        if UserInput == 1:
            os.system('python3 ./Alberta.py ./Alberta1980-2020.csv ')
        elif UserInput == 2:
            os.system('python3 ./Australia.py ./Australia1952-2021.csv ')
        elif UserInput == 3:
            os.system('python3 ./California.py ./California1960-2021.csv ')
        elif UserInput == 4:
            os.system('python3 ./NewYork.py ./NewYork2011-2019.csv ')
        elif UserInput == 5:
            os.system('python3 ./NovaScotia.py ./NoviaScotia1920-2022.csv ')
        else:
            ContinueProgram = 0
    except:
        print(f"Error Running {UserInput}")
        ContinueProgram = 0
