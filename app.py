# Module
import math

# print       ('hello world');

# '''
# fsdfsdfdsfdfd
# fdsfdsfdfdfdf
# fdfdfdfdfdf
# '''
# Command Line: cd mkdir pwd ls cd ..
# to_do = '50'


# name = "              iqbal         "
# age = "28"
# print(name.capitalize())
# print(name.title())
# print(name + "J" + age)
# print(len(name))
# print(name[0:4])
# print(name[0:])
# print(name[1:4])
# print(name.upper())
# print(name.lower())
# print(name.strip())
# print(name.lstrip())
# print(name.rstrip())
# print(name.find("a"))

# print (name.replace('q', 'h'));
# print("su" in name)
# print('iq' not in name)
# print(f"Iqbals age is {age} , {name}")  # f'{}'
# print (type(None))
# num = -45.47
# print(round(num))
# print(abs(num))

# print(math.sin(60))
# print(math.cos(60))


# print(math.ceil(2.03))
# print(math.floor(2.99))
# print(math.trunc(-2.958))
# x = input("number: ")
# print(type(x))
# print(x)
# y = int(x) + 20
# print(y)
# print(type(y))
# Falsy Values : 0, '', None
# a = None
# if(a):
#     print('a is True')
# else:
#     print('a is False')
# int(), float(), str(), bool()
# print(bool(0));
# a = 3
# b = 5
# print(id(3))
# print(id(a))
# print(id(4))
# print(id(b))
# Everything in python is object (same as JS)
# c = 'text'
# print(id(c))
# print(id('text'))
# c = 3;
# print( id (c))
# print(id ('text'))
# d = 3;
# print ( id (d));
# def hello():
#     print('hello world')
# f = hello
# hello()
# f()
# def house():
#     print("Beautiful!")
# house()
# a = 9
# samena = house
# # print(f"Samena: {a}")
# samena()

# ////////////////////Name Spaces - Scope in JavaScript

# global_name = 25
# global_name = 45
# print(global_name)
# print(id(global_name))


# def outer():
#     a = 2
#     print("hi")
#     print(id(a))
#     # global global_name
#     global_name = 35
#     print(global_name)
#     print(id(global_name))

#     def inner():
#         a = 3
#         print(f"Inner A = {id(a)} and Global {global_name}")

#     print(f"Outer A = {id(a)}")
#     inner()


# outer()

# print(id(global_name))
# //////////////Conditional Operators
# print(ord("a"))  # Different character has different numerical form
# print(ord("*"))
# print(ord("b"))
# print(4 == "4")
# print(4 >= int("4"))
# print(4 <= int("5"))
# print(4 == "4")

# a = -2
# if a >= 20:
#     print("a")
# elif a == 30:
#     print("b")
# else:
#     print("boom")
# result = "Passed" if (a > 2) else "Failed"
# print(result)

# ////////////// Logical Operator
"""
# 1. and
# 2. or
# 3. not
 """
# good_salary = True
# good_health = True
# # good_health = True
# if good_health and good_salary:
#     print("Eligible for loan")
# else:
#     print("Not Eligible for loan")
# if not good_health:
#     print("Eligible for loan GH")
# else:
#     print("Not Eligible for loan")
# ////////////////////LOOPS

# for x in range(10):
#     print(x)
# for x in range(10, 100, 10):
#     print(f"loop runned {(x / 10)} time(s)")
# success = False
# for x in range(0, 3):
#     print(x)
#     if success:
#         print("Success")
#     else:
#         print("Failed")
#         break
# else:
#     print("hi")
# //////////Nested Loops
# for x in range(2, 6, 2):
#     for y in range(2):
#         for z in range(5):
#             print(x, y, z)

# While Loop
# temperature = 35
# while temperature >= 20:
#     print(temperature)
#     temperature -= 5

# Functions - Part 1
# def sum(x, y):
#     print(f"{x} + {y} = {x+y}")
#     print(f"{x} - {y} = {x-y}")
#     print(f"{x} * {y} = {x*y}")
#     print(f"{x} / {y} = {x/y}")


# sum(2, 3)
# sum(x=4, y=7)
# Keyword Arguments
# /////////////////////
# def sum(z, x, y):  # Default Parameter / Optional Parameter
#     print(f"{x} + {y} + {z} = {x+y+z}")
#     print(f"{x} - {y} - {z}= {x-y-z}")
#     print(f"{x} * {y} * {z}= {x*y*z}")
#     print(f"{x} / {y} / {z}= {x/y/z}")


# sum(2, 3, 6)
# sum(x=4, y=7)
# # Keyword Arguments
# sum(10, 10, 11)
# ///////////// By returning a Value
# def ticketValidity(date=True, payment=False):
#     if date or payment:
#         return "Your ticket is valid!!"
#     else:
#         return "Your ticket is invalid!!"


# ticketCheck = ticketValidity()
# print(ticketCheck)
# /////// Non Keyword Arguments -Tuple

# g = 20


# def num(*numbers):
#     print(numbers)
# global g
# for num in numbers:
#     g = g * num
#     return g


# value = num(1, 2, 3, 4)
# print(value)
# # /////// Keyword Arguments - Dictionary
# def identity(**informations):
#     return informations


# person = identity(name="Iqbal", pet="cat", cell="+49015901950063")
# print(person)


