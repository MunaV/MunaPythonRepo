## JOKE GENERATOR IN PYTHON
## Write a program that asks a user for
## their favourite number and then tells
## them a joke. The program will call a
## joke printing function with the users
## favourite number.
## The function will accept one numeric
## parameter and use it to choose the
## joke to tell. You will probably use
## multi_selection if statement to match
## the joke against the number.

def getNumberFromStandardInput():

    valid = False
    while not valid:
        userInput = input("Give me a number and I will give you a joke!")
        try:
            return int(userInput)
        except ValueError:
            print('Actually, {} is not a number!'.format(userInput))


jokeList = ["I’d like to start with the chimney jokes – I’ve got a stack of them. The first one is on the house.",
            "I did a gig in a fertility clinic. I got a standing ovulation.",
            "I had a dream last night that I was cutting carrots with the Grim Reaper - dicing with death.",
            "I rang up British Telecom and said: 'I want to report a nuisance caller.' He said: 'Not you again.'",
            "I saw this bloke chatting-up a cheetah and I thought: 'He’s trying to pull a fast one.'",
            "The advantages of easy origami are two-fold.",
            "I rang up my local swimming baths. I said: 'Is that the local swimming baths?' He said: 'It depends where you’re calling from.'",
            "I said to the gym instructor: 'Can you teach me to do the splits?' He said: 'How flexible are you?' I said: 'I can’t make Tuesdays.'",
            "I’m against hunting. In fact, I’m a hunt saboteur. I go out the night before and shoot the fox.",
            "This policeman came up to me with a pencil and a piece of very thin paper. He said, 'I want you to trace someone for me.'"]



print(jokeList[getNumberFromStandardInput() % len(jokeList)])


