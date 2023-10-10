import random
import sys

secreteNumber = random.randint(1, 20)
print("what number I am thinking between 1 to 20, you have 6 guesses")
for guesstaken in range(1, 7):
    print("Guess a number " + str(guesstaken) + " chace")
    guess = int(input())
    if guess < secreteNumber:
        print("your number is less than my number")
    elif guess > secreteNumber:
        print("your number is greater than my number")
    else:
        break
if guess == secreteNumber:
    print("your guess is write. You guess my number in " + str(guesstaken) + " guesses!")
else:
    print('Nope. The number I was thinking of was ' + str(secreteNumber))


print("rock","paper","scissors")
wins=0
losses=0
ties=0
while True: # the main game loop
    print('%s wins, %s losses, %sties' % (wins, losses, ties))
    while True:  # player input loop
        print('Enter your move:(r)ock (p)aper (s)cissors or (q)uite')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # quit the game
        if playerMove == 'r' or playerMove == 's' or playerMove == 'p':
            break
        print("Type one of r, p, s, or q.")
    # display what player choose
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:

    randomNumber = random.randint(1, 3)

    if randomNumber == 1:
        computerMove = 'r'
        print("ROCK")
    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        computerMove = 's'
        print("SCISSORS')")

    # Display and record the win/loss/tie:

    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