# ///////////////////////////Samena Teaching/////////////
"""
Python - Higher level Programming Language , OOL, Similar to JavaScript (around 50%)
Python Interpreter - Code compile 
Software: Python , VSCode / Atom Editor
Extension: .py 
Ex: something.py
Code Formatter: autopep8, black
# Variables - Container (Data)
a = 4 (any data type)
a is a var
DATA TYPE:
- Number - Integer / Float
- String "anything"
- List [3, 4, 'iqbal']
- Dictionary (key-value) {'name': 'samena', 'id': '220631'}
- Tuple (same as list but ordered) 
- Set 
- Boolean (True, False)
- None 
"""

# name = "Iqbal"
# print(name)
# num = 10
# num2 = 10.1
# iqbal = True
# ls = [1, 23, 444, 5]
# tup = (2,3,2,3,2)
# dic = {'name': 'samena', 'id': '220631'}
# print(type(name))
# print(type(num))
# print(type(num2))
# print(type(iqbal))
# print(type(ls))
# print(type(tup))
# print(type(dic))
# print(type(None))
# a = 4

# dialog = 'Iqbal is good boy.'
# print(len(dialog))
# g = 4

# /////////////List Methods


# cats = ["cat"] * 10
# print(cats)

# a = [1, 2, 3]
# b = [4, 5 ,56,]
# mixed = a + b
# print(mixed)
# a = []
# a = list(range(100))
# a = list(range(5)) # Something Iterable
# a = list((1,2,3,4))
# a = list('iqbal')
# list_item = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_item1 = [1, 2, 3] * 5
# print(list_item[0])
# print(list_item[:])
# print(list_item[:4])
# print(list_item[2:6])
# print(list_item[::2])
# print(list_item[2::2])
# print(list_item[3::3])
# print(list_item[1:8:2])
# item1, item2, *others = list_item
# item1, *others, item2, item3, item4 = list_item
# list_item = ["icecream", 2, "car", 4, 5, 6, 7, 8, 9]
# for item in list_item:
#     print(item)
# for  item in enumerate(list_item):
#     print(item ) #Gives Tuple
# for index, item in enumerate(list_item):
#     print(index,item)
# list_item.append(900)
# list_item.insert(2, {"name": "samena", "job": "MCD", "age": 45})
# list_item.insert(3, 'iqbal')
# list_item.pop();
# list_item.pop(2)
# list_item.pop(-2);
# list_item.remove('car')
# del list_item[0:2]
# del list_item[2:7]
# print(list_item.clear())
# list_item_str = ["iqbal", "mou", "akter"]
# print(" - ".join(list_item_str)) #Only works for string
# print(list_item_str.index('akter'))
# print(list_item_str.index('holy'))
# list_item_str = ["iqbal", "mou", "akter", 'samena']
# names = ["holy", "iqbal", "mou", "samena"]


# def find_name():
#     for name in names:
#         if name in list_item_str:
#             print(f"{name} is here")
#         else:
#             print(f"{name} is not here")


# find_name()
# print(list_item1.count(1))
# ///////// Sorting
# player_list = [
#     1,
#     2,
#     3,
#     4,
#     0.8,
#     596,
#     5,
#     6,
#     7.2,
#     5.6,
# ]
# player_list.sort()
# print(player_list)
# player_list.sort(reverse=True)
# print(player_list)
# print(sorted(player_list))
# print(sorted(player_list,reverse=False))
# print(sorted(player_list,reverse=True))
# products = [
#     ("cup", 7),
#     ("beer", 0.7),
#     ("cigerette", 8.5),
#     ("mobile", 650),
#     ("hamburger", 2),
#     ("pasta", 8),
# ]
# print(products)
# print(sorted(products))
# products.sort()
# print(products)
# def sort_products(items):
#     return items[1]


# products.sort(key=sort_products)
# print(products)
# /////////List Comprehensions

# Syntax is [expression for item in list]
# products = [
#     ("cup", 7),
#     ("beer", 0.7),
#     ("cigerette", 8.5),
#     ("mobile", 650),
#     ("hamburger", 2),
#     ("pasta", 8),
# ]
# products_new = [product[0] for product in products]
# products_new1 = [product[1] for product in products]
# print(products_new, products_new1)
# With Conditions (single and two )
# modified_products = [product[1] for product in products if product[1] >= 7]
# For two conditions you have to use if else
# player_list = [1, 2, 3, 4, 5, 6, 7.2, 5.6, 0.8]
# modified_player_list = [player if player < 3 else player / 3 for player in player_list]
# modified_player_list2 = [player for player in player_list if player < 3]


# # ////////////Swapping the list items

# names = ["iqbal", "mou", "noman", "enni"]
# names[0], names[1], names[2], names[3] = names[0], names[1], names[3], names[2]
# print(names)
# # you have to use whole list
# /////////////////////Dictionary
# person = {"name": "iqbal", "job": "student", "age": 28, "favorite_food": "kacci", "favorite_color": "blue"}
# print(person)
# print(person['job']);
# person['name'] = 'jhony sins'
# person['job'] = 'pornstar'
# print(person)
# print(person['name'].capitalize());
# person['favorite_food'] = 'biryani' , 'pasta', 'noodles'
# print(person)
# person['favorite_movie'] = 'Despicable Me', 'Troy', "Avengers"
# print(person['favorite_movie'])
# print(person['favorite_color'])
# Get methods
# print(person.get('favorite_color', 'black'))
# /////////////////// Dictionary Methods
# person = {"name": 'iqbal', "job": "student", "age": 28, "favorite_food": "kacci", "favorite_color": "blue"}
# person.clear()
# print(person)
# person2 = person.copy()
# person2["favorite_food"] = "biryani", "kabab"
# print(person2)
# person3 = dict.fromkeys(person)
# person3['favorite_food'] = 'alu parata'
# print(person3);
# Items and keys Method
# print(person.items())
# person['job'] = 'developer'
# # del person['age']
# print(person.items())
# print(person.keys())
# del person['job']
# print(person.keys())
# print(person.values())
# print(person.popitem())
# person.setdefault('Smoking')
# person.setdefault('Smoking', True)
# person.setdefault("name", "Saim")
# print(person["name"])
# ///Pop Method
# person = {
#     "name": "iqbal",
#     "job": "student",
#     "age": 28,
#     "favorite_food": "kacci",
#     "favorite_color": "blue",
#     "favorite_gun": "Sniper",
# }
# poped = person.pop("job")
# print(poped)
# poped = person.pop('favorite_gun')
# poped = person.pop('favorite_gun', 'AK-47') # If not exist there
# print(poped)
# // Update Method
# lost_key = {"favorite_music": "habibi"}
# person.update(lost_key)
# person.update(dog='Krypto', cat='Pupa')
# //////////// Dictionary Comprehensions
# dictionary = {}
# for x in range(5):
#     dictionary[x] = x + 1;

