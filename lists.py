#!/bin/python3

#Lists - Have square brackets []
movies = ["When Harry Met Sally", "The Hangover", "The perks of being a Wallflower", "The Exorcist"]
print(movies[0])  #Indexing starts from 0
print(movies[1])

print(movies[1:3])
print(movies[1:])
print(movies[:2])
print(movies[-1])
print(len(movies))
movies .append("JAWS")
print(movies)

movies.pop()
print(movies)
movies.pop(0)
print(movies)
