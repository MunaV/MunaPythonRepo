## MunaVenning Jan 2020

## User's favourite Menu in Python
##Write a program that allows user to
##enter his favourite starter, main
##course, dessert and drink.
##Output a message which says ––“Your
##favourite meal is ………with a glass
##of….”


#Prompts user for favourite starter, main course, dessert and drink

print("\nWelcome to your favourite meal\n")
starter = input("Your favourite starter please? ")
mainCourse = input("Your favourite main course please? ")
dessert = input("Your favourite dessert please? ")
drink = input("Your favourite drink please? ")

#Display user's favourite meal
print("\nThank You\n"
      "Your favourite meal consists of {} as a starter "
      "followed by {} as a main course "
      "and a {} for dessert.\n"
      "All with a glass of {} of course! Bon appetite!!".format(starter, mainCourse, dessert, drink))


