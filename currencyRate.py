__author__ = 'Michael'


import csv

class CountryCurrency():
    def __init__(self, country = '', currency_code = '', exchange_to = '1', exchange_from = '1' ):
        self.country = country
        self.currency_code = currency_code
        self.exchange_to = exchange_to
        self.exchange_from = exchange_from

    def getCurrencyCode(self):
        return self.currency_code

    def getExchangeRate(self):
        return self.exchange_to



def currencyRateDictionary():
    with open('currencyrates.csv', mode='r', encoding="utf8") as infile:
        reader = csv.reader(infile)

        currencyConversionDict = {}


        for rows in reader:
            currency_convert = CountryCurrency(rows[0], rows[1], rows[2], rows[3])
            currencyConversionDict[rows[1]] = currency_convert

        return currencyConversionDict

def calculateCost(currencyCode):

        conversion = float(currencyDict.get(currencyCode).exchange_to)
        #print (conversion)
        return conversion

        print(currencyDict)

