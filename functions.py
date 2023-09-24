#!/bin/python3

#Function
print("Here is an exmpale of function")
def who_am_i():
	name = "Vardhman Jain"
	age = 18
	print("My name is " + name + " and i am " + str(age) + " years old.")
who_am_i()


# Adding Parameters
def add_one_hundred(num):
	print(num+100)
add_one_hundred(150)

# Multiple Parameters
def add(x,y):
	print(x + y)
add(9,9)

def multiply(x,y):
	return x*y
print(multiply(7,7))

def square_root(x):
	print(x**0.5)
square_root(64)

# New line function
def nl():
	print('\n')
nl()
