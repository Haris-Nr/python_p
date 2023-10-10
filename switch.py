import os
import pprint
os.system('python --version')

a = 9

match a:
    # if a is 7
    case 0:
        print("a is zero")
        
        




spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

print(list(spam.keys()))

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)

spam = {'adse':['asfsa','safda',",asfsadf"],
        "adfe":"safas",
        "wer":23
        }
pprint.pprint(spam)
print(pprint.pformat(spam))