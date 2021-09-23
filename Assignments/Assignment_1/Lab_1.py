########################################################################
##
## CSC 101 Lab
## Program : Grade calculator
## Name : Vishista Vuppulapati
## Email : vvd94@umsystem.edu

## Problem : The main aim is to take in the inputs name,lab grade,exam grade, and the attendence grade 
## and calculate the weighted grade and the overall grade for the particular student.

## Algorithm 

print("\n**** Welcome to the LAB grade calculator! **** \n")
name = input("Who are we calculating grades for? ==> ")
lab_grade = int(input("\nEnter the Labs grade? ==> "))
if lab_grade > 100 :
    lab_grade = 100  ## I'm setting value to 100 if its greater than 100.
    print("The lab value should have been 100 or less.  It has been changed to 100. ")
exam_grade = float(input("\nEnter the EXAMS grade? ==> "))
if exam_grade < 0:
    exam_grade = 0  ## setting the value to 0 if it's less than 0.
    print("The exam value should have been zero or greater.  It has been changed to Zero. ")
attendance_grade = float(input("\nEnter the attendance grade? ==> "))
weighted_grade = float(lab_grade*0.7 + exam_grade*0.2 + attendance_grade*0.1)  ## Logic (calculation )
print("\nThe weighted grade for",name,"is",weighted_grade)

## for printing grades, we're defining the ranges for which the accurate grade will be printed according to the Weighted_grade ranges.

if weighted_grade >= 90 and weighted_grade <= 100:
    print(name,"has a letter grade of A")
elif weighted_grade >=80 and weighted_grade <= 90:
    print(name,"has a letter grade of B")
elif weighted_grade >=70 and weighted_grade <= 80:
    print(name,"has a letter grade of C")
elif weighted_grade >=60 and weighted_grade <=70 :
    print(name,"has a letter grade of D")
elif weighted_grade >=0 and weighted_grade <= 60:
    print(name,"has a letter grade of F")
print("\n**** Thanks for using the Lab grade calculator **** ")
##
########################################################################