# print(dictionary)
# player_list = {"Iqbal": 28, "Abir": 39, "Sadiq": 50, "Gandu": 62}
# new_player_list = {player_name: age / 2 for (player_name, age) in player_list.items() }
# print(new_player_list)
# new_player_list = {player_name: age / 2 for (player_name, age) in player_list.items() if age > 30}
# print(new_player_list)

# Dictionary Comprehension Example
# age_calculator = {"Iqbal": 29, "Abir": 39, "Sadiq": 50, "Gandu": 62, "mou": 25, "sifat": 27}
# who_is_young = {player: "young" if age < 30 else "old" for (player, age) in age_calculator.items()}
# who_is_young = {player:age for (player, age) in age_calculator.items() if age > 25 and age % 2 == 1}

# new_dict = {k1: {k2: k1 * k2 for k2 in range(1, 5)} for k1 in range(2, 5)}
# print(new_dict)
# More elaborately
# new_dict = {}
# for k1 in range(2,5):
#     new_dict[k1] = {k2: k1*k2 for k2 in range(1,5)}
# print(new_dict)
# Iterating Dictionary
# age_calculator = {"Iqbal": 29, "Abir": 39, "Sadiq": 50, "Gandu": 62, "mou": 25, "sifat": 27}
# for age_key in age_calculator:
#     print(age_key)  # by default you will get key
# for age_key in age_calculator:
#     print(age_calculator[age_key])  # To get the value
# ////// Tuples
# a = (1,2, 4)
# b = tuple(a)
# print(a, b)
# c = ('ham')
# print(c)
# print(type(c))
# d = ('ham',)
# print(d)
# print(type(d))
# names = ('iqbal', 28, 'OvGU')
# person_name, age, school = names
# print(age)
# /// Indexing and Slicing Same as Lists
# contents = ("iqbal", 28, ["Great Persia", "Halalua"], {7, 8, 9}, {"friend": "Zaed", "color": "brown"})

# print(contents[2])
# print(contents[3])
# print(contents[:])
# print(contents[1:2])
# print(contents[:3])
# print(contents[:-2])
# print(contents[:-3])
# contents[0] = 'noman' #TypeError (tuple is immutable)
# contents[2][1] = "noman"  # TypeError (tuple is immutable)
# print(contents)

# bamboo = (555, 222, 555, 222, 5, 5)
# mixed = contents + bamboo
# del mixed
# print(mixed)
# print(contents.count('iqbal'))
# print(contents.count('iq'))
# print(contents.index({7,8,9}))
# print({7,8,9} in contents )
# for content in contents:
#     print(content)
# /////////////////Sets /////////////
# first_set = {1, 2, 3, 4, 89, 5, 3, 4, 6}
# print(first_set)
# # set is immutable, takes immutable data types. set is unordered
# first_set[1] = 'iqbal' # Don't support item assignment
# second_set = set((1, 2, 34))  # set method takes mutable data
# print(second_set)
# third_set = set([1, 2, 34, 54])
# print(third_set)
# fourth_set = set({'name': 'iqbal','age': 45})
# print(fourth_set) #For dictionary it only takes keys
# # Empty Sets
# c = set()
# print(c)
# print(type(c))
# ////////// Set Methods ///////////////////////////
# set1 = {1, 2, 3}
# set1.add(
#     "iqbal",
# )
# set1.update((3,4 ,5))
# print(set1)
# set1.update([7 ,7,8,9, 'mou'], ('bamboo', 'biryani'), {'cake': True})
# print(set1)
# trust = {2, 3,4,5}
# trust.discard(4)
# print(trust)
# trust.discard(8) # No error will be shown
# trust.remove(2)
# print(trust)
# trust.remove(8) # It will show a KeyError
# trust.clear()
# print(trust)
# //////////// Set Operators ////////////////
# A = {1, 2, 3, 4, 5, 6}
# B = {4, 5, 6, 7, 8, 9, 0}
# Set Union
# print(A | B)
# print(B | A)
# print(A.union(B))
# print(B.union(A))
# Set Intersection
# print(A & B)
# print(B & A)
# print(A.intersection(B))
# print(B.intersection(A))
# Set Difference
# print(A - B)
# print(B - A)
# print(A.difference(B))
# print(B.difference(A))
# Set Symmetric Difference
# print(A ^ B)
# print(B ^ A)
# print(A.symmetric_difference(B))
# print(B.symmetric_difference(A))
# Set Copy
# numbers = {1, 2, 3, 4, 5, 6}
# other_numbers = numbers
# print(other_numbers)
# numbers.discard(1)
# print(other_numbers)
# print(id(numbers))
# print(id(other_numbers))
# new_numbers =  numbers.copy()
# print(new_numbers)
# new_numbers.remove(3)
# print(numbers)
# print(new_numbers)
# Set isdisjoint method
# A = {1, 2, 4,5}
# B ={5, 6 ,7}
# C = {'iqbal', 1}
# A.isdisjoint(B)
# print(B.isdisjoint(C))
# print(B.isdisjoint(A))
# print(A.isdisjoint(B))
# print(A.isdisjoint(C))
# Set issubset and issuperset method
# A = {1,2 ,3}
# B = {1, 2,3, 4,5,6,7}
# C = {1, 3, 4,5,6}
# D = {0, 4, 5}
# print(A.issubset(B))
# print(B.issubset(A))
# print(C.issubset(B))
# print(D.issubset(B))
# print(B.issuperset(B))
# print(B.issuperset(A))
# print(B.issuperset(D))
# print(C.issuperset(A))
# Set Membership Test
# B = {1, 2, 3, 4, 5, 6, 7}
# print(1 in B)
# print(9 in B)
# print(4 in B)
# # Set Loop
# for num in B:
#     print(f"number {num}")
# /////////Frozen Sets
# immutable
# Creating a frozen sets
# new_frozenset1 = frozenset({1, 2,4})
# new_frozense2 = frozenset([1, 2,4,5])
# new_frozenset3 = frozenset((1, 2,4, 'kuky'))
# print(new_frozenset1, new_frozense2, new_frozenset3)
# print(new_frozenset1.isdisjoint(new_frozenset3));
# vowels = ['a', 'e', 'i']
# frozen_vowel = frozenset(vowels)
# print(frozen_vowel)
# empty_frozen_set = frozenset()
# empty_frozen_set.add() # You will get an attribute errror. Because frozen set is immutable
# Set Comprehensions
# numbers = {number**3 for number in range(5)}
# print(numbers)
# numbers = {number**2 for number in range(10) if number > 3}
# print(numbers)

