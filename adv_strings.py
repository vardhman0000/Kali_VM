#!/bin/python

my_name = "Vardhman"
print(my_name[0])
print(my_name[-1])

sentence = "this is a sentence"
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = " ".join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"
print(quote)
quote1 = "He said, \"give me all your money\"" # To use quotes as a part of string
print(quote1)

too_much_space = "          hello     "
print(too_much_space.strip())

print("a" in "Apple")

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #Improved

movie = "The Hangover"
print("My favourite movie is {}.".format(movie))  # {}. is a placeholder

