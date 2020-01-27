## MunaVenning Jan 2020
## Calculator in Python


def getNumberFromStandardInput(prompt):

    valid = False
    while not valid:
        userInput = input(prompt)
        try:
            return int(userInput)
        except ValueError:
            print('Actually, {} is not a number!'.format(userInput))



a = getNumberFromStandardInput("Enter first number ")
b = getNumberFromStandardInput("Enter second number ")
operator = input("Enter an operator - + * ** or / ")
result = 0

if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    result = a / b
elif operator == '**':
    result = pow(int(a), int(b))

print ('{} {} {} = {}'.format(a, operator, b, result))
