__author__ = 'Michael'

import csv

class CurrencyCodes():
    def __init__(self, country = '', currency_code = '' ):
        self.country = country
        self.currency_code = currency_code

    def getCountryName(self):
            return self.country

    def getCurrencyCode(self):
            return self.currency_code



def currencyCodeDictionary():
    with open('countrycurrency.csv', mode='r', encoding="utf8") as infile:
            reader = csv.reader(infile)

            countryCurrencyDict = {}

            for rows in reader:
                country_currency = CurrencyCodes(rows[0], rows[14])
                countryCurrencyDict[rows[0]] = country_currency

            return countryCurrencyDict
