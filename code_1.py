import copy

spam = ['a','v','b','f']
spam2 = [['a','v','b','f'],['g','d','4','h']]

cheese2 = copy.deepcopy(spam2)
cheese = copy.copy(spam)

cheese2[1][0] = 32
cheese[1] = 32

print(spam2)
print(cheese2)

print(spam)
print(cheese)