#!/bin/python3

# Conditional statements

def drink(money):
	if money >= 2 :
		return "You can Buy a drink"
	else :
		return "Not enough money"
print(drink(3))
print(drink(1))

def alcohol(age, money):
	if(age>=21) and (money>=5):
		return "You are eligible to have a Drink"
	elif (age>=21) and (money<5):
		return "Age is OK!! but Come back with more money"
	elif (age<21) and (money>=5):
		return "Nice try Kid!!"
	else:
		return "You are too young and don't have enough money"
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))
