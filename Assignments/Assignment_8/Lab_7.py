##########################################################################################################################

##
## CSC 101 Lab week 8
## Program : Weighted Grades
## Name : Vishista Vuppulapati
## Email : vvd94@umsystem.edu

## Problem : A program to calculate grades which have a weightage to them, based on the data user provides.

## Algorithm


import math #to use math modules in the code

# defined a function to calculate the average of elements in the list.
def mean(list1):
    total_values = len(list1)
    if list1 == 0:
        return 0
    else:
        sum = 0
        for value in list1:
            sum += value
        return (sum/total_values)
        
#defined a function to calculate standard deviation (using standard deviation formula.
def standard_dev(mean,list1):
    total_values = len(list1)
    sum = 0
    for value in list1:
        sum += math.pow((value - mean),2)
        sum1 = math.sqrt(sum/total_values)
    return sum1

# defined a function to display the table of values containing minimumum value in the list , minimum and maximum values in the list along with the average and the
# standard deviation.
def show_table(test,assignment):
    score = 0
    count_tests = len(test) 
    count_assign = len(assignment)
    print("Type               #       min       max       avg       std") 
    print("===================================================================")
    if count_tests == 0:
        minimum_test,maximum_test,average_test,standard_test = 'n/a','n/a','n/a','n/a'
        print("Tests               0       n/a       n/a       n/a       n/a")
    else :
        if count_tests > 0:
            minimum_test = min(test) 
            maximum_test = max(test) 
            average_test = mean(test) 
            standard_test = standard_dev(average_test,test)
            score += (average_test*0.6) # 0.6 is the weight for the tests in order to calculate the overall grade.
            print("Tests              {}       {:.2f}        {:.2f}        {:.2f}         {:.2f}".format(count_tests,minimum_test,maximum_test,average_test,
            standard_test))

    if count_assign == 0: # if the length of the list is 0 then the nothing can be calculaed.
        minimum_assign,maximum_assign,average_assign,standard_assign = 'n/a','n/a','n/a','n/a'
        print("Program             0       n/a       n/a       n/a       n/a \n")
    else: 
        if count_assign > 0:
            minimum_assign = min(assignment)
            maximum_assign = max(assignment)
            average_assign = mean(assignment)
            standard_assign = standard_dev(average_assign,assignment)
            score += (average_assign*0.4)
            print("Program            {}       {:.2f}        {:.2f}        {:.2f}         {:.2f}".format(count_assign,minimum_assign,maximum_assign,average_assign,
            standard_assign))
    print("The weighted score is",score)


def main():
    tests = [] #empty list
    assignments =[]

    while(1):
        print("\t\tGrade Menu") #options the user can choose from.
        print("1 - Add Test")
        print("2 - Remove Test")
        print("3 - Clear Tests")
        print("4 - Add Assignments")
        print("5 - Remove Assignment")
        print("6 - Clear Assignments")
        print("D - Display Scores")
        print("Q - Quit\n")
        option = input("==> ")
        if option == '1':
            new_test = float(input("\nEnter the new Test score 0-100 ==> "))
            if new_test >= 0 and new_test<= 100:
                tests.append(new_test) # adding the value to the test list if the value satisfices the given condititon.
        elif option == '2':
            Test_remove = float(input("\nEnter the Test to remove 0-100 ==> "))
            try:
                tests.remove(Test_remove)
            except ValueError:
                print("Could not find that score to remove") 
                 
        elif option == '3':
            tests.clear()
        elif option == '4':
            new_assignment = float(input("\nEnter the new Assignment score 0-100 ==> "))
            if new_assignment >= 0 and new_assignment<= 100:
                assignments.append(new_assignment)
        
        elif option == '5':
            Assign_remove = float(input("\nEnter the Assignment to remove 0-100 ==> "))
            try:
                assignments.remove(Assign_remove) # this is removing the value entered by the user if the value is not found in the list.
            except ValueError:
                print("Could not find that score to remove\n") # informing the user that value entered is not found in the list.
        elif option == '6':
            assignments.clear() # this will clear up all the data the user entered.
        elif option == 'D' or option == 'd':
            show_table(tests,assignments)
        elif option == 'Q' or option == 'q':
            break
        else:
            break
main()        


#######################################################################################################################################



       


