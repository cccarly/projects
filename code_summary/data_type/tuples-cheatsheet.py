### ordered & immutable, allows duplicate elements
### a collection of objects (any types, list, dict,string)
### insert, change is unable 
###In Python tuples are written with round brackets and comma separated values.
### good for large data

my_tuple = ("Max", 28, "New York")

""" Reasons to use a tuple over a list
1. Generally used for objects that belong together.
2. Use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.
3. Since tuple are immutable, iterating through tuple is slightly faster than with list.
4. Tuples with their immutable elements can be used as key for a dictionary. This is not possible with lists.
5. If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected. """

## tuple = ("max") --> type = str
## tuple - ("max",) --> type = tuple

my_tuple2 = ("Max")
print('----type-----\n',type(my_tuple2))

#### accessing 
print('----accessing-----\n',my_tuple[0])

#### insert, change - impossible
try:
    my_tuple[2] = "Boston"
except TypeError:
    print('-------change is impossible-----------')
else:
    print('immutable')
finally:
    print('done')

#### delete
del my_tuple2

#### iterating & check existing 
if "New York" in my_tuple:
    print("-----yes---------")
else:
    print("------no------")

my_tuple3 = ('a','p','p','l','e',)

# len() : get the number of elements in a tuple
print('----len()-----\n',len(my_tuple3))

# count(x) : Return the number of items that is equal to x
print('----count()-----\n',my_tuple3.count('p'))

# index(x) : Return index of first item that is equal to x
print('----index()-----\n',my_tuple3.index('l'))

# repetition
my_tuple3 = ('a', 'b') * 5
print('----repetition-----\n',my_tuple3)

# concatenation
my_tuple3 = (1,2,3) + (4,5,6)
print('----add extra tuples together-----\n',my_tuple3)

# convert list to a tuple and vice versa
my_list = ['a', 'b', 'c', 'd']
list_to_tuple = tuple(my_list)
print('----list to tuples-----\n',list_to_tuple)

tuple_to_list = list(list_to_tuple)
print('----tuple to list-----\n',tuple_to_list)

# convert string to tuple (each will have one position)
string_to_tuple = tuple('Hello')
print('----string to tuple-----\n',string_to_tuple)

### slicing [n:i], [::i],[::-1]
### list has reverse function, but tuples only relying on [::-1]
print('----slicing example with reverse------')
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
b = a[::2] # start to end with every second item
print(b)
b = a[::-1] # reverse tuple
print(b)

print('-----slicing example end-------')

#### unpack tuple (doesn have in list )
##### unpack will return value to its specific data type

print('------unpack starts here---------')
name, age, city = my_tuple
print(name)
print(age)
print(city)

# tip: unpack multiple elements to a list with *
my_tuple = (0, 1, 2, 3, 4, 5)
item_first, *items_between, item_last = my_tuple
print(item_first)
print(items_between)
print(item_last)

print('------unpack ends here---------')
#### nested tuples avaiable and can loop 

#### iteration available 

#### compare tuples and list - more effective - good for large data 
#### due to immutability of tuples

import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# compare the execution time of a list vs. tuple creation statement
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

x = (1,2,3,100,4)
print(type(x))
### sorted tuple will turn it to list
print(type(sorted(x)))