# # ///////////Filter Method
# letters = ["a", "b", "e", "p", "o", "j", 0, False, '0', 'f']


# def check_vowel(letter):
#     vowel = ["a", "e", "i", "o", "u"]
#     if letter in vowel:
#         print(f"{letter} - True")
#     else:
#         print(f"{letter} - False")


# filtered_vowel = filter(check_vowel, letters)
# print(filtered_vowel)

# for letter in filtered_vowel:
#     print(letter)

# # If no functions are provided than it will filter falsy values
# filtered_values = filter(None, letters)
# for letter in filtered_values:
#     print(letter)
# //////////////////////// Anonymous Function/ Lamda //////////

# products = [
#     ("potato", 2.86),
#     ("tomato", 2.47),
#     ("broccoli", 1.99),
#     ("fish", 5.99),
#     ("beef", 6.99),
#     ("rice", 0.99),
# ]
# products.sort(key=lambda product: product[1])
# # print(products)

# # Lamda + Filter Functions
# product_price = [
#     11,
#     22,
#     5,
#     25,
#     58,
#     2,
#     78,
#     25,
#     8,
#     29854,
#     968,
#     546,
#     964,
#     1,
#     56,
#     978,
#     5468,
#     9,
#     78,
#     978,
#     546,
#     978,
#     546,
#     9781546,
#     978,
#     978,
#     56,
#     4,
#     987,
# ]
# filtered_price = filter(lambda x: x % 2 == 0, product_price)
# filtered_price = filter(lambda x: x % 2, product_price)
# filtered_price = map(lambda x: x % 2 , product_price)
# # print(filtered_price)
# print(list(filtered_price))
# for price in filtered_price:
#     print(
#         price
#     )  # here you will get empty array because the iterator got from filter method can be iterated only once in whole interpretation
#     # print(list(filtered_price))
# //////////////////////// Map Method ////////////////////
# num1 = [1, 2, 3, 4, 5]
# num2 = [6, 7]
# for num in num1:
#     print(num * num2)
# for num in num2:
#     for number in num1:
#         print(num * number)
# //////////// MAP ///////////////////
# num1 = [1, 2, 3, 4, 5]
# num2 = [6, 7]
# mapped_numbers = list(map(lambda n1: n1**2, num1))
# print(mapped_numbers);
# # Map method Stops when the shortest iterable is exhausted.
# new_numbers = map(lambda n1, n2: n1 + n2 , num1, num2);
# print(list(new_numbers))
# //////////// Zip Methods //////////////

# number_list = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# character_list = ["ONE", "TWO", "THREE"]
# order_list = ("First", "Second", "Third", "Fourth", "Fifth")
# zipped = zip(number_list, order_list, character_list)
# zipped = zip(number_list, order_list)
# print(set(zipped))
# print(list(zipped))
# // Unpacking zipped
# number, order, character = zip(*zipped)
# print(number, order, character)
# //////////////////// ARRAYS /////////////////
# from array import array

# numbers = array("i", [1, 2, 3])
# print(numbers)

# price = array("f", [1.99, 2.56, 6.559])
# print(price)
# ///////////// Generator Expressions //////////////////
# Same syntax as list comprehension but use of parenthesis
# numbers_gen = (x * 2 for x in range(10))
# numbers_gen = (x * 2 for x in range(100))
# numbers_gen = (x * 2 for x in range(1000))
# numbers_gen = (x * 2 for x in range(10000))
# numbers_gen = (x * 2 for x in range(100000))
# numbers_gen = (x * 2 for x in range(1000000))
# print(numbers_gen)
# print(type(numbers_gen))
# for number in numbers_gen:
# print(number)
# numbers_list = [x * 2 for x in range(10)]
# numbers_list = [x * 2 for x in range(100)]
# numbers_list = [x * 2 for x in range(1000)]
# numbers_list = [x * 2 for x in range(10000)]
# numbers_list = [x * 2 for x in range(100000)]
# numbers_list = [x * 2 for x in range(1000000)]
# Now lets compare the sizes
# from sys import getsizeof

