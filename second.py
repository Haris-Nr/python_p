name = ''
number = 0
while name != 'your name':
    number = number +1
    print('Please type your name.')
    name = input()
    if(number == 5):
        print("jaa tur jaa ____")
        break
print('Thank you!')

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    break
print('Access granted.')

print('My name is')
for i in range(6):
  print('Jimmy Five Times (' + str(i) + ')')

total = 0
for num in range(1010):
    total = total + num
print(total)


for i in range(5,-1,-1):
    print(i)

import random
for i in range(5):
    print(random.randint(1, 10))

print("hello\nworld")

name = input("what is your name")
print("helo", name )


a = 1
b = 2
c = a
a = b
b = c

print(a)
print(b)


def hello1():
    print("howdy!")
    print("howdy!!")
    print("howdy!!!")


hello1()

def hello(name):
    print ("Howdy " + name,"! ")

hello("haris")


# Strings are immutable

str= "!!haRiS!!!!!!!!"
str2 = "Haris Haris"
print(len(str))
print(str.upper())
print(str.lower())
print(str.rstrip("!")) # only works on end
print(str2.strip)
print(str2.split(" ")) # split the string at the whitespace " ".
print(str2.replace("Haris","Hamza"))

blohHeading = "introduction tO pyThoN"
print(blohHeading.capitalize())

str3 = "welcome to center"
str4 = "welcome to Home to !!"
print(str3.center(50))  #added spaces 
print(str3.center(50,'.'))  #added dotes to check 

print(str2.count("Haris"))
print(str4.endswith("!"))
print(str4.endswith("to",4,10))
print(str4.find("to"))
print(str4.find("too"))
print(str4.index("to"))
# print(str4.index("too"))
str5 = "welcometothepython8"
str7 = "welcometothepython"
str8 = "welcometothepython8"
str6 = "welcometothepython8."
print(str5.isalnum())
print(str6.isalnum())
print(str7.isalpha())
print(str8.isalpha())
print(str8.islower())
print(str8.isprintable())
print(str8.isspace())
print(str7.istitle())

# string method in replit






