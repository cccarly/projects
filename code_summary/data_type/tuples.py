### ordered & immutable, allows duplicate elements
### a collection of objects (any types, list, dict,string)
###In Python tuples are written with round brackets and comma separated values.

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