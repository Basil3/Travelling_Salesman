__author__ = 'Michael'

from tkinter import *
import tkinter
from tkinter import filedialog
import airport
import projecttest
import random

airport_dictionary = airport.createDictionary()
currency_rate_dictionary = currencyRate.currencyRateDictionary()
country_currency_dictionary = currency.currencyCodeDictionary()














def manuallyEnterList():

    example = []

    user = input ("Please enter the salesperson name: ")
    example.append(user)

    while True:
        airport1 = input("Please enter your home airport code: ").upper()
        if airport1 not in airport_dictionary:
            print("That is not a valid entry")
            airport1
        else:
            example.append(airport1)
            print(example)
            break
            print("test")

    while True:
        airport2 = input ("Please enter your first airport code: ").upper()
        if airport2 not in airport_dictionary:
            print("That is not a valid entry")
            airport2
        else:
            example.append(airport2)
            break

    while True:
        airport3 = input ("Please enter your second airport code: ").upper()
        if airport3 not in airport_dictionary:
            print("That is not a valid entry")
            airport3
        else:
            example.append(airport3)
            break

    while True:
        airport4 = input ("Please enter your third airport code: ").upper()
        if airport4 not in airport_dictionary:
            print("That is not a valid entry")
            airport4
        else:
            example.append(airport4)
            break

    while True:
        airport5 = input ("Please enter your fourth airport code: ").upper()
        if airport1 not in airport_dictionary:
            print("That is not a valid entry")
            airport1
        else:
            example.append(airport5)
            break

    calculateLowest(example)






def openFileDialog():
    root = tkinter.Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()

    try:
        filename = tkinter.filedialog.askopenfilename()

        output_file = open("travel_plans.txt", "w")

        with open(filename, mode='r', encoding="utf8") as infile:
                reader = csv.reader(infile)
                for rows in reader:

                    output_file.write("For " + rows[0] + ": \n")
                    output_file.write(calculateLowest(rows) + "\n")

        print ("Your results have been output to travel_plans.txt")
    except:
        print("Unable to open file")
        input("Press Enter to return to main menu...")
        optionsMenu()

def displayOptions():
    print('Options: ')
    print(" '0' Show options")
    print(" '1' Enter 5 airports for cheapest route")
    print(" '2' Read from file")
    print(" '3' Calculate distance between two airports")
    print(" '4' Generate random route with cost")
    print(" '5' Run tests")
    print(" 'q' Quit the program")


def trial_test():
    print("This is the testing menu")
    print("Running test 1: Check distance between airports")
    print("Auckland to Dublin according to webflyer.com = 18200km")
    print("Checking against the program......")
    webflyer_distance = 18200
    result = distanceLongLat('AKL', 'DUB')
    print(result)
    if result > (webflyer_distance*0.98) and result < (webflyer_distance * 1.02):
        print ("The result is within +/- 2% webflyer distance")
        print ("Test passed")
    else:
        print ("Test failed!")
    input("Press Enter to continue to next test...")
'''
def random_program_test():
    random_test = []
    home_city = random.choice(list(airport_dictionary.keys()))
    city1 = random.choice(list(airport_dictionary.keys()))
    city2 = random.choice(list(airport_dictionary.keys()))
    city3 = random.choice(list(airport_dictionary.keys()))
    city4 = random.choice(list(airport_dictionary.keys()))
    random_test = ["Random_user",home_city, city1, city2, city3, city4]
    #print(home_city, city1, city2, city3, city4)
    print(random_test)
    calculateLowest(random_test)
'''

def optionsMenu():
    choice = "0"

    while choice != 'q':
        if choice == '1':
            manuallyEnterList()
            choice = input ("Enter your next option: ")
        elif choice == '2':
            openFileDialog()
            choice = input ("Enter your next option: ")
        elif choice == '3':
            distance = 0
            while True:
                code1 = input("Please enter airport 1 code: ").upper()
                if code1 not in airport_dictionary:
                    print ("That entry is not valid, please try again.")
                    code1
                else:
                    break

            while True:
                code2 = input("Please enter airport 2 code: ").upper()
                if code2 not in airport_dictionary:
                    print ("That entry is not valid, please try again.")
                    code2
                else:
                    break
            distance = distanceLongLat(code1, code2)
            print("The distance is %d km" % distance)
            choice = input ("Enter your next option: ")
        elif choice == '4':
            projecttest.random_program_test()
            #choice = input ("Enter your next option: ")
        elif choice == '5':
            trial_test()
            choice = input ("Enter your next option: ")
        else:
            displayOptions()
            choice = input ("Enter your option: ")






optionsMenu()
