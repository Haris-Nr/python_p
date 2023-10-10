catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames)+1) +' ( or Enter nothing to stop.):')
    name = input()
    if name == '':
        print("Total cats you enter" + str(len(catNames)))
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)