# Name : Vishista Vuppulapati
# Week 10 Program : Dictionaries 
# Student ID : 16324243
# UMKC email ID : vvd94@umsystem.edu

# A python program to read file of the Kansas City Crime data. 

##################################################################################### 

import csv

def read_in_file():

  data = []
 
  with open('KCPD_Crime_Data_2019 copy.csv',encoding='utf-8') as file:
    file_csv = csv.reader(file)
    for line in file_csv:
      data.append(line)
  return data 

number = int()

def month_from_number(number):
  months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
  try:
    if number<13 and 0<number:
      return months[number]
  except ValueError:
    print("Month must be 1-12")
month_from_number(number)

data =[]

def create_reported_date_dict(data):
  list = {}
  while(True):
    for i in data[1:]:
     key = i[1]
     list[key]=list.get(key,0)+1
    break
  return (list)

create_reported_date_dict(data)

name =[]
def create_dict_column(data,name):
    diction = {}
    val = data[0].index(name)
    while(True):
      for i in data[1:]:
        if i[val]in diction:
            diction[i[val]]+=1
        else:
            diction[i[val]]=1
      break
    return diction
create_dict_column(data,name)

def create_offense_dict(data):
    return create_dict_column(data,"Offense")

create_offense_dict(data)

def create_reported_month_dict(data):
    diction = {}
    for i in data[1:]:
        value = i[1][0:2]
        while(True):
          try:
            if value in diction:
              diction[value]+=1
          except:
            diction[value]=1
    return diction
create_reported_month_dict(data)

def create_offense_by_zip(data):
    diction={}

    for i in data[1:]:
        value = i[7]
        while(True):
          if value in diction:
            diction = diction[value]
            try:
               if i[13] in diction:
                 diction[i[13]]+=1
            except:
                diction[i[13]] = 1
          else:
            diction[value] = {i[13]:1}
    return diction

create_offense_by_zip(data)

##################################################################################### 



