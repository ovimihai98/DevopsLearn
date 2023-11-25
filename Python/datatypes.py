#Strings

str1 = "alpha"
str2 = 'beta'

#Numbers

num1 = 123
flt1 = 2.0

#Lists / Collection of datatypes, enclosed in square brackets

first_list = [str1, "DevOps", 47, num1, 1.5]
print(first_list)

#Tuple / Collection of datatypes, enclosed in round brackets immutable

first_tuple = (str1, "DevOps", 47, num1, 1.5)
print(first_tuple)

#Dictionary / Elements in the dictionary are always in pairs (Key:value), curly brackets.

first_dictionary = { "Name": "Ovidiu", "Weight":80, "Exercises":["Jogging", "Gym", "Football"]}
print(first_dictionary)

print("Variable first_list is a :", type(first_list))
print("Variable first_tuple is a :", type(first_tuple))
print("Variable first_dictionary is a :", type(first_dictionary))

#Boolean

x = True
y = False
print(type(x))