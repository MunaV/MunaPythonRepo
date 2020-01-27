## MunaVenning Jan 2020
## Joke punchline prompter in colours

## Challenge 1
## Write a program that will display a joke
## Don’t display the punchline until the reader
## hits the enter key.
## Extension
## display the punchline in a different colour
## Prior Knowledge Needed
## How to output information to the screen


prompt = input("\nknock knock who is there?")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    JOKE = '\033[78m'

#To use code like this, you can do something like

#print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
#or, with Python3.6+:


#print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

print(f"{bcolors.OKGREEN}it's a knock-knock joke!!{bcolors.ENDC}")

print(f"{bcolors.JOKE}it's a knock-knock joke!!{bcolors.ENDC}")



var = '\033[1m' + 'Hello'
print (var)