# print(f"GO: {getsizeof(numbers_gen)}")
# print(f"LCE: {getsizeof(numbers_list)}")
# Generator Expressions are very very memory efficient for infinte number of data storing compared to list
# ///////////// Unpacking Operator //////////////////////
# USE '*'
# It is like spread operator in JS
# numbers = [1,2,3,4,5,6]
# print(numbers)
# print(*numbers)
# numbers = range(2,100, 6)
# print(numbers)
# print(list(numbers))
# print(*list(numbers))
# name = 'iqbal'
# print(name)
# print(*name)
# print(list(name))
# print(*list(name))
# number = [1, 2, 3]
# name = "kalia"
# mixed = set([*number, *name])
# print(mixed)
# print(*mixed)
# // For Dictionaries (USE '**')
# person = {"name": "iqbal", "job": "student"}
# person_address = {"home": "Dr. grosz strasse - 4", "room": 703}
# person_last = {"name": "khandakar", "skills": ["python", "javascript"]}  # if same key, the value will be last one
# person_all = {**person, **person_address, "country": "Germany", **person_last}
# print(person_all)
# ////////////////////// RECURSIVE FUNCTIONS /////////////////
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)  # Recursive function call


# number = 3
# print(f"The factorial of {number} is {factorial(number)}")
# first factorial(3) return 3 * factorial(2) = 2 , where factorial 2 returns 2 - factorial(1) = 1,
# So 3*2*1 = 6
# ///////////////////// Exceptions Handling /////////////////////
# print(int(input("Age: ")))
import sys

# Try Except block (Same as try catch block like JS)
# try:
#     age = int(input("Age: "))
# except ValueError as exp_error:
#     print("please enter a valid age")
#     print(exp_error)
#     print(type(exp_error))
# else:
#     print("No Errors Here")
random = ["a", 0, 2]
# for entry in random:
#     try:
#         print("The entry is:", entry)
#         r = 1 / int(entry)
#         break
#     # except ValueError as val_err:
#     except:
#         # print("Please enter the valid number!")
#         print("Opps! the", sys.exc_info()[0], "occured!")
#         # print(sys.exc_info)
#         # print(type(sys.exc_info))
#         # print(sys.exc_info())
#         # print(type(sys.exc_info()))
# print()
# print(f"The reciprocal of {entry} is {r}")
# for entry in random:
#     try:
#         print("The entry is:", entry)
#         r = 1 / int(entry)
#         break
#     except Exception as exp:
#         print("Exception error", exp.__class__, "occured!")

# print()
# print("The reciprocal of", entry, "is", r)
#  // Resolve for every error same massage (By entering into tuple )
# for entry in random:
#     try:
#         print("The entry is:", entry)
#         r = 1 / int(entry)
#         break
#     except ValueError as value_err:
#         print("Please enter valid value!")
#     except ZeroDivisionError as zero_err:
#         print("Please enter value rather than zero!")
#     else:
#         print("No error")

# print()
# print("The reciprocal of", entry, "is", r)

# try:
#     age = int(input("Age: "))
#     print("Your age is ", age)
#     z = int(age) / 0
# except (ValueError, ZeroDivisionError):
#     print("Please enter a valid age!")
# else:
#     print("No errors found.")
# //////// Finally Method /////////////////
# try:
#     note = open("inde.html")
#     age = int(input("Age: "))
#     x = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("Please enter the valid age!")
# except FileNotFoundError:
#     print("File is not in the directory.")
# else:
#     print("No errors were found!")
# finally:
# note.close()
# ////////// With Statement /////////////////

# try:
#     with open("index.html") as note, open("script.js") as my_note:
#         print("notes opened")

#     age = int(input("Age: "))
#     x = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("Please enter the valid age!")
# except FileNotFoundError:
#     print("File is not in the directory.")
# else:
#     print("No errors were found!")
#     print("closing note....")
# finally:
#     print("notes closed!")
#     note.close()
#     my_note.close()

# ///////// Raising an Error //////////


# def calculate_age(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero or less than zero, try again")

#     return age


# # calculate_age(0)
# try:
#     #    age = calculate_age(5)
#     age = calculate_age(0)
#     print(age)
# except ValueError as error:
#     print(error)
# /////// Bad side of raising error //////////////
# from timeit import timeit

# test_1 = """
# def calculate_age(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero or less than zero, try again")

#     return age


# try:
#     age = calculate_age(0)
#     print(age)
# except ValueError as error:
#     # print(error)
#     pass

# """

# print("Test 01:", timeit(test_1, number=10000))

# test_2 = """
# def calculate_age(age):
#     if age <= 0:
#         return None;
#     return age

# age = calculate_age(0)
# if (age == None):
#     pass

# """

# print("Test 02:", timeit(test_2, number=10000))
# //////// Object Oriented Programming (Class) ////////


# class Robot:
#     project_name = "Area 51"  # Class Attribute

#     def __init__(self, x, y):  # constructor function
#         self.x = x  # self is this keyword in JS
#         self.y = y

#     def walk(
#         self,
#     ):
#         print(f"Project {self.project_name} robot coordinate is ({self.x},{ self.y})")


