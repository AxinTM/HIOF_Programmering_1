# oppgave 5.1
def append_new_movie(movies_list, title, year, rating=5.0):
    movies_list.append({'title': title, 'year': year, 'rating': rating})
    print(f"\n You just added {title} released {year}, and has a rating of {rating}")


# oppgave 5.2
def list_of_movies(movies_list):
    print("\n=====Movie List=====:\n")
    for movie in movies_list:
        print(f"{movie['title']} - {movie['year']} has a rating of {movie['rating']}")


def average_rating_in_movies(movie_list):
    total_rating = 0
    for element in movie_list:
        total_rating += element['rating']
    return total_rating / len(movie_list)


def movies_after_2010(movies_list, year):
    for movie in movies_list:
        if year <= movie.get('year'):
            print(f"{movie['title']} was release after {year}!")


# Oppgave 5.3
def export_movie_list(movie_list, file_name):
    with open(file_name, 'w') as movie_file:
        for movie in movie_list:
            movie_file.write(f"{movie['title']}\n")


def import_movie_list(file_name):
    with open(file_name, 'r') as file:
        imported_movie = file.read()
        print(f'\n{imported_movie}')