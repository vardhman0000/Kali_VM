#!/bin/python3

#Dictionaries - Key/Value Pair pairs {}

drink = {"White Russian" : 7, "Old Fashion" : 10, "Lemon Drop" : 8}  #drink is key and price is value
print(drink)

employees = {"Finance" :["Bob", "Linda", "Tina"], "IT" : ["Gene", "Louise", "teedy"], "HR" : ["Jimmy", "Mort"]}
print(employees)

employees["Legal"] = ["Mr. Frond"]  # add new key : value pair
print(employees)

employees.update({"Sales" : ["Andie", "Ollie"]})  # add new key : value pair
print(employees)

drink['White Russian'] = 8
print(drink)

print(drink.get("White Russian"))