# robot_1 = Robot(2.1, 5.9)
# robot_2 = Robot(15.1, 66.9)
# # print(robot_1)
# print(robot_1.x)
# print(robot_1.y)
# robot_1.walk()
# # Instance Attribute
# robot_2.z = 13

# # print(robot_1.z)
# # Only available for that particular instance

# # Class Attribute
# print(robot_1.project_name)
# print(robot_2.project_name)
# class attribute is accesible to every instances

# //////// Instance Method and Class Methods ////////
# class Robot:
#     project_name = "Area 51"  # Class Attribute

#     def __init__(self, x, y):  # constructor function
#         self.x = x  # self is this keyword in JS
#         self.y = y

#     # Class Method (use decorator)
#     @classmethod
#     def specific_cordinates(cls):
#         return cls(555, 666)

#     def walk(
#         self,
#     ):
#         print(f"Project {self.project_name} robot coordinate is ({self.x},{ self.y})")


# robot_1 = Robot(2.1, 5.9)
# robot_2 = Robot(15.1, 66.9)
# # robot_1.walk()  # This is instance methods
# robot_special = Robot.specific_cordinates()
# robot_special.walk()
# print(robot_special)
# ////// Magic Methods ////////////////
# class Robot:
#     project_name = "Area 51"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # Magic Methods
#     # __str__ magic method must return an string type

#     def __str__(self):
#         return f"This is a magic method with cordinate of {self.x},{self.y}"

#     def walk(
#         self,
#     ):
#         print(f"Project {self.project_name} robot coordinate is ({self.x},{ self.y})")


# robot_1 = Robot(2.1, 5.9)
# robot_2 = Robot(15.1, 66.9)

# # print(robot_1.__str__())
# robot_1.__str__()
# print(str(robot_1))

# Comparing two instances with magic methods
# class Robot:
#     project_name = "Area 51"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # Magic Methods
#     # __str__ magic method must return an string type
#     def __str__(self):
#         return f"This is a magic method with cordinate of {self.x},{self.y}"

#     #  For Comparing (Equality)
#     def __eq__(self, object_other):
#         return self.x == object_other.x and self.y == object_other.y

#     #  For Comparing (Greater than)
#     def __gt__(self, other_obj):
#         return self.x > other_obj.x and self.y > other_obj.y

#     #  For Comparing (Less than)
#     def __lt__(self, other_obj):
#         return self.x < other_obj.x and self.y < other_obj.y

#     def walk(
#         self,
#     ):
#         print(f"Project {self.project_name} robot coordinate is ({self.x},{ self.y})")


# # robot_1 = Robot(15.1, 66.9)
# # robot_2 = Robot(15.1, 66.9)
# # robot_1 = Robot(2, 4)
# # robot_2 = Robot(1, 2)
# robot_2 = Robot(2, 4)
# robot_1 = Robot(1, 2)

# print(robot_1.__str__())
# robot_1.__str__()
# # print(str(robot_1))
# print(robot_1 == robot_2)
# print(robot_1 > robot_2)
# print(robot_1 < robot_2)
# print(robot_1 <= robot_2) # Not supported (only one comparison is possible)
# ////////  Arithmetic Operations with Magic Methods


# class Robot:
#     project_name = "Area 51"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # Magic Methods

#     def __str__(self):
#         return f"This is a magic method with cordinate of {self.x},{self.y}"

#     #  For Comparing (Equality)
#     def __eq__(self, object_other):
#         return self.x == object_other.x and self.y == object_other.y

#     #  For Comparing (Greater than)
#     def __gt__(self, other_obj):
#         return self.x > other_obj.x and self.y > other_obj.y

#     #  For Comparing (Less than)
#     def __lt__(self, other_obj):
#         return self.x < other_obj.x and self.y < other_obj.y

#     # Arithmatic Magic Method (add)
#     def __add__(self, other_obj):
#         return f"New cordinates are ({self.x + other_obj.x} , {self.y + other_obj.y})"

#     # Arithmatic Magic Method (floor divide )
#     def __floordiv__(self, other_obj):
#         return f"New cordinates are ({self.x // other_obj.x} , {self.y // other_obj.y})"

#     def walk(
#         self,
#     ):
#         print(f"Project {self.project_name} robot coordinate is ({self.x},{ self.y})")


# # robot_1 = Robot(15.1, 66.9)
# # robot_2 = Robot(15.1, 66.9)
# # robot_1 = Robot(2, 4)
# # robot_2 = Robot(1, 2)
# robot_1 = Robot(6, 8.2)
# robot_2 = Robot(2.1, 4.5)
# print(robot_2 + robot_1)
# print(robot_1 // robot_2)
# //////////// Building Container ////////////


# class BookmarkedPage:
#     def __init__(self):
#         self.__bookmarks = {}

#     def add(self, bookmark):
#         self.__bookmarks[bookmark.lower()] = self.__bookmarks.get(bookmark.lower(), 0) + 1

#     def __getitem__(self, bookmark):
#         return self.__bookmarks.get(bookmark.lower(), 0)

#     def __setitem__(self, bookmark, count):
#         self.__bookmarks[bookmark] = count

#     def __len__(self):
#         return len(self.__bookmarks)

#     def __iter__(self):
#         return iter(self.__bookmarks)


# target_bookmark = BookmarkedPage()
# target_bookmark.add("javascript")
# target_bookmark.add("javascript")
# target_bookmark.add("JavaScript")
# target_bookmark.add("javascript")
# target_bookmark.add("javascript")
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("pYthon")
# target_bookmark.add("React")
# target_bookmark.add("React")
# target_bookmark.add("Typescript")
# target_bookmark.add("typescript")
# target_bookmark.add("Ruby")

