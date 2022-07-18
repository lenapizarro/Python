#!/usr/bin/env python3


from cgi import test
from decimal import *
from pickle import TRUE                                        #if we didn't import the decimal library, it would not allow us to be accurate with our results 

a = Decimal('0.10')
b = Decimal('0.30')

x = a + a + a - b
print('x is {}'. format(x))
print(type(x))   #decimal library 

bool_var = True
print(type(bool_var))

var1 = None
print(type(var1))

#lists, tuples and dictionaries
#list 

listA = [1, True, 26, 30, 'Cow']
for i in listA:
        print('i is {}'.format(i))

#tuple

tupleB = (1,2,3,4, True, 'Panda')
for i in tupleB:
    print('i is {}'.format(i))
collectionVar = 'Panda'
if collectionVar in tupleB:
    print('It is a member of the collection')
else:
    print('It is not a member')

#dictionary
var_key, var_value = 0, 0 
dictC = {'one': 1, 'two': 2, 'Hello': 'World'} #structure key:value
for var_key, var_value in dictC.items():
    print('Key is {}, value is {}'.format(var_key, var_value))



#Defining different variables w/ different value types in the same line 

test1, test2, test3 = 0, 'Hello', True
print('test1 is {}, test2 is {}, test3 is {}'. format(test1, test2, test3)) 

#type() and id()

tupleC = (1, 'Hello', 3.0, [4, True], (1,2,3,4))
print(type(tupleC[3]))


#Using keyword is & isinstance

if tupleB[0] is tupleC[0]:
    print('They are identical')
else:
    print('No, they are different')

if isinstance(tupleC, list):
    print('It is')
else:
    print('Nope')


#While + else loops

secretWord = 'Panda'
password = ''
authenticated = False
i = 0
max_attempt = 6

while password != secretWord:
    i += 1
    if i > max_attempt: break
    password = input('{}: What is the secret word? '.format(i))
else: 
    authenticated = True
    print('Authorized' if authenticated else "Breach attempt")   


#for + else loops


cute_animals = ('Panda', 'Guinea Pig', 'Bear', 'Cow', 'Elephant')

for animal in cute_animals:
    if animal == 'Cow': continue #this means it will restart the loop, going back up to the for condition without printing the animal's name
    if animal == 'Elephant': break
    print(animal)
else: 
    print('Thats the complete list of animals')


#using args
def main():
    kitten('meow', 'purr', 'grr')
    seq = range(11)
    seq2 = [ x * 2 for x in seq]
    print_list(seq)
    print_list(seq2)


def kitten(*args):   #the * passes a reference to an object
    if len(args):
        for s in args: 
            print(s)
    else: print ('Sleepy cat')


def print_list(seqs):
	for i in seqs:
		print(i, end= ' ')
   


if __name__ == '__main__' : main()