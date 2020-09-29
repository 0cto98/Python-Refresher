# 1. Write a method leap_year which determines whether a year (as parameter)
# is leap or not (A year A is leap if A is divisible by 4. However, it is
# not if A is a multiple of 100, unless A is a multiple of 400).

def leap_year(year):
	return (year%4==0 and year%100!=0) or year%400==0

# assert are here to check your solutions. For the next exercices, you will
# have to write assertions to verify your solutions

assert leap_year(1996) == True
assert leap_year(1998) == False
assert leap_year(1900) == False
assert leap_year(2000) == True

# 2. Write a function that, given two integer bounds a and b
# adds the multiple numbers of 3 and 5 between these bounds.
# Take for example a = 0, b = 32, the result should then be 0 + 15 + 30 = 45.

def my_bounds(a,b):
	s = 0
	for i in range (a,b):
		if i%3==0 and i%5==0:
			s+=i
	return s

# Don't forget your assertions !
assert my_bounds(0,32) == 45

# 3. Slightly modify this program so that it adds the multiple numbers of 3 or 5
# between terminals a and b. With terminals 0 and 32, the result should
# therefore be: 0 + 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20
# + 21 + 24 + 25 + 27 + 30 = 225.

def my_new_bounds(a,b):
	s = 0
	for i in range (a,b):
		if i%3==0 or i%5==0:
			s+=i
	return s

# Don't forget your assertions !
assert my_new_bounds(0,32) == 225

# 4. Write a function which take a list as parameter and returns a dictionnary
# with each entry contains the entry as key and the number of
# characters for each entry if the entry is a string (else None)

def check_array_names(a):
	d = {}
	for i in a:
		if type(i)==str:
			d[i]=len(i)
	return d


# Note: The comparaison uses ==, as it can be used to compare dictionnary
# See https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# (does not work for OrderedDict)
assert check_array_names(["abc",3,"blabla"]) == { "abc": 3, "blabla": 6}

