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

##### del set , clear(),pop(x)
# del my_set_3
# my_set_3.clear()
# my_set.pop() --**delete random element ** --

#### remove(x) elements
my_set.remove("apple")
print('---remove-----\n',my_set)

#####discard(x) -remove but doesn't throw out keyerror if not exist

my_set.discard("blueberry")
print('---discard -----\n',my_set)

#### iteration & loop available

#### copy() & update(*) - same as dict
##### but keep distinct elements as always

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.update(setB)
print('---update()-----\n',setA)


# intersection_update() : Update the set by keeping only the elements found in both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.intersection_update(setB)
print('---elements in both----\n',setA)

# difference_update() : Update the set by removing elements found in another set.
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.difference_update(setB)
print('---removing elements if in other set----\n',setA)

# symmetric_difference_update() : Update the set by only keeping the elements found in either set, but not in both
### same as symmetric_difference() 
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.symmetric_difference_update(setB)
print('---return A,B but not both----\n',setA)

#subset,superset, and disjoint

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
# issubset(setX): Returns True if setX contains the set
print('---subset1---\n',setA.issubset(setB))
print('---subset2---\n',setB.issubset(setA)) # True

# issuperset(setX): Returns True if the set contains setX
print('---superset1---\n',setA.issuperset(setB)) # True
print('---superset2---\n',setB.issuperset(setA))

# isdisjoint(setX) : Return True if both sets have a null intersection, i.e. no same elements
setC = {7, 8, 9}
print('---disjoint1---\n',setA.isdisjoint(setB))
print('---disjoint2----\n',setA.isdisjoint(setC))

##### NEW SET REQUEST - START FROM HERE #######
#### union() same as update

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7,18}

# union(*set) : combine elements from both sets, no duplication
# note that this does not change the two sets
u = odds.union(evens,primes)
print('------union-----\n',u)

# intersection(): take elements that are in both sets
i = odds.intersection(primes)
print('------intersection-------\n',i)

# difference() : returns a set with all the elements from the setA that are not in setB.
diff_set = setA.difference(setB)
print('-----return difference of two set---\n',diff_set)

# symmetric_difference() : returns a set with all the elements that are in setA and setB but not in both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
diff_set = setA.symmetric_difference(setB)
print('---return A,B but not both----\n',diff_set)

##################frozenset ##################
## immutable version of normal set
## add,remove, discard,clear,update doesn't work
## union, intersection, difference works

odds = frozenset({1, 3, 5, 7, 9})
evens = frozenset({0, 2, 4, 6, 8})
print('---frozenset union----\n',odds.union(evens))
print('----frozenset intersection---\n',odds.intersection(evens))
print('---frozenset difference ----\n',odds.difference(evens))
