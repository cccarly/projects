## mutable with order, allow duplicate
## mutable will have remove, pop, append method 
## sorted and slices request new list
##[::-1] of reversing request new list
## accessing request new list

### reverse

mylist = ['banana','cherry','apply',5,1]
mylist2 = [3,2,7,3,9,11,2,7,8,40,99]
print(mylist)

## l1 didn't store value if l1 = mylist2.reverse doesn't work
mylist2.reverse()
print(mylist2)

#### [::-1] reverse request new list 
print(mylist[::-1])


## copy
mylist2.copy()
print(mylist2)

## extend - add another list to the end or simply use + between multiple list
mylist2.extend(mylist)
print(mylist2)


## index - return the position of the first occurrence of value x in the list
print(mylist2.index('banana'))

############# inserting #############
## insert(i,x) - inserts element x at position i in the list
mylist2.insert(5,"insert")
print(mylist2)

## append(x) - inserts element x at position i in the list
mylist2.append("insert2")
print(mylist2)

############# removing #############
## pop() removes and returns the final element of the list
mylist2.pop()
print(mylist2)

## remove(x) removes and returns the first occurrence of element x in the list
mylist2.remove('insert')
mylist2.remove('banana')
mylist2.remove('cherry')
mylist2.remove('apply')
print(mylist2)

## clearn() : removes an item from the list

############## removing #############

## sort(reverse=True|False,key=myFunc) - sorts the elements in the list in ascending order
mylist2.sort()
print(mylist2)
## sort with key and get first position of each key
mylist2.sort(key=lambda x: str(x)[0])
print(mylist2)
## sort a list of dictionaries based on the "year" value of the dictionaries:

def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)

def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)

### sorted() to get a new list and leave original unaffected

new_list = sorted(mylist2)
print('-----new list sorted-----\n' ,
      new_list)

### accessing 
x = mylist2[0]
print('-----accessing-----\n' ,
      x)

### change
mylist2[0] = "change"
print('-----change-----\n' ,
      mylist2)

### slicing - save new list with [::i]
#### same as np.arrange(), select every other (2),3- (2 between)

print('-----slicing1-----\n' ,
    mylist2[::2])


### [::i] in string to reverse string
my_list = ["banana", "cherry", "apple"]
### list comprehension
new_one = [x[::-1] for x in sorted(my_list)]

print('-----slicing2-----\n' ,
    new_one)

###slicing and save new one [:i] get elements before position i

print('-----slicing3-----\n' ,
    mylist2[:3])

### replicate elements

list_with_zeros = [0] * 5
print('-----replicate-----\n' ,list_with_zeros)

### list comprehension with condition

special_squares = [ x**2 for x in range(10) if x**2 > 5 and x**2 < 50 ]

print('-----list comprehension with condition-----\n' ,special_squares)

### list comprehension with nested loop
coords = [ (x,y) for x in range(5) for y in range(3) ]

print('-----list comprehension with nested loop-----\n' ,coords)