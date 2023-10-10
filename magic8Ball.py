import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2 :
        return 'yes'
    elif answerNumber == 3 :
        return 'Reply hazy try again'
    elif answerNumber == 4 :
        return 'Ask again later'
    elif answerNumber == 5 :
        return 'Concentrate and ask again.'
    elif answerNumber == 6 :
        return 'Don\'t count on it. Ask again later!'
    elif answerNumber == 7 :
        return 'My reply is no'
    elif answerNumber == 8 :
        return 'Outlook not so good'
    elif answerNumber == 9 :
        return 'Very doubtful'

ranNum = random.randint(1,9)
fortune = getAnswer(ranNum)
print(fortune)


messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']

print(messages[random.randint(0,len(messages)-1)])
print(random.choice(messages))

id('Howdy')