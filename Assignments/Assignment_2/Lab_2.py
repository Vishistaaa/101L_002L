########################################################################
##
## CSC 101 Lab week 4
## Program : Flarsheim Guesser
## Name : Vishista Vuppulapati
## Email : vvd94@umsystem.edu

## Problem : The main aim is to ask the user to guess the any number in their head and to write a program by using divisiblity rules of 3,5,7, to figure out 
## what that number is.

## Algorithm

print("Welcome to the Flarsheim Gusser!\n")
while(True):
    print("Please think of a number between and including 1 and 100.\n")
    # to access 3 5 or 7
    values="357"
    # to store remainders
    result=[]
    for i in values:
        while(True):
            print("What is the remainder when your number is divide by ",i,"? ",end="")
            r=int(input())
            if(r<0):
                print("The value entered must be 0 or greater") # warning the user to enter a value in range
                continue
            elif(r>=int(i)):
                print("The value entered must be less than ",i)
                continue
            else:
                if(i!='7'):
                    print()
                result.append(r)
                break
    # The values range from 1 - 100 only
    for val in range(1,101):
        if(val%3 == result[0] and val%5 == result[1] and val%7 == result[2]):
            print("Your number was ",str(val))
            print("How amazing is that?\n")
            break

    # Asking the user to choose a choice if whether they wanna play the game again.
    choice=''
    while(True):
        print("Do you want to play the game again?Y to continue,N to quit ==> ",end="")
        choice=input()
        if(choice=='n' or choice=='N' or choice=='y' or choice=='y'):
            break
        else:
            continue
        
    if(choice=='n' or choice=='N'):
        break
    elif(choice=='y' or choice=='Y'):
        continue
    print()
########################################################################