from io import StringIO
import csv
from operator import itemgetter #to sort list of tuples

# This lab use the movielens dataset available here
# https://grouplens.org/datasets/movielens/
# download one of them (tips: use a small one)

# 1. create a method load_movies which load the csv file an return a dict
# For instance, the entry: "17, name of the movie (1993), genre1|genre2|genre3"
# is an entry of the dict variable movies is:

movies_entry_example = "17, name of the movie (1993), genre1|genre2|genre3"

movies_example = {
	17: {
		"name": "name of the movie",
		"genres": ["genre1", "genre2", "genre3"],
		"year": 1993
	}
}

#568,Bhaji on the Beach (1993),Comedy|Drama
def load_movies(csv_file):
    dict = {}
    csv_reader = csv.reader(csv_file, delimiter=',',skipinitialspace=True)
    #next(csv_reader)
    for row in csv_reader:
        i = row[0]
        name, year = row[1].split('(')
        name = name[0:-1] #remove space at the end
        year = year[0:-1] #remove ')' at the end
        genres = row[2].split('|')
        dict[int(i)] = {"name": name, "genres":genres, "year":int(year)}
    return dict

assert load_movies(StringIO(movies_entry_example)) == movies_example


# 2. Create two methods which returns the number of each genre in an array called
#    genres like this:

genres_example = [
  ('genre1', 1),
  ('genre2', 1),
  ('genre3', 1)
]

# 2.1 using normal loop methods
def count_genres_with_loop(movies):
    dict = {}
    for movie in movies:
        for genre in movies[movie]["genres"]:
            if genre in dict:
                dict[genre] += 1    #if genre already exists, we add 1
            else:
                dict[genre] = 1     #otherwise we create it and initialize it to 1
    #Then we "translate" dict to an array to fit what is asked
    genres_array = []
    for genre in dict:
        genres_array.append((genre,dict[genre]))
    genres_array.sort(key=itemgetter(0))
    return genres_array

assert count_genres_with_loop(load_movies(StringIO(movies_entry_example))) == genres_example

# 2.2 using normal list comprehension
def count_genres_with_list_comprehension(movies):
	pass

