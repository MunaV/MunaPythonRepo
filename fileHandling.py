#file handling in python

#print("writing and reading  file in Python. this will write values to file and read them \n")


def inputNumbers(howMany):

    list = []

    for i in range(1, howMany + 1):
        prompt = '{}/{} Please enter a number: '.format(i, howMany)
        list.append(input(prompt))

    return list

def writeToFile(list, filename):

    file = open(filename, "w")

    for item in list:
        file.write(item + "\n")

    file.close()

def printContentsOfFile(filename):

    file = open(filename, "r")
    contents = file.read()
    print ("Contents of {}:\n\n{}".format(str(filename), str(contents)))



filename = "Numbers"
list = inputNumbers(4)
writeToFile(list, filename)
printContentsOfFile(filename)