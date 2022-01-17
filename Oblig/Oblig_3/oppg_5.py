from oppgave_5_moviefunction import *
collection = [
    {'title': 'Inception', 'year': 2010, 'rating': 8.7},
    {'title': 'Inside out', 'year': 2015, 'rating': 8.1},
    {'title': 'Con Air', 'year': 1997, 'rating': 6.9},
]

bad_collection = []

append_new_movie(bad_collection, "The Hulk", 1985, 4.5)
append_new_movie(bad_collection, "I Kill You", 1996, 3.4)

append_new_movie(collection, "American Sniper", 2014, 7.3)
append_new_movie(collection, "Dune", 2021, 8.4)
append_new_movie(collection, "Interstellar", 2014, 8.5)
append_new_movie(collection, "Red Cliff", 2008)

list_of_movies(collection)
list_of_movies(bad_collection)

print(f"\nYour average rating for collection movies is {average_rating_in_movies(collection)}")
print(f"\nYour average BAD collection movies is {average_rating_in_movies(bad_collection)}\n")

movies_after_2010(collection, 2010)
print()

export_movie_list(collection, 'movie_list.txt')
export_movie_list(bad_collection, 'bad_movies.txt')

import_movie_list('movie_list.txt')
import_movie_list('bad_movies.txt')
