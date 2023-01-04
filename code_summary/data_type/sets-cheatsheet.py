#### unordered (not add by sequential)
#### unindexed
#### mutable
#### no duplicate elements
#### created with braces

my_set = {"apple", "banana", "cherry"}
my_set_3 = set("aaabbbcccdddeeeeeffff")
print('---set to keep distinct value-----\n',my_set_3)

# careful: an empty set cannot be created with {}, as this is interpreted as dict
# use set() instead
my_set_3 = set()
print('---empty set-----\n',type(my_set_3))

#### add(x)
my_set.add(1)
my_set.add(2)
my_set.add(3)
print('---add()----\n',my_set)

##### del , clear
# del my_set_3
# my_set_3.clear()

#### remove elements