# print(target_bookmark.bookmarks)
# print(target_bookmark["javascript"])
# print(target_bookmark["PYTHON"])
# # target_bookmark["python"] = 100
# print(target_bookmark.bookmarks)
# print(len(target_bookmark))
# Iteration
# for bookmark in target_bookmark:
#     print(bookmark)
# ///////// Making private members //////
# use __ to make an attribute private
# for example
# print(target_bookmark["PYTHON"])
# print(target_bookmark.bookmarks['PYTHON'])
# print(target_bookmark.bookmarks["python"])
# If you want to not access bookmarks from outside.Just add __
# print(target_bookmark.bookmarks["python"])
# print(target_bookmark.__bookmarks["python"]) # Not Available anymore
# ///////// ACCESS PRIVATE ATTRIBUTES
# print(target_bookmark.__dict__)
# print(target_bookmark._BookmarkedPage__bookmarks)
# /////////// Class Property and Property Decorators /////
# class MovieRating:
#     def __init__(self, rating):
#         # self.rating = rating
#         self.set_rating(rating)

#     def get_rating(self):
#         return self.__rating

#     def set_rating(self, value):
#         if value < 0:
#             raise ValueError("Movie ratings cannot be zero")
#         self.__rating = value

# movie_rating = MovieRating(8)

# print(movie_rating.get_rating())
# class MovieRating:
#     def __init__(self, rating):
#         self.set_rating(rating)

#     def get_rating(self):
#         return self.__rating

#     def set_rating(self, value):
#         if value < 0:
#             raise ValueError("Movie ratings cannot be zero")
#         self.__rating = value
#     # Class Property
#     rating = property(get_rating, set_rating)


# movie_rating = MovieRating(8)

# print(movie_rating.get_rating())
# print(movie_rating.rating)
# ////////// Property Decorator
# class MovieRating:
#     def __init__(self, rating):
#         self.rating = rating

#     @property
#     def rating(self):
#         return self.__rating

#     @rating.setter
#     def rating(self, value):
#         if value < 0:
#             raise ValueError("Movie ratings cannot be zero")
#         self.__rating = value


# movie_rating = MovieRating(8)

# print(movie_rating.rating)
# //////// Class Inheritance ////////////////
# class Person:
#     def __init__(self):
#         self.employed = True

#     def sing(self, name):
#         print(f"{name.capitalize()} is singing")


# class Jay(Person):
#     person_name = "jay"

#     def walk(self):
#         print("Jay is walking....")


# class Jane(Person):
#     person_name = "jane"

#     def fuck(self):
#         print("Jane is fucking....")


# jay_person = Jay()
# jane_person = Jane()
# jay_person.sing(jay_person.person_name)
# jay_person.walk()
# jane_person.sing(jane_person.person_name)
# jane_person.employed
# ///////// Object Class ///////////////

# print(isinstance(jane_person, Person))
# print(isinstance(jane_person, Jane))
# print(isinstance(jane_person, Jay))
# print(issubclass(Jay, Jay))
# print(issubclass(Jay, Person))
# print(issubclass(Jay, object))

# object_person = object()
# print(isinstance(object_person, object))
# print(issubclass(Person, object))

# ///////// Method Overriding ///////////
# class Person:
#     def __init__(self):
#         self.employed = True
#         print("Person Class")

#     def sing(self, name):
#         print(f"{name.capitalize()} is singing")


# class Jay(Person):
#     person_name = "jay"

#     def __init__(self):
#         # super().__init__()
#         self.rich = False
#         print("Jay Class")
#         super().__init__()  # to call this first (Person class __init__ later)

#     def walk(self):
#         print("Jay is walking....")


# class Jane(Person):
#     person_name = "jane"

#     def fuck(self):
#         print("Jane is fucking....")


# jay_person = Jay()
# jane_person = Jane()
# print(jay_person.employed)  # No Attribute showing because of super is missing (method overrided)
# ////////// Multiple Inheritence ///////////////
# class Person:
#     def sports_activity(self):
#         print('swimming')

# class Jay:
#     def sports_activity(self):
#         print('jogging')

# # class Jane(Person, Jay):
# class Jane(Jay, Person):
#     pass

# jane = Jane()
# jane.sports_activity() #swimming will show if (person, jay), jogging will show if (jay, person)
# For multi Inheritance that was a bad example


# class Person:
#     def swimming(self):
#         print("swimming")


# class Jay:
#     def jogging(self):
#         print("jogging")


# # class Jane(Person, Jay):
# class Jane(Jay, Person):
#     pass


# jane = Jane()
# jane.swimming()
# jane.jogging()  # Provide the better name...


# /////// Data Classes ////////////
# from collections import namedtuple

# Robot = namedtuple("Robot", ['x', 'y'])
# robot_1 = Robot(1,2)
# robot_2 = Robot(1,2)
# print(robot_1 == robot_2)
# Implement the magic methods (e.g __eq__) under the hood..

# ////////// Iterators //////////////////
# __iter()__ and __next()__ magic method
# numbers = [1, 2, 3, 4, 5]

# print(type(numbers))
# first_iterator = iter(numbers)
# print(type(first_iterator))
# print(next(first_iterator))
# print(next(first_iterator))
# print(next(first_iterator))
# print(next(first_iterator))
# print(next(first_iterator))
# print(next(first_iterator))
# ///////////// For Loop ////////////////
# A iterator can be iterated only one time so until commenting the next functions this will not run
# for number in first_iterator:
#     print(f'num : {number}')

