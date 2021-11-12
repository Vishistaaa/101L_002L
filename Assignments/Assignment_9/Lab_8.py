# Name : Vishista Vuppulapati
# Week 10 Program : Dictionaries 
# Student ID : 16324243
# UMKC email ID : vvd94@umsystem.edu

# A python program to read file of the Kansas City Crime data. 

##################################################################################### 

import csv

# defining a function to open and read the csv file.
def read_in_file():

  data = []
 
  with open('KCPD_Crime_Data_2019 copy.csv',encoding='utf-8') as file:
    file_csv = csv.reader(file) # reads the csv file
    for line in file_csv: 
      data.append(line)  #for some line in the file the line is going to get appended into the empty dictionary
  return data 

number = int()

def month_from_number(number):
  months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
  try:
    if number<13 and 0<number: # Beacause there are 12 months, number should be less than 13.
      return months[number]
  except ValueError:
    print("Month must be 1-12") # Throws an error if it's greater than or less than 0.


data =[]

def create_reported_date_dict(data):
  list = {}
  while(True):
    for i in data[1:]: # for some value in the data from the index 1 to end of the data.
     list[i[1]]=list.get(i[1],0)+1  
    break
  return (list) 


name =[]
def create_dict_column(data,name): # passing two variables 
    diction = {}
    val = data[0].index(name) 
    while(True):
      for i in data[1:]: # for some value in the data from the index 1 to end of the data.
        if i[val]in diction:
            diction[i[val]]+=1  # we are incrementing by 1 
        else:
            diction[i[val]]=1 
      break
    return diction # we are returning the dictionary named diction


def create_offense_dict(data):
    return create_dict_column(data,"Offense")

create_offense_dict(data)

def create_reported_month_dict(data):
    diction = {}
    for i in data[1:]:
        value = i[1][0:2] #  the value of how many times a crime occurred on that data as read from the file.
        while(True):
          try:
            if value in diction:
              diction[value]+=1 #incrementing by 1 if the values exists in the dictionary.
          except:
            diction[value]=1
    return diction


def create_offense_by_zip(data):
    diction={}

    for i in data[1:]:
        value = i[7]
        while(True):
          if value in diction:
            diction = diction[value] # if the value is in the dictionary then it is going to return i[7] 
            try:
               if i[13] in diction: 
                 diction[i[13]]+= 1
            except:
                diction[i[13]] = 1
          else:
            diction[value] = {i[13]:1}
    return diction


def main(): # here we're calling the above defined function.
    while(True):
        filename = input("Enter the name of the crime data file ==> ")
        data = read_in_file(filename)
        if(data != filename): 
            print("Could not find the file specified. "+filename+" not found")# it's going to print this if the file entered is not found.
        else:
            break
        report = create_reported_month_dict(data)
    print(report)
    month_from_number(number)
    offense = create_offense_dict(data)
    create_dict_column()
    print("Zip Code                        # Offenses")
    print("==========================================") 
    while(True):
        offense1 = input("Enter an offense : ")
        if offense1 not in offense:
            print("Not a valid offense, please try again")
        else:
            break
    print(offense1+" offense by Zip Code")
    create_offense_by_zip(data)


if __name__ == "__main__":
    main() # calling the main function

##################################################################################### 



