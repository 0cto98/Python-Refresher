from io import StringIO
import csv

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

# Warning: there is a few thing to keep in mind:
# - name can contains comma
# - if a name contains comma then there is double-quote around
# - year is extracted from the name but
#   * not all names have a year
#   * some are badly formatted



# 2. Create two methods which returns the number of each genre in an array called
#    genres like this:

genres_example = [
  ('Adventure', 2134),
  ('Animation', 345),
  # ...
]

# 2.1 using normal loop methods

def count_genres_with_loop(movies):
	pass

# 2.2 using normal list comprehension

def count_genres_with_list_comprehension(movies):
	pass

