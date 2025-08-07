# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:38:06 2024

@author: dell
"""
#helpers module gives us all fucntions to interacts with csv and json files:
import helpers
import importlib
#reload the file:
importlib.reload(helpers)    
#allow the user to choose the type of ifle that he|she wants (to didn't repeat the code that ask him in each step of function):
file_type=(input("Enter file's type: "))    
while True :
    #allow the user to choose the fucntionality:
    print("Functions' codes menu:\n1: Add Student\n2: Update Student\n3: Delete Student\n4: View Student List\n5: Generate Report\n6:Save data\n7:Exit ")    
    function_choice=(int)(input("Enter the code of function that you want to do: "))
    #csv file:
    #Call add function 
    file_name='students.csv'
    file_name2='students.json'
    if function_choice == 1 and file_type == 'csv' :
      """ print("Add function to csv file") """
      helpers.add_student_to_csv(file_name)
  
    #Call update function
    elif function_choice == 2 and file_type == 'csv' :
         student_id=input("Enter the student id ")
         helpers.update_student_in_csv(file_name,student_id)
     
    #Call delete_student_records function :
    elif  function_choice==3 and file_type=='csv' :
        student_id=(input("Enter student id to delete his/he recors: "))
        helpers.delete_student_from_csv(file_name,student_id)
    
    #Call view_student_list function :
    elif function_choice==4 and file_type=='csv' :
        helpers.view_student_list(file_name)  
    
    #Call generate_report_from_csv function :
    elif  function_choice==5 and file_type=='csv' :
         helpers.generate_report_from_csv(file_name)
         
    #Call save_data_in_csv function:
    elif function_choice==6 and file_type=='csv' :
        file_name4=input("Enter the name of the new file: ") 
        helpers.add_student_to_csv(file_name4)
         
    #Exit the program:
    elif function_choice==7 :
          print("The program is terminated...")
          break
      
        
    #In json file:
    #Call add function:
    elif function_choice==1 and file_type=='json' :  
        helpers.add_student_in_json(file_name2)
        
    #Call update_student_in_json function:
    elif function_choice==2 and file_type=='json' :
         ide=(int)(input("Enter student's id: "))
         name=(input("Enter student's name: "))
         age=(int)(input("Enter student's age: "))
         city=(input("Enter student's city: "))
         average=(float)(input("Enter student's average: "))
         data={"id":ide, "name":name, "age":age, "city":city, "Average":average}
         helpers.update_students_in_json(file_name2, data)
         
    #Call delete function:
    elif function_choice==3 and file_type=='json' :
         helpers.delete_student_from_json(file_name2)
         
    #Call view_student_list function:
    elif function_choice==4 and file_type=='json' : 
        helpers.view_students_list_in_json(file_name2)
        
    #Call generate_report_from_json function:
    elif function_choice==5 and file_type=='json' : 
        helpers.generate_report_from_json(file_name2)
        
    #Call save_data function:
    elif function_choice==6 and file_type=='json' :
         file_name4=(input("Enter the name of the new file that you want to save in it: "))
         ide=(int)(input("Enter student's id: "))
         name=(input("Enter student's name: "))
         age=(int)(input("Enter student's age: "))
         city=(input("Enter student's city: "))
         average=(float)(input("Enter student's average: "))
         data={"id":ide, "name":name, "age":age, "city":city, "Average":average}
         helpers.save_date_in_json(file_name4, data)    
           
             
         
        
        
     
        
        
       
    

    
    
