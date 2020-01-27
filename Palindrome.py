## REVERSING STRINGS IN PYTHON
## Write a program that takes in a word and says
## whether or not it is a palindrome.
## (A palindrome is a word that is the same
## backwards as forwards like noon and radar


print("Checking for Palindromes using Python\n")

prompt = "***** Please input a word *****\n"
word = input(prompt)
if word[::-1] == str(word):
    print (str(word) + " is a palindrome" )
else:
    print ("sorry. no palindrome")
