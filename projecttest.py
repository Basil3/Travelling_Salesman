__author__ = 'Michael'

import random
import airport

airport_dictionary = airport.createDictionary()

def random_program_test():
    print("test")
    results = []
    from maintest import calculateLowest
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
    print(results)
