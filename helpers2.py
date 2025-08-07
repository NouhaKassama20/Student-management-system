# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:30:57 2024

@author: dell
"""

#This module provides functions to read from and write in csv files.
import csv 
import json

#First function: ADD
#IN csv file:
def add_student_to_csv(file_name, ide, name, age, city, average) :
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
        writer.writerow([ide, name, age, city, average])
    #message of operation success:
    return("The student has been added to the csv records")    

def update_student_in_csv(file_name,ide, name, age, city, average) :
    file=open(file_name, 'r', newline='\n')
    found=0
    records=csv.reader(file)
    newRecords=[]
    updatedRecord=[]
    for r in records :
        if r[0]==ide :
            new_information=[ide, name, age, city, average]
            for i in range (0,5):
              r[i]=new_information[i]  
            found=1
        newRecords.append(r)
        
    if found==0 :
        file.close()
        return ("The student doesn't exist in the records!!!")
    else:
        file=open(file_name, 'w', newline='\n')
        writer=csv.writer(file)
        writer.writerows(newRecords)
        file.close()
        return("Student's informations have been updated ")
    
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
            return("The student that you want to remove doesn't exist originally in the records !!!! ")
            file.close()
        else :
            file=open(file_name, 'w', newline='\n')
            writer=csv.writer(file)
            writer.writerows(newRecords)
            file.close()
            return("The student has been removed from the records (: (: ")
            
def view_student_list(file_name) :
    file=open(file_name, 'r', newline='\n')
    records=csv.reader(file)
    print("The list of student in this file: ")
    for row in records :
          for i in range (len(row)) :
             print(row[i],end=" ") 
          print()   
    file.close()   
               
def generate_report_from_csv(file_name, attribut) :
    file=open(file_name, 'r', newline='\n')
    records=csv.reader(file)
    header=next(records)
    key_founded=0
    try :
        index=header.index(attribut)
        key_founded=1
    except ValueError :
        key_founded=0
    if key_founded==1 :
        values_list=[]
        for row in records :
            values_list.append(row[index])
    return(values_list)        
    
def save_data_in_csv(file_name, data) :
    file=open(file_name, 'w', newline='\n')
    writer=csv.writer(file)
    writer.writerow(data)
    return(f"The data has been saved in the file {file_name}")
    file.close()
            

#In json file:
def add_student_in_json(file_name, ide, name, age, city, average) :
    jsonFile=open(file_name)
    data=json.load(jsonFile)
    new={"id":ide, "name":name, "age":age, "city":city, "Average":average}
    """new={"id":7,"name":"Ahmed", "age":19, "city":"Algiers", "Average":15.44}"""
    data.append(new)
    
    jsonFile=open(file_name, 'w')
    json.dump(data,jsonFile,indent=4)
    jsonFile.close()
    return ("The student has been added to the json file")
   
def update_students_in_json(file_name, ide, name, age, city, average) :
    integerIde=(int)(ide)
    
    new_information = {"id":ide, "name":name, "age":age, "city":city, "Average":average}
    
    newData=[]
    
    file=open(file_name, 'r')
    recentData=json.load(file)
    
    current_id=1
    for d in recentData :
        if current_id == integerIde :
            newData.append(new_information)
            current_id+=1
        else :
            newData.append(d)
            current_id+=1
            
    file=open(file_name, 'w')
    json.dump(newData,file,indent=4)
    file.close()
    return("The student is updated now")
    
def delete_student_from_json(file_name, ide) :
    integerIde=(int)(ide)
    newData=[]
    file=open(file_name, 'r')
    recentData=json.load(file)
    current_id=1
    for d in recentData :
        if current_id == integerIde :
            current_id+=1 
        else :
            newData.append(d)
            current_id+=1
    file=open(file_name, 'w')
    json.dump(newData,file,indent=4)
    file.close()
    return("The student is deleted now.")

def view_students_list_in_json(file_name) :
    file=open(file_name, 'r', newline='\n')
    records=json.load(file)

    for row in records :
        ide=(row["id"])
        name=(row["name"])
        age=(row["age"])
        city=(row["city"])
        average=(row["Average"])
        print(f"{ide}  {name}  {age}  {city}  {average}")
        file.close()
        
def generate_report_from_json(file_name, attribut) :
    file=open(file_name, 'r', newline='\n')
    records=json.load(file)
    
    values=[]
    
    for row in records :
        values.append(row[attribut])
     
    file.close() 
   
    return(values)

def save_date_in_json(file_name, data) :
    file=open(file_name, 'w', newline='\n')
    json.dump(data, file, indent=4)
    file.close()
    return("Saving data in the file has been terminated (: (:")
   