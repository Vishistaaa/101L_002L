########################################################################
##
## CSC 101 Lab week 13
## Program : Classes (Clock)
## Name : Vishista Vuppulapati
## Email : vvd94@umsystem.edu

## Problem : To write a code to keep create a clock class that can keeptrack of hours, minutes and seconds. 
## Algorithm


import time

class Clock: # Here I'm defining a class called Clock.
    
    def __init__(variable,hours,minutes,seconds,clock_type=0): # Here I'm defining constructor, passing 5 aruguments.

        variable.hours = hours # assigning the value to a variable (where the value will get stored.)
        variable.minutes = minutes
        variable.seconds = seconds
       
        variable.clock_type = clock_type

    def tick(variable): # passing paramter called variable to use it in or for the function we defined named tick.
        variable.seconds += 1 # it will increment seconds by 1 everytime and gets stored in space called "variable".
        while(True):
            if variable.seconds >= 60: # if the seconds are greater than 60 then it will make it 0 and increment the previous value  minutes
                variable.seconds = 0  #  by 1 or if the minutes are greater than 60 it will make it 0, and increment the pervious value
                variable.minutes += 1 # value to 1 i.e hours. The same method applies to hours too.
            if variable.minutes >= 60:
                variable.minutes = 0
                variable.hours += 1
            if variable.hours >= 24:
                variable.hours = 0
            break
   
    def __str__(variable): # __ str__ represents the class objects as a string
        if variable.clock_type == 0:
            return '{:02}:{:02}:{:02}'.format(variable.hours,variable.minutes,variable.seconds) # this is going to format hours,minutes,seconds to 2 decimal values.
                                                                                                
        else:
            Meridians = "am" # this is to define whether if the time is am or pm.
            while(True):
                if variable.hours>=12: # if the value is greater than or equal to 12 then its going to change the meridian from am to pm.
                    Meridians = "pm"  
                hours_1 = variable.hours
                if variable.hours==0: # if the value is eual to zero it is going to assign 12 to a new variable.
                    hours_1 = 12
                elif variable.hours>12: 
                    hours_1 = variable.hours-12 # here it will substract 12 from the value if the value is greater than 12.
                break

            return '{:02}:{:02}:{:02} {}'.format(hours_1,variable.minutes,variable.seconds,Meridians)

if __name__ == "__main__": # This is the main function to call the other functions written in the program.

    hours=int(input("What is the current hour ==> ")) # this is asking the user to type in the value of what they want to set the current hour as.
    minutes=int(input("What is the current minute ==> ")) # similarly the others too, here it's aking to input minutes.
    seconds=int(input("What is the current second ==> ")) # input the seconds.

    ticking=Clock(hours,minutes,seconds,1) # passing parameters for the class.

    while (True):
        print(ticking) # printing the class which is assigned to a variable named "ticking".
        ticking.tick() # calling the function 
        time.sleep(1)

########################################################################









