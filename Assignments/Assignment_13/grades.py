##########################################################################################################################

##
## CSC 101 Lab week 15
## Program : Unit Testing
## Name : Vishista Vuppulapati
## Email : vvd94@umsystem.edu

## Problem : To test functions using test modules.

## Algorithm

def total(t): # this is a function defined to calculate the sum of all the elemnts in the list.
    sum =0
    for i in t:
        sum+=i
    return sum

def average(a) : # this is a function defined to calculate the average of all the elements in the list.
    sum = 0
    if len(a)!= 0:
        for t in a:
            sum = sum + t           
        avg = sum / len(a)
        return avg
    else:
       return 0
       
def median(m):  # this is a function defined to calculate the median of the list amongest the elements in the list.
    n = len(m)
    if n % 2 == 0:
        median1 = n[n//2]
        median2 = n[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = n[n//2]
    return median

##########################################################################################################################