# for number in numbers:
#     print(f'number: {number}')

# ///// For loop under the Hood //////////////

# for loop under the hood is while infinite loop
# numbers = [1, 2, 3, 4, 5]

# first_iterator = iter(numbers)

# # for number in first_iterator:
# #     print(number)


# while True:
#     try:
#         print(f"number: {next(first_iterator)}")

#     except StopIteration:
#         break
# //////// Creating a custom iterator //////////
# class NumberPower:
#     def __init__(self, max_value):
#         self.max_value = max_value

#     # Creating the Iterator Object
#     def __iter__(self):
#         self.n = 0
#         return self

#     # Iterate over the created iterator object and generate one value
#     def __next__(self):
#         if self.n <= self.max_value:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration


# #  Creating a object / Instance from the class NumberPower
# number_pow = NumberPower(5)
# #  Creating an Iterable from this object
# iterable_num_pow = iter(number_pow)
# print(next(iterable_num_pow))
# print(next(iterable_num_pow))
# print(next(iterable_num_pow))
# print(next(iterable_num_pow))
# print(next(iterable_num_pow))
# print(next(iterable_num_pow))
# # print(next(iterable_num_pow))
# for i in iterable_num_pow:
#     print(f"num: {i}")
# ///////////////////// Generators in Python //////////


# def first_generator():
#     try:

#         x = 1
#         print("1st iteration")
#         yield x
#         x += 2
#         print("2nd iteration")
#         yield x
#         x += 3
#         print("3rd iteration")
#         yield x
#         x += 4
#         print("4th iteration")
#         yield x
#     except StopIteration:
#         print("start it over")


# first_gen = first_generator()

# print(first_gen)
# print(next(first_gen))
# print(next(first_gen))
# print(next(first_gen))
# print(next(first_gen))
# # print(next(first_gen))
# numbers = [1, 2, 3, 45, 6]

# squr_numbers_LC = [x ** 2 for x in numbers if x > 3]
# print(squr_numbers_LC)
# squr_numbers_GE = (x ** 0.5 for x in numbers)
# print(squr_numbers_GE)
# print(next(squr_numbers_GE))
# print(next(squr_numbers_GE))
# print(next(squr_numbers_GE))
# print(next(squr_numbers_GE))
# print(next(squr_numbers_GE))
# # print(next(squr_numbers_GE))
# # ///////// Generation Expression as Function Argument //////////////

# print(max(x ** 4 for x in numbers))
# print(sum(x ** 4 for x in numbers))
# print(min(x ** 4 for x in numbers))

# ///////// Generator Expresssions Advantages //////////

# Memory Efficient
# Ease of Implementation
# Representing Infinite Stream
# Pipelining Generators


# def number_power(maxi_num):
#     n = 0
#     while n <= maxi_num:
#         yield 2 ** n
#         n += 1


# result = number_power(10)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))


#  ----> Fibonacci Number Series ---------> //////////
# 0,1,1,2,4,8,16,32,55
# def fibonacci_number(num):
#     x, y = 0, 1
#     for _ in range(num):
#         x, y = y, x + y
#         yield x


# result_fib = fibonacci_number(10)

# print(next(result_fib))
# print(next(result_fib))
# print(next(result_fib))
# print(next(result_fib))
# print(next(result_fib))
# print(next(result_fib))
# print(next(result_fib))
# print(next(result_fib))
# print(next(result_fib))
# print(next(result_fib))
# print(next(result_fib))


# def square(num):
#     for n in num:
#         yield n ** 2


# result_fib_sqr = square(result_fib)
# print(next(result_fib_sqr))
# print(next(result_fib_sqr))
# print(next(result_fib_sqr))
# print(next(result_fib_sqr))
# print(next(result_fib_sqr))
# print(next(result_fib_sqr))
# print(next(result_fib_sqr))
# print(next(result_fib_sqr))
# print(next(result_fib_sqr))
# /////////// Closure ///////////////////////


# def person(address):
#     def john():
#         print(address)

#     return john


# # print(person("USA"))
# # print(person("USA")())

# address_person = person("USA")

# address_person()
# del person
# # print(person)
# # But still we can access address because of closure
# address_person()
# ///////// When to use closures /////////////////////
# def numbers(n):
#     def multiply_with(x):
#         return x * n

#     return multiply_with


# three = numbers(3)
# print(three(10))

# string_number = numbers("thirty")
# print(string_number(2))
# print(three.__closure__)
# print(three.__closure__[0].cell_contents)
# print(string_number.__closure__[0].cell_contents)
# //////// Decorations Prerequisites //////////////////
# # Function with different names


# def one(name):
#     print(name.capitalize())


# one("iqbal")

# two = one
# two("habib")

# # Higher order functions#
# def name_print(name):
#     print(f"My name is {name.title()}")


# def higher_order(func, name):
#     return func(name)


# higher_order(name_print, "iqbal khandakar")

# # A functions returning another functions
# def func_return():
#     def increment():
#         print("Hi how are you?")

#     return increment


# func_return()()
# /////// Decorators //////////////////


# def operation(func):
#     def increment():
#         print('what up')
#         func()
#         print('hi darling')

#     return increment

# def decrement():
#     print(f'boom')

# # operation(decrement)()

# decorated_func = operation(decrement)
# decorated_func()
# // Synthetic suger in decorators /////
# def operation(func):
#     def increment():
#         print("what up")
#         func()
#         print("hi darling")

#     return increment


# @operation
# def decrement():
#     print(f"boom")


# decrement()
