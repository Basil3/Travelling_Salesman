__author__ = 'Michael'

import csv
import currencyRate
import currency
import itertools
from operator import itemgetter
from math import pi, sin, cos, acos

airport_dictionary = createDictionary()



class Airport_lookup():

    def __init__(self, idx = -1, airportName = '', cityName = '', countryName = '', code3 = '',
        code4 = '', lat = 0, long = 0, altitude = 0, timeZone = '', DST = '', Tz = '' ):

        self.idx = idx
        self.airportName = airportName
        self.cityName = cityName
        self.countryName = countryName
        self.code3 = code3
        self.code4 = code4
        self.lat = lat
        self.long = long
        self.altitude = altitude
        self.timeZone = timeZone
        self.DST = DST
        self.Tz = Tz

    def getAirportName(self):
        return self.airportName

    def getCityName(self):
        return self.cityName

    def getCountryName(self):
        return self.countryName

    def getLat(self):
        return self.lat

    def getLong(self):
        return self.long


def createDictionary():
    with open('airport.csv', mode='r', encoding="utf8") as infile:
            reader = csv.reader(infile)
            airportDict = {}
            for rows in reader:
                airport_csv = Airport_lookup(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9],rows[10],rows[11])
                airportDict[rows[4]] = airport_csv
            return airportDict



def getCombinations(example):

    total_list = []

    combination_1 = [example[1],example[2],example[3],example[4],example[5],example[1]]

    all_combinations =  (list (itertools.permutations(combination_1)))
    all_combinations_list = [list(i) for i in all_combinations]

    for items in all_combinations_list:
        if items[0] == example[1] and items[5] == example[1] and example[2] in items and example[3] in items and example[4] in items and example[5] in items:

            items.append(totalCostOfTravelv2(items))

            total_list.append(items)

            cheapest_fare = (x for x in total_list)
            result = min(cheapest_fare, key=itemgetter(6))

    return result

def getCombinations_extra(combination):

    total_list = []

    all_combinations =  (list (itertools.permutations(combination)))

    all_combinations_list = [list(i) for i in all_combinations]


    for items in all_combinations_list:
        if items[0] == combination[0] and items[6] == combination[0] and combination[1] in items and combination[2] in items and combination[3] in items and combination[4] in items and combination[5] in items:

            items.append(totalCostOfTravelv2(items))

            total_list.append(items)

            cheapest_fare = (x for x in total_list)
            result = min(cheapest_fare, key=itemgetter(7))

    return result


def totalCostOfTravelv2(items):

    total_cost = 0

    for i in range(len(items)-1):

        trip = costOfTravel(items[i], items[i+1])
        total_cost = total_cost + trip

    return(total_cost)

def costOfTravel(airport1, airport2):

    distance = distanceLongLat(airport1, airport2)

    test = airport_dictionary.get(airport1).getCountryName()

    conversion_currency_code = country_currency_dictionary.get(test).getCurrencyCode()

    conversion_rate = currency_rate_dictionary.get(conversion_currency_code).getExchangeRate()

    cost_of_travel = distance*float(conversion_rate)

    return cost_of_travel

def distanceLongLat(code1, code2):

        radius_of_earth = 6373

        lat1 = airport_dictionary.get(code1).getLat()
        long1 = airport_dictionary.get(code1).getLong()
        lat2 = airport_dictionary.get(code2).getLat()
        long2 = airport_dictionary.get(code2).getLong()

        lat1 = (90-(float(lat1))) * (2*pi/360)
        long1 = (float(long1)*(2*pi/360))
        lat2 = (90-(float(lat2))) * (2*pi/360)
        long2 = (float(long2))*(2*pi/360)
        distance = (acos ((sin (lat1)) * (sin(lat2)) * (cos(long1 - long2)) + (cos(lat1) * cos(lat2))) * radius_of_earth)

        return distance

def calculateLowest(example):

        combination_1 = [example[1],example[2],example[3],example[2],example[4],example[5],example[1]]
        combination_2 = [example[1],example[2],example[3],example[4],example[3],example[5],example[1]]
        combination_3 = [example[1],example[2],example[4],example[3],example[4],example[5],example[1]]
        combination_4 = [example[1],example[2],example[5],example[3],example[4],example[5],example[1]]

        result_list = []
        result_list_extra = []

        result1 = getCombinations(example)
        result2 = getCombinations_extra(combination_1)
        result3 = getCombinations_extra(combination_2)
        result4 = getCombinations_extra(combination_3)
        result5 = getCombinations_extra(combination_4)


        result_list.append(result1)
        result_list_extra.append(result2)
        result_list_extra.append(result3)
        result_list_extra.append(result4)
        result_list_extra.append(result5)

        cheapest_fare = min(result_list, key=itemgetter(6))
        cheapest_fare_extra = min(result_list_extra, key=itemgetter(7))

        if (cheapest_fare[6] == cheapest_fare_extra[7]):
            cheapest_overall = cheapest_fare

            results =  ("The cheapest route is " + str(cheapest_overall[0]) + " -> " + str(cheapest_overall[1]) + " -> " + str(cheapest_overall[2]) +
                   " -> " + str(cheapest_overall[3]) + " -> " + str(cheapest_overall[4]) + " -> " + str(cheapest_overall[5]) + " -> " + " and costs \u20ac%.2f" % (cheapest_overall[6]))
            print (results)
        else:
            cheapest_overall = cheapest_fare_extra
            results =  ("The cheapest route is " + str(cheapest_overall[0]) + " -> " + str(cheapest_overall[1]) + " -> " + str(cheapest_overall[2]) +
                   " -> " + str(cheapest_overall[3]) + " -> " + str(cheapest_overall[4]) + " -> " + str(cheapest_overall[5]) + " -> " + str(cheapest_overall[6]) + " and costs \u20ac%.2f" % (cheapest_overall[7]))
            print (results)

        return results


def calculateCostBetweenTwoAirports():

    airports = []

    while True:
        airport1 = input("Please enter the first airport: ").upper()
        if airport1 not in airport_dictionary:
            print("That is not a valid airport, please try again.")
            airport1
        else:
            airports.append(airport1)

    while True:
        airport2 = input ("Please enter the second airport: ").upper()
        if airport2 not in airport_dictionary:
            print("That is not a valid airport, please try again.")
            airport2
        else:
            airports.append(airport2)


    cost = costOfTravel(airports)


    print(cost)