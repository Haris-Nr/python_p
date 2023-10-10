import time
import random
time.sleep(3)

for i in range(20):
    print("My World")


supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

### enumerate() function
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)



myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input().capitalize()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')


pets = ['Dog', 'Cat', 'Moose']

print(random.choice(pets))

random.shuffle(pets)
print(pets)


def eggs(someParameter):
    someParameter.append('Hello')
spam = [1, 2, 3]
eggs(spam)
print(spam)