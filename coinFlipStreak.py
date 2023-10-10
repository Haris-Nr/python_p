import random
numberOfStreaks = 0
for experimentNumber in range(10000):
# Code that creates a list of 100 'heads' or 'tails' values.
    coins = ["H","T"]
    randomNum = random.randint(0,1)
    coin_filp = [coins[randomNum]]
# Code that checks if there is a streak of 6 heads or tails in a row.
if(coin_filp[0]=="H"):
    print("helo")

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
print(coin_filp)
