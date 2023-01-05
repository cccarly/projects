### sequence of characters
### with doubt or single quote
### ordered,immutable, text representation
## **a string object always represents the same string **



### when string with ' 

x = 'i\'m a prgrammer'
x = "i'm a programmer"
print(x)
# escaping backslash
my_string = 'I\' m  a "Geek"'
my_string = 'I\' m a \'Geek\''
print(my_string)
### triple quotes works too!
### immutable !!!!
### slicing available such as list 
### :: also works, ::-1 tricks also works 
### works with plus concatenate 
i = 'snow'
combine = x + " " + i
print('---concatenate----\n',combine)

### iterator works <for> - check if char inside of string using <if>

### access and substrings 

b = my_string[0]
print('-----position1----\n',b)

b = my_string[:5] # from beginning
print('-----position2----\n',b)

b = my_string[::2] # start to end with every second item
print('---access every other letter ---\n',b)

b = my_string[::-1] # reverse the string with a negative step:
print('---reverse str---\n',b)


###  remove white space 
b = '        hello'
print('---strip---\n',b.strip())
### immutable, the original b doesn't change, assign new value = b.strip() works 
print('---not strip ---\n',b)

### uper and lower

print('---upper() ----\n',my_string.upper())
print('---lower() ----\n',my_string.lower())

## binary true false/ starswith - endswith/ 
print('---startswith---- \n',x.startswith('pr'))

print('----endswith--- \n',x.endswith('mmer'))

## find() search function and find first index of a given substring
## e.g substring = 'euw',return index position is e's position
## return -1 otherwise
print('---find()---\n',x.find('er'))

## count(string) case sensitive
print('---count()---\n',x.count('g'))

## string with replace 
## The original string stays the same
x.replace("programmer","bankser")
print('----replace function ----\n',x.replace("programmer","bankser"))

## split(sep,maxsplit) -> list, split string and turn into list 
a = my_string.split() # default argument is " "
print('----split1 ----\n',a)

a = my_string.split("'")
print('----split sep with single quote----\n',a)

## join element x = '(sep)'.join(list etc.)

my_list = ['How', 'are', 'you', 'doing']
a = ','.join(my_list) # the given string is the separator, e.g. ' ' between each argument
print('----join()----\n',a)

## format 
'''
### .format() with {}
### "%s %d %f %.2f" % val
### f-strings
'''
'''
## effciency tips
# since a string is immutable, adding strings with +,  or += always 
# creates a new string, and therefore is expensive for multiple operations
# --> join method is much faster '''

