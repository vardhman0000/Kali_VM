#!/bin/python3

#Variables and Methods
quote = "All is fair in love and war."
print(quote)
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #titlecase

print(len(quote))

name = 'Vardhman Jain'  # STRING
age = 18  # INTEGER VALUE
cgpa = 9.22  # FLOAT VALUE
print(name)
print(age)
print(cgpa)
print(int(cgpa))

print("My Nmae is "+ name + "and i am " + str(age) + " years old")  # because string and integer can't be concatinated to we need to convert int to string

age += 1  # shorthand operator
print(age)

birthday = 1
age += birthday
print(age)
