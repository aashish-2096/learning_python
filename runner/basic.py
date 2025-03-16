from itertools import islice
from more_itertools import peekable
from functools import reduce
from functools import partial

## Sun 16 March-2025

## Sorting with keys 
# .sort() makes sorting inplace and original list is modified here 
scores = [5, 7, 4, 6, 9, 8]
scores.sort()
print(scores)

print("After reverse")
scores.sort(reverse=True)
print(scores)


def sort_key(company):
    print("Type Check" + str(type(company[1])))
    return company[0]
    
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

companies.sort(key=sort_key, reverse=True)
print(companies)
companies.sort(key= lambda company: company[2])
print("Second Sort")
print(companies)


## Sorted sorted(), sorts and creates a new list keeping the older list intact
orders = [5, 7, 4, 6, 9, 8]
temp = sorted(orders)
print(orders)
print("Modified")
print(temp)


## Slicing 
## sub_list = list[begin: end: step]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[::2]
last_3_index = colors[-3:]
reverse_with_step = colors[::-2]
print(sub_colors)
print(last_3_index)
print(reverse_with_step) 

## Unpacking 
colors = ['cyan', 'magenta', 'yellow', 'black']
cyan, magenta, *other = colors
print(magenta)
print(other)

## Loops 

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for item in enumerate(cities):
    ## print(type(item)), returns tuple
    print(item[0])
    print(item[1])
    
print("Without Index")
for index, city in enumerate(cities):
    print(f"{index}: {city}")
    
## Only acts as index intializer, doesn't skip first elemet
print("Considering starting Index")
for index, city in enumerate(cities,1):
    print(f"{index}: {city}")
    
print("Enumerate Slicing with starting Index")
for index, city in islice(enumerate(cities), 2, None):
    print(index, city)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

print("Enumerate Slicing with starting Index with stop and step size")
# islice(iterable, start, stop, step)
for index, color in islice(enumerate(colors), 2, 6, 2):  
    print(index, color)
    
# help(islice)
## Index of item in list, required to handle in case element doesn't exist in list
print("Elements Existence in list")
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
city = 'Osaka'

if city in cities:
    result = cities.index(city)
    print(f"The {city} has an index of {result}.")
else:
    print(f"{city} doesn't exist in the list.")
    
print("Check for element if exist in it, rather than throwing exception")   
it = peekable(iter([]))
if it:
    print("Next element exists:", it.peek())  # Peek without consuming
else:
    print("No more elements")
    
    
## Map 
print("Map on a list")   
names = ['david', 'peter', 'jenifer']
new_names = map(lambda name: name.capitalize(), names)
print(list(new_names))

## Filter Usage
print("Filter on a list")   
countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]
populated = filter(lambda c: c[1] > 300000000, countries)
print(list(populated))


## Reduce on list
print("Reduce on a list")   
scores = [75, 65, 80, 95, 50]
total = reduce(lambda a, b: a + b, scores)
print(total)

## List Comprehension 
print("List Comprehension on a list")   
mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]
highest_mountains = list(filter(lambda m: m[1] > 8600, mountains))
print(highest_mountains)



## Dictiionaries 
print("Dictionary get using getmethod, direct refreence throws exception")
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

ssn = person.get('ssn', '000-00-0000')
print(ssn)


print('Looping through dictionary')
for key, value in person.items():
    print(f"{key}: {value}")

print("Key Looping Default behaviour")
for key in person:
    print(f"{key}")
    
print("Value Looping")
for value in person.values():
    print(f"{value}")
    
    
#Dictionary Comprehension 
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 1344
}

selected_stocks = {s: p for (s, p) in stocks.items() if p > 400}
print(selected_stocks)


## Sets
skills = {'Problem solving', 'Software design', 'Python programming'}
if 'Java' in skills:
    skills.remove('Java')
print("Discard doesn't throw error if key is absent")
skills.discard('Java')

print("Making set immutable, frozenset for rescue")
skills = {'Problem solving', 'Software design', 'Python programming'}
skills = frozenset(skills)


tags = {'Django', 'Pandas', 'Numpy'}
new_tags = {tag.lower() for tag in tags if tag != 'Numpy'}
print(new_tags)


## Union method and union operator
print("Only Considers sets")
s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}
s = s1 | s2
print(s)

print("Considers iterables")
rates = {1, 2, 3}
ranks = [2, 3, 4]
ratings = rates.union(ranks)
print(ratings)


print("Interection Considers iterables")
numbers = {1, 2, 3}
scores = [2, 3, 4]
numbers = numbers.intersection(scores)
print(numbers)

print("Only Considers sets")
numbers = {1, 2, 3}
scores = {2, 3, 4}
numbers = numbers & scores
print(numbers)


## Similar is the handling with difference method | difference Operator (-)
## symmetric_difference(), operator (^)

## Exceptions Handling - try...except...else..excuted when no exception then -> finally


## for else statement 
# Use Python for else statement to execute a code block if the loop doesn’t encounter a 
# break statement or if the iterables object has no item

print("for Else Statement")
people = [{'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 22},
        {'name': 'Peter', 'age': 30},
        {'name': 'Jenifer', 'age': 28}]

#name = input('Enter a name:')
name = ""
for person in people:
    if person['name'] == name:
        print(person)
        break
else:
    print(f'{name} not found!')
    
    
## Similar is while else 
print("While Else")
basket = [
    {'fruit': 'apple', 'qty': 20},
    {'fruit': 'banana', 'qty': 30},
    {'fruit': 'orange', 'qty': 10}
]

# fruit = input('Enter a fruit:')
fruit = ""
index = 0
while index < len(basket):
    item = basket[index]
    # check the fruit name
    if item['fruit'] == fruit:
        print(f"The basket has {item['qty']} {item['fruit']}(s)")
        found_it = True
        break

    index += 1
else:
    qty = int(input(f'Enter the qty for {fruit}:'))
    basket.append({'fruit': fruit, 'qty': qty})
    print(basket)

## Tuples Unpacking 
r, g, *other = (192, 210, 100, 0.5)

#Tuple Aggregation
odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)
numbers = (*odd_numbers, *even_numbers)
print(numbers)



#Partial functions
print("Partial Functions")
def multiply(a, b):
    return a*b
x = 2
f = partial(multiply, x)

result = f(10)  # 20
print(result)

x = 3
result = f(10)  # 20
print(result)

print("Type Hints")
from typing import Union

number = Union[int, float]

def add(x: number, y: number) -> number:
    return x + y
print(add(10,11))



## __name__ -> double underscores -> dunder variables 
print(__name__)