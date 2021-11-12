##########################################################################################################################

##
## CSC 101 Lab week 12
## Program : Word Count
## Name : Vishista Vuppulapati
## Email : vvd94@umsystem.edu

## Problem : A program to calculate how many words are there in the data provided.

## Algorithm


def open_file(filename): # Defined a function to open the txt files .
    try:
        open(filename, "r")
        return 1
    except IOError:
        print("Could not open file"+filename)
        return 0

def removePunctuation(text): # this fumction is defined to remove the unwanted punctuations, and replace it by space
    Punctuation = '!.,'
    for i in text:
        if i in Punctuation:
            text = text.replace(i,"") # replacing values of !,. with gaps.(empty)
    return text # we are returning value

def main(): # this is where the all the above function are called 
    
    while True:
        filename = input("Enter the name of the file to open ") # asking the user to input the file name
        if open_file(filename):
            file = open(filename, "r") # this is for opening and reading the file
            break
        else:
            print("Please Try again")
            print()

    diction = {}
    for line in file:
        words = line.strip().lower().split(" ")
        for word in words:
            while(True):
               word = removePunctuation(word)
               if len(word) > 3:
                   if word not in diction:
                       diction[word] = 1
                   else:
                       diction[word] = diction[word]+1
               break

        sorted_dictionary = dict( sorted(diction.items()))

    count = 0
    for i in diction:
        if diction[i] == 1:
            count += 1
    index = 1
    print()
    print("Most frequently used words")
    print(" #          Word            Freq.")
    print("================================")
    for i in sorted_dictionary:
        print("{:>2}{:>15}{:>15}".format(index,i,sorted_dictionary[i]))

        index += 1
        if index >= 10:
            break
    print()
    print("There are " + str(count) + " words that occur only once")
    print("There are " + str(len(diction)) + " unique words in the document")  
main()

##########################################################################################################################