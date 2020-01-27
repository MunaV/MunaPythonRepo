#Create a program that asks the user to
#input a password, re enter the password
#and the tells the user if the password is
#weak, medium or strong.

import re


def promptUserForPasswords():

    passwordsMatch = False
    longEnough = False
    noWhiteSpaces = False
    password =''



    while passwordsMatch == False:

        while longEnough == False or noWhiteSpaces == False:


            #Prompting user for password:

            prompt = '\n***** Please enter an 8 character long password ***** ' \
                     '\n***** with at least one digit *****' \
                     '\n***** at least one uppercase letter *****' \
                     '\n***** at least one lowercase letter *****' \
                     '\n***** and no empty spaces ***** ' \
                     '\n: '
            password = input(prompt)


            #Checking password length

            passwordLength = int(len(password))
            if  passwordLength < 8:
                print(str(passwordLength) + " characters is too short. Please try again.")
            elif passwordLength > 8:
                print(str(passwordLength) + " characters is too long. Please try again.")
            else:
                longEnough = True
                #print('Your password is the right length.')


            #Checking for white spaces:

            NONwhiteSpace = re.findall("\S", password)

            if len(NONwhiteSpace) == len(password):
                noWhiteSpaces = True
                #print("There are no white spaces in this password")
            else:
                print('please remove any empty spaces')



        #verify input by confirming password



        prompt2 = '\n***** Great! Please re-enter your password for confirmation: *****\n : '
        password2 = input(prompt2)

        if password == password2:
            print("your passwords match")
            passwordsMatch = True
            return password
        else:
            print("Your passwords did not match")



def checkPassword(password):

    hasDigits = False
    hasLowerCase =False
    hasCapitals = False
    passwordStrength = 'weak'

    #Check if the string contains any digits (numbers from 0-9):

    digits = re.findall("\d", password)

    #print(digits)

    if (digits):
        print("Yes, there is at least one digit in this password!")
        #print(digits)
        hasDigits = True
    else:
        print("There are no digits in this password!")
        #print(digits)


    #Check if the string has any characters from a to z lower case, and A to Z upper case:

    upperCaseLetters = re.findall('[A-Z]', password)

    #print(upperCaseLetters)

    if (upperCaseLetters):
        print("There is at least one Capital letter in this password!")
        hasCapitals = True
    else:
        print("There are no Capital letters in this password!")


    #Check if the string has any characters from a to z lower case, and A to Z upper case:

    lowerCaseLetters = re.findall('[a-z]', password)

    #print(lowerCaseLetters)

    if (lowerCaseLetters):
        print("There is at least one small letter in this password!")
        hasLowerCase = True
    else:
        print("There are no small letters in this password")


    if hasDigits and hasCapitals and hasLowerCase == True:
        passwordStrength = 'strong'
    elif False == hasCapitals and hasDigits == True:
        passwordStrength = 'medium'

    return passwordStrength



# running the program


password =  str(promptUserForPasswords())

if (password):
    passwordStrength = checkPassword(password)
    print("\nYour password is: {0}".format(str(passwordStrength)))



