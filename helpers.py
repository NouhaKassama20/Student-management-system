# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:07:13 2024

@author: dell
"""
#This module provides functions to read from and write in csv files.
import csv 
import json

#First function: ADD
#IN csv file:
def add_student_to_csv(file_name) :
    #get student information from the user:
    Id=input("Enter student id please:")
    name=input("Enter student name please: ")
    age=input("Enter student age please: ")
    city=input("Enter student city please: ")
    average=input("Enter student average please: ")
    """check if the ifle exist or not,
       if it doesn't exist we create a new one and add to the specified header(Name, Age, City, Average)
    """
    try:
       #this block will be excuted if the file exist, it starts by open the file in read mode: 
       with open(file_name, 'r', newline='') as file:
            #creates reader object:
            reader=csv.reader(file)
            #reads the first row(header) from the file:
            header=next(reader)
    #this block will be excuted if the file dosn't exist        
    except FileNotFoundError:
            #default header:
            header=['Id', 'Name', 'Age', 'City', 'Average']
            #create a new file with default header:
            with open(file_name, 'w', newline='\n') as file :
             #create writer object:   
             writer=csv.writer(file)
             #write the first row(header) in the file:
             writer.writerow(header)
    #append the student information in the csv file:
    with open(file_name, 'a', newline='\n') as csvfile :
        writer=csv.writer(csvfile)
        writer.writerow([Id, name, age, city, average])
        
    print("Student information added to csv file. ")

def update_student_in_csv(file_name,student_id) :
    file=open(file_name, 'r', newline='\n')
    found=0
    records=csv.reader(file)
    newRecords=[]
    for r in records :
        if r[0]==student_id :
            print("Current record is: ",r)
            print("Enter the new record for this student (if you don't want to change all attributs you can rewrite the old ones)")
            ide=student_id
            name=(input("Enter the name: "))
            age=(int)(input("Enter the age: "))
            city=(input("Enter the city: "))
            average=(float)(input("Enter the average: "))
            new_information=[ide, name, age, city, average]
            for i in range (0,5):
              r[i]=new_information[i]
            print("The updated record: ",r)
            found=1
        newRecords.append(r)
        
    if found==0 :
        print("Record not found!!!")
        file.close()
    else:
        file=open(file_name, 'w', newline='\n')
        writer=csv.writer(file)
        writer.writerows(newRecords)
        file.close()
    
def delete_student_from_csv(file_name, student_id) :
        file= open(file_name, 'r', newline='\n')
        records=csv.reader(file)
        found=0
        newRecords=[]
        for row in records :
            if row[0] == student_id :
               found=1
            else :
               newRecords.append(row)
        if found == 0 :
            print("The student that you want to remove from records doesn't exist originally")
            file.close()
        else :
            file=open(file_name, 'w', newline='\n')
            writer=csv.writer(file)
            writer.writerows(newRecords)
            file.close()
            print("The student is removed")
            
def view_student_list(file_name) :
    file=open(file_name, 'r', newline='\n')
    records=csv.reader(file)
    print("The list of student in this file: ")
    for row in records :
          for i in range (len(row)) :
             print(row[i],end=" ") 
          print()   
    file.close()   
               
def generate_report_from_csv(file_name) :
    key=input("Give me the attribut that you to generate a report about it (Id, Name, Age, City, Average): ")
    file=open(file_name, 'r', newline='\n')
    records=csv.reader(file)
    header=next(records)
    key_founded=0
    try :
        index=header.index(key)
        key_founded=1
    except ValueError :
        key_founded=0
    if key_founded==1 :
        print(f"The report about {key}")
        for row in records :
            print(row[index])
    else :
        print("There is no such an attribut in the given csv file")
    
def save_data_in_csv(file_name, data) :
    file=open(file_name, 'w', newline='\n')
    writer=csv.writer(file)
    writer.writerows(data)
    file.close()
            

#In json file:
def add_student_in_json(file_name) :
    jsonFile=open(file_name)
    data=json.load(jsonFile)
    id=(int)(input("Enter the new student id: "))
    name=(input("Enter the new student name: "))
    age=(int)(input("Enter the new student age: "))
    city=(input("Enter the new student city: "))
    average=(input("Enter the new student average: "))
    new={"id":id, "name":name, "age":age, "city":city, "Average":average}
    """new={"id":7,"name":"Ahmed", "age":19, "city":"Algiers", "Average":15.44}"""
    data.append(new)
    
    jsonFile=open(file_name, 'w')
    json.dump(data,jsonFile,indent=4)
    jsonFile.close()
    print("The student has been added to the json file")
   
def update_students_in_json(file_name, new_information) :
    print("**************************************************")
    view_students_list_in_json(file_name)
    print("**************************************************")
    newData=[]
    file=open(file_name, 'r')
    recentData=json.load(file)
    dict_number=len(recentData)
    print("Enter student id that you want to update: ")
    modifie_id=(int)(input(f"Select it from 1 to {dict_number}: "))
    current_id=1
    for d in recentData :
        if current_id==modifie_id :
            newData.append(new_information)
            current_id+=1
        else :
            newData.append(d)
            current_id+=1
    file=open(file_name, 'w')
    json.dump(newData,file,indent=4)
    print("The student is updated now.")
    file.close()
    
def delete_student_from_json(file_name) :
    newData=[]
    file=open(file_name, 'r')
    recentData=json.load(file)
    dict_number=len(recentData)
    print("Enter student id that you want to delete: ")
    delete_id=(int)(input(f"Select it from 1 to {dict_number}: "))
    current_id=1
    for d in recentData :
        if current_id==delete_id :
            current_id+=1
        else :
            newData.append(d)
            current_id+=1
    file=open(file_name, 'w')
    json.dump(newData,file,indent=4)
    print("The student is removed now.")
    file.close()

def view_students_list_in_json(file_name) :
    file=open(file_name, 'r', newline='\n')
    records=json.load(file)
    print("Students' list:")
    for row in records :
        ide=(row["id"])
        name=(row["name"])
        age=(row["age"])
        city=(row["city"])
        average=(row["Average"])
        print(f"{ide}  {name}  {age}  {city}  {average}")
        file.close()
        
def generate_report_from_json(file_name) :
    attribut=(input("Enter the attribut that you a report about it: "))
    file=open(file_name, 'r', newline='\n')
    records=json.load(file)
    print(f"The list of students' {attribut}")
    for row in records :
        print(row[attribut])
    file.close() 
    
def save_date_in_json(file_name, data) :
    file=open(file_name, 'w', newline='\n')
    json.dump(data, file, indent=4)
    print("saving in file's operation is terminated.")
    file.close()


    
    
        
     
        
        
    
        
        
    
               
            
            
            
                
                
    

    
    
    
   
    
    
                    
           