import random

# passwordFile = open('SecretPasswordFile.txt')
# secretPassword = passwordFile.read()
# print ('Enter your password')
# typedPassword = input()
# if typedPassword == secretPassword:
#     print('access granted')
# if typedPassword == '12345':
#     print('that password is written by  an idiot')
# else:
#     print('access denied')

# print('Hello, world!')
# print('What is your name?') # ask for their name
# myName = input()
# print('It is good to meet you, ' + myName)
# print()
# print('The length of your name is: ' + str(len(myName)))
# print()
# print('What is your age?') # ask for their age
# myAge = input()
# print('You will be ' + str(int(myAge) + 1) + ' in a year.')

# print(int(7.8)+1)

# for num in range(0,11):
#     print(num)
# i = 0    
# while i <= 10:
#     print(i)
#     i = i + 1     

print(round(56.943))
# print(abs(-4.8))

# asd = 3
# asd1 = "name"
# asd2 = True
# asd3 = float
# asd4 = list
# print(type(asd))
# print(type(asd1))
# print(type(asd2))
# print(type(asd3))
# print(type(asd4))

#for loop

# for character in asd1:
#     print(character)

# slicing
names = "harisnr"
# print(len(names)
 
   # it works like names[0:len(names)-3] (same work for both side when minus) automatic pyhton put len function it only to show you to how to work
 
# print(names[0:5]) # including 0 but not 5
# print(names[1:5]) # including 1 but not 5
# print(names[:5])
# print(names[5])
# print(names[:])  
print(names[0:-3])  
print(names[-3:-1])


# quick 
# nm = "haris"
# print(nm[-4:-2])

# spam = print('hello')
# print(len)
# print(spam)

# print('Hello')
# print('World')

# print('hello', end=' ')
# print('baby')

# print('cats', 'dogs', 'mice')
# print('cats', 'dogs', 'mice', sep=',')

# bitwise operators

#  & and    
# | or
# ^ xor
# 8 >> 1 # left shift by one position
# 6 << 1 right shift by one postion
# ~ not (compliment)

a = 5 
b = '5'
c = 5

# print( a & b)
# print( a | b)
# print( a ^ b)
# print( ~ a)
# print( ~ b)
# print(a << 2)
# print(a >> 2 )

# print(6 % 2)


# identity operator 

print(a is c)
print(a is not b)

print(id(a))
print(id(b))
print(id(c))

# membership operator in python

strin = 'jerry'
print('y' in strin)
print('y' not in strin)