# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:39:03 2024

@author: dell
"""

import tkinter as tk
from tkinter import ttk
import helpers2
import importlib
import csv

#reload the file:
importlib.reload(helpers2) 

def initial_window():
    root = tk.Tk()
    root.title("File and Function Selection")
    root.configure(bg="#C5EB43")
    
    #Title of the window:
    title_label= tk.Label(root, text="File type and function choise", fg="#000000", bg="#C5EB43", font=("Times new Roman",24)) 
    title_label.pack()
    
    #empty container for white space:
    empty_container_frame = tk.Frame(root, bg="#C5EB43")
    empty_label= tk.Label(empty_container_frame, text="", fg="#C5EB43", bg="#C5EB43")
    empty_label.pack(side=tk.LEFT)
    empty_container_frame.pack()

    # File Type Selection Frame
    file_type_frame = tk.Frame(root, bg="#C5EB43")
    file_type_label = tk.Label(file_type_frame, text="Select File Type:", fg="#000000", bg="#C5EB43")
    file_type_var = tk.StringVar(root)
    file_type_var.set("CSV")
    file_type_dropdown = ttk.Combobox(file_type_frame, textvariable=file_type_var, values=["CSV", "JSON"])
    file_type_label.pack(side=tk.LEFT)
    file_type_dropdown.pack(side=tk.LEFT)
    file_type_frame.pack()
    
    #empty container for white space:
    empty_container_frame = tk.Frame(root, bg="#C5EB43")
    empty_label= tk.Label(empty_container_frame, text="", fg="#C5EB43", bg="#C5EB43")
    empty_label.pack(side=tk.LEFT)
    empty_container_frame.pack()
        
    # Function Selection Frame
    function_frame = tk.Frame(root, bg="#C5EB43")
    function_label = tk.Label(function_frame, text="Select Function:", fg="#000000", bg="#C5EB43")
    function_var = tk.StringVar(root)
    function_var.set("Add")
    function_dropdown = ttk.Combobox(function_frame, textvariable=function_var, values=["Add", "Delete", "Update", "Display", "Save", "Exit"])
    function_label.pack(side=tk.LEFT)
    function_dropdown.pack(side=tk.LEFT)
    function_frame.pack()

    #empty container for white space:
    empty_container_frame = tk.Frame(root, bg="#C5EB43")
    empty_label= tk.Label(empty_container_frame, text="", fg="#C5EB43", bg="#C5EB43")
    empty_label.pack(side=tk.LEFT)
    empty_container_frame.pack()
    
    def proceed():
        file_type = file_type_var.get()
        function = function_var.get()
        root.destroy()  # Close the initial window
        second_window(file_type, function)

    button_frame = tk.Frame(root, bg="#C5EB43")
    proceed_button = tk.Button(button_frame, text="Proceed", command=proceed, fg="white", bg="#000000")
    proceed_button.pack(side=tk.RIGHT)
    button_frame.pack()

    root.mainloop()
    
    
#########################################################################################################
#########################################################################################################


def second_window(file_type, function):
   second_root = tk.Tk()
   second_root.title("Function Specific GUI")
   file_name="students.csv"
   file_name2="students.json"
   

   if file_type == "CSV":
     second_root.configure(bg="#20e050")  
     if function == "Add":
        #title of the add function window:
        title_label = tk.Label(second_root, text="Adding a new student to the csv records ", fg="black", bg="#20e050", font=("Times new Roman",24))
        title_label.pack()
        #empty container for white space:
        empty_container_frame = tk.Frame(second_root, bg="#20e050")
        empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
        empty_label.pack(side=tk.LEFT)
        empty_container_frame.pack()
        #input fileds:
        id_label = tk.Label(second_root, text="ID:", fg="black",  bg="#20e050")
        id_label.pack()
        id_entry = tk.Entry(second_root)
        id_entry.pack()
        
        name_label= tk.Label(second_root, text="Name: ", fg="black",  bg="#20e050")
        name_label.pack()
        name_entry= tk.Entry(second_root)
        name_entry.pack()
        
        age_labe= tk.Label(second_root, text="Age: ", fg="black",  bg="#20e050")
        age_labe.pack()
        age_entry= tk.Entry(second_root)
        age_entry.pack()
        
        city_label= tk.Label(second_root, text="City: ", fg="black",  bg="#20e050")
        city_label.pack()
        city_entry= tk.Entry(second_root)
        city_entry.pack()
        
        average_label= tk.Label(second_root, text="Average: ", fg="black",  bg="#20e050")
        average_label.pack()
        average_entry= tk.Entry(second_root)
        average_entry.pack()
        #empty container for white space:
        empty_container_frame = tk.Frame(second_root, bg="#20e050")
        empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
        empty_label.pack(side=tk.LEFT)
        empty_container_frame.pack()
        
        def add_student_to_csv():
            ide = id_entry.get()
            name = name_entry.get()
            age = age_entry.get()
            city = city_entry.get()
            average = average_entry.get()
            message=helpers2.add_student_to_csv(file_name, ide, name, age, city, average)
            #empty container for white space:
            empty_container_frame = tk.Frame(second_root, bg="#20e050")
            empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
            empty_label.pack(side=tk.LEFT)
            empty_container_frame.pack()
            message_label=tk.Label(second_root, text="Process's result : "+message, fg="black",  bg="#20e050", font=("Times new Roman",12))
            message_label.pack()
            
        add_button = tk.Button(second_root, text="Add Student", command=add_student_to_csv, fg="#000000",  bg="#eded21")
        add_button.pack()
        #empty container for white space:
        empty_container_frame = tk.Frame(second_root, bg="#20e050")
        empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
        empty_label.pack(side=tk.LEFT)
        empty_container_frame.pack()
        def exit_process():
            second_root.destroy()
        exit_button=tk.Button(second_root, text="Exit", command=exit_process, fg="#000000",  bg="#eded21")
        exit_button.pack()
        
        second_root.mainloop()
        
        #end of second window first case #################################################################
        ##################################################################################################
        
        
     elif function == "Update" :
         #title label of the current precess:
         title_label = tk.Label(second_root, text="Updating student's informations in the csv records ", fg="black", bg="#20e050", font=("Arial",24))
         title_label.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#20e050")
         empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         #input field:
         recent_id_label = tk.Label(second_root, text="Recent student's id: ", fg="black",  bg="#20e050")
         recent_id_label.pack()
         recent_id_entry = tk.Entry(second_root)
         recent_id_entry.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#20e050")
         empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         
         def proceed2():
             ide=recent_id_entry.get()
             second_root.destroy()
             update_window_csv(file_name, ide)
         
         update_proceed_button= tk.Button(second_root, text="update process", command=proceed2, fg="#000000",  bg="#eded21")
         update_proceed_button.pack()
         
         second_root.mainloop()
         
         #Delete case#########################################################
         #######################################################################
         
     elif function == "Delete" :
         #title of deleting process :
         delete_title = tk.Label(second_root, text="Deleting an existing student from the csv records", fg="black", bg="#20e050", font=("Times new Roman",24))
         delete_title.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#20e050")
         empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         #id label and entry:
         ide_label=tk.Label(second_root, text="Give me the id of the student that you want to remove: ", fg="black", bg="#20e050")    
         ide_label.pack()
         ide_entry=tk.Entry(second_root)
         ide_entry.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#20e050")
         empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         
         def delete_student() :
            ide=ide_entry.get()
            message=helpers2.delete_student_from_csv(file_name, ide)
            #empty container for white space:
            empty_container_frame = tk.Frame(second_root, bg="#20e050")
            empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
            empty_label.pack(side=tk.LEFT)
            empty_container_frame.pack()
            #result message:
            message_label= tk.Label(second_root, text="Process's result : "+message, fg="#000000",  bg="#20e050", font=("Arial",12))
            message_label.pack()  
        
         delete_button=tk.Button(second_root, text="Delete student", command=delete_student, fg="#000000",  bg="#eded21")
         delete_button.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#20e050")
         empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         def exit_process():
             second_root.destroy()
         exit_button=tk.Button(second_root, text="Exit", command=exit_process, fg="#000000",  bg="#eded21")
         exit_button.pack()

         
         ####### Reports case ###########################################
         ################################################################
     elif function == "Display" :
         #title of deleting process :
         delete_title = tk.Label(second_root, text="Displaying a report about a given attribut", fg="black", bg="#20e050", font=("Times new Roman",24))
         delete_title.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#20e050")
         empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         #attribut label and entry:
         att_label=tk.Label(second_root, text="Give me the attribut that you want a report abut it from the following list [Id, Name, Age, City, Average] : ", fg="black", bg="#20e050")    
         att_label.pack()
         att_entry=tk.Entry(second_root)
         att_entry.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#20e050")
         empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
        
         def generate_report() :
             attribut=att_entry.get()
             attribut_value_list=[]
             attribut_value_list=helpers2.generate_report_from_csv(file_name,attribut)
             #empty container for white space:
             empty_container_frame = tk.Frame(second_root, bg="#20e050")
             empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
             empty_label.pack(side=tk.LEFT)
             empty_container_frame.pack()
             if len(attribut_value_list)!= 0 :
                 title=tk.Label(second_root, text=f"The {attribut}'s report :", fg="black", bg="#20e050", font=("Times new Roman",14))
                 title.pack()
                 for value in attribut_value_list :
                     value_label=tk.Label(second_root, text=value, fg="black", bg="#20e050")
                     value_label.pack()
             else :
                 #result message:
                 message_label= tk.Label(second_root, text="There is no matched attribut !!! ", fg="#000000",  bg="#20e050", font=("Arial",12))
                 message_label.pack() 
         #report button:
         report_button=tk.Button(second_root, text="Give me a Report", command=generate_report, fg="black", bg="#eded21") 
         report_button.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#20e050")
         empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         def exit_process():
             second_root.destroy()
         exit_button=tk.Button(second_root, text="Exit", command=exit_process, fg="#000000",  bg="#eded21")
         exit_button.pack()
         
         ######### Save case ########################################################
         ############################################################################
     elif function == "Save" :
       #title of saving process :
       save_title = tk.Label(second_root, text="Saving students informations in a new file csv ", fg="black", bg="#20e050", font=("Times new Roman",24))
       save_title.pack()
       #empty container for white space:
       empty_container_frame = tk.Frame(second_root, bg="#20e050")
       empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
       empty_label.pack(side=tk.LEFT)
       empty_container_frame.pack()
       #file name label and entry:
       fileName_label=tk.Label(second_root, text="Give me the file name with the extention csv please : ", fg="black", bg="#20e050")    
       fileName_label.pack()
       fileName_entry=tk.Entry(second_root)
       fileName_entry.pack()
       #input fileds:
       id_label = tk.Label(second_root, text="ID:", fg="black",  bg="#20e050")
       id_label.pack()
       id_entry = tk.Entry(second_root)
       id_entry.pack()
       
       name_label= tk.Label(second_root, text="Name: ", fg="black",  bg="#20e050")
       name_label.pack()
       name_entry= tk.Entry(second_root)
       name_entry.pack()
       
       age_labe= tk.Label(second_root, text="Age: ", fg="black",  bg="#20e050")
       age_labe.pack()
       age_entry= tk.Entry(second_root)
       age_entry.pack()
       
       city_label= tk.Label(second_root, text="City: ", fg="black",  bg="#20e050")
       city_label.pack()
       city_entry= tk.Entry(second_root)
       city_entry.pack()
       
       average_label= tk.Label(second_root, text="Average: ", fg="black",  bg="#20e050")
       average_label.pack()
       average_entry= tk.Entry(second_root)
       average_entry.pack()
       
       #empty container for white space:
       empty_container_frame = tk.Frame(second_root, bg="#20e050")
       empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
       empty_label.pack(side=tk.LEFT)
       empty_container_frame.pack()
       
       def save_student () :
           file_name=fileName_entry.get()
           ide=id_entry.get()
           name=name_entry.get()
           age=age_entry.get()
           city=city_entry.get()
           average=average_entry.get()
           data=[ide, name, age, city, average]
           message=helpers2.save_data_in_csv(file_name, data)
           #empty container for white space:
           empty_container_frame = tk.Frame(second_root, bg="#20e050")
           empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
           empty_label.pack(side=tk.LEFT)
           empty_container_frame.pack()
           #process message:
           #result message:
           message_label= tk.Label(second_root, text="Process's result : "+message, fg="#000000",  bg="#20e050", font=("Arial",12))
           message_label.pack()     
               
       save_button=tk.Button(second_root, text="Save in csv file", command=save_student, fg="black", bg="#eded21")
       save_button.pack()
       #empty container for white space:
       empty_container_frame = tk.Frame(second_root, bg="#20e050")
       empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
       empty_label.pack(side=tk.LEFT)
       empty_container_frame.pack()
       def exit_process():
           second_root.destroy()
       exit_button=tk.Button(second_root, text="Exit", command=exit_process, fg="#000000",  bg="#eded21")
       exit_button.pack()
       
       ############# Exit case #######################################
       ###############################################################
     elif function == "Exit" :
          second_root.destroy()
          
          #**************************************************************************************************************
          #**************************************************************************************************************
   if file_type == "JSON" :
     second_root.configure(bg="#eded21") 
     ################################ Add case ##################################################
     if function == "Add" :
         #title of the add function window:
         title_label = tk.Label(second_root, text="Adding a new student to the json records ", fg="black", bg="#eded21", font=("Times new Roman",24))
         title_label.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         #input fileds:
         id_label = tk.Label(second_root, text="ID:", fg="black",  bg="#eded21")
         id_label.pack()
         id_entry = tk.Entry(second_root)
         id_entry.pack()
         
         name_label= tk.Label(second_root, text="Name: ", fg="black",  bg="#eded21")
         name_label.pack()
         name_entry= tk.Entry(second_root)
         name_entry.pack()
         
         age_labe= tk.Label(second_root, text="Age: ", fg="black",  bg="#eded21")
         age_labe.pack()
         age_entry= tk.Entry(second_root)
         age_entry.pack()
         
         city_label= tk.Label(second_root, text="City: ", fg="black",  bg="#eded21")
         city_label.pack()
         city_entry= tk.Entry(second_root)
         city_entry.pack()
         
         average_label= tk.Label(second_root, text="Average: ", fg="black",  bg="#eded21")
         average_label.pack()
         average_entry= tk.Entry(second_root)
         average_entry.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         
         def add_student_to_json():
             ide = id_entry.get()
             name = name_entry.get()
             age = age_entry.get()
             city = city_entry.get()
             average = average_entry.get()
             message=helpers2.add_student_in_json(file_name2, ide, name, age, city, average)
             #empty container for white space:
             empty_container_frame = tk.Frame(second_root, bg="#eded21")
             empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
             empty_label.pack(side=tk.LEFT)
             empty_container_frame.pack()
             message_label=tk.Label(second_root, text="Process's result : "+message, fg="black",  bg="#eded21", font=("Times new Roman",12))
             message_label.pack()
             
         add_button = tk.Button(second_root, text="Add Student", command=add_student_to_json, fg="#000000",  bg="#20e050")
         add_button.pack() 
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         def exit_process():
             second_root.destroy()
         exit_button=tk.Button(second_root, text="Exit", command=exit_process, fg="black", bg="#20e050")
         exit_button.pack()
         
         second_root.mainloop()
         ######################################### update case #############################################
     elif function == "Update" :
         #title label of the current precess:
         title_label = tk.Label(second_root, text="Updating student's informations in the json records ", fg="black", bg="#eded21", font=("Times new Roman",24))
         title_label.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         #input field:
         recent_id_label = tk.Label(second_root, text="Student's id: ", fg="black",  bg="#eded21")
         recent_id_label.pack()
         recent_id_entry = tk.Entry(second_root)
         recent_id_entry.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         #message of guide:
         guide_label=tk.Label(second_root, text="Give me the new informations of the student (if you don't want to update them all give me the old ones) : ", fg="black", bg="#eded21")    
         guide_label.pack()
         #input fileds:
         name_label= tk.Label(second_root, text="Name: ", fg="black",  bg="#eded21")
         name_label.pack()
         name_entry= tk.Entry(second_root)
         name_entry.pack()
         
         age_labe= tk.Label(second_root, text="Age: ", fg="black",  bg="#eded21")
         age_labe.pack()
         age_entry= tk.Entry(second_root)
         age_entry.pack()
         
         city_label= tk.Label(second_root, text="City: ", fg="black",  bg="#eded21")
         city_label.pack()
         city_entry= tk.Entry(second_root)
         city_entry.pack()
         
         average_label= tk.Label(second_root, text="Average: ", fg="black",  bg="#eded21")
         average_label.pack()
         average_entry= tk.Entry(second_root)
         average_entry.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         
         def update_student_in_json () :
             ide=recent_id_entry.get()
             name=name_entry.get()
             age=age_entry.get()
             city=city_entry.get()
             average=average_entry.get()
             message=helpers2.update_students_in_json(file_name2, ide, name, age, city, average)
             #empty container for white space:
             empty_container_frame = tk.Frame(second_root, bg="#eded21")
             empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
             empty_label.pack(side=tk.LEFT)
             empty_container_frame.pack()
             message_label=tk.Label(second_root, text="Process's result : "+message, fg="black",  bg="#eded21", font=("Times new Roman",12))
             message_label.pack()
             
         update_button=tk.Button(second_root, text="Update student", command=update_student_in_json, fg="#000000",  bg="#20e050")
         update_button.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         def exit_process():
             second_root.destroy()
         exit_button=tk.Button(second_root, text="Exit", command=exit_process, fg="black", bg="#20e050")
         exit_button.pack()
         second_root.mainloop()
         ############################# Delete case #########################################################
     elif function == "Delete" :         
         #title of the delete function window:
         title_label = tk.Label(second_root, text="Deleting a student from the json records ", fg="black", bg="#eded21", font=("Times new Roman",24))
         title_label.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         #input fileds:
         #message of guide:
         guide_label=tk.Label(second_root, text="Give me the student's id that you want to remove : ", fg="black", bg="#eded21")    
         guide_label.pack()    
         id_entry = tk.Entry(second_root)
         id_entry.pack() 
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         
         def delete_student_to_json():
             ide=id_entry.get()
             message=helpers2.delete_student_from_json(file_name2, ide)
             #empty container for white space:
             empty_container_frame = tk.Frame(second_root, bg="#eded21")
             empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
             empty_label.pack(side=tk.LEFT)
             empty_container_frame.pack()
             message_label=tk.Label(second_root, text="Process's result : "+message, fg="black",  bg="#eded21", font=("Times new Roman",12))
             message_label.pack()
             
         delete_button = tk.Button(second_root, text="Delete Student", command=delete_student_to_json, fg="#000000",  bg="#20e050")
         delete_button.pack() 
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         def exit_process():
             second_root.destroy()
         exit_button=tk.Button(second_root, text="Exit", command=exit_process, fg="black", bg="#20e050")
         exit_button.pack()
         second_root.mainloop()
         ######################### Display attribut's report #############################################
         #################################################################################################
     elif function == "Display" :         
         #title of the display function window:
         display_title = tk.Label(second_root, text="Displaying a report about a given attribut ", fg="black", bg="#eded21", font=("Times new Roman",24))
         display_title.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         #input fileds:
         #message of guide:
         guide_label=tk.Label(second_root, text="Give me the attribut that you a report about it from the following list [id, name, age, city, Average] : ", fg="black", bg="#eded21")    
         guide_label.pack()    
         att_entry = tk.Entry(second_root)
         att_entry.pack() 
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         
         def display_report():
             attribut=att_entry.get()
             values=helpers2.generate_report_from_json(file_name2, attribut)
             #empty container for white space:
             empty_container_frame = tk.Frame(second_root, bg="#eded21")
             empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
             empty_label.pack(side=tk.LEFT)
             empty_container_frame.pack()
             Title=tk.Label(second_root, text=f"The {attribut}'s report: ", fg="black", bg="#eded21", font=("Times new Roman",14))
             Title.pack()
             for val in values :
                 val_label=tk.Label(second_root, text=val, fg="black", bg="#eded21")
                 val_label.pack()
             
         Display_button = tk.Button(second_root, text="Display report", command=display_report, fg="black", bg="#20e050")
         Display_button.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         def exit_process():
             second_root.destroy()
         exit_button=tk.Button(second_root, text="Exit", command=exit_process, fg="black", bg="#20e050")
         exit_button.pack()
         second_root.mainloop()
         ######################### Save data #############################################
         #################################################################################################
     elif function == "Save" :
         #title of the display function window:
         Save_title = tk.Label(second_root, text="Saving student informations in a json file:", fg="black", bg="#eded21", font=("Times new Roman",24))
         Save_title.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         #input fileds:
         #message of guide:
         guide_label=tk.Label(second_root, text="Give me the name of the new json file:", fg="black", bg="#eded21")    
         guide_label.pack()    
         file_name_entry = tk.Entry(second_root)
         file_name_entry.pack() 
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         #input fileds:
         id_label = tk.Label(second_root, text="ID:", fg="black",  bg="#eded21")
         id_label.pack()
         id_entry = tk.Entry(second_root)
         id_entry.pack()
         
         name_label= tk.Label(second_root, text="Name: ", fg="black",  bg="#eded21")
         name_label.pack()
         name_entry= tk.Entry(second_root)
         name_entry.pack()
         
         age_labe= tk.Label(second_root, text="Age: ", fg="black",  bg="#eded21")
         age_labe.pack()
         age_entry= tk.Entry(second_root)
         age_entry.pack()
         
         city_label= tk.Label(second_root, text="City: ", fg="black",  bg="#eded21")
         city_label.pack()
         city_entry= tk.Entry(second_root)
         city_entry.pack()
         
         average_label= tk.Label(second_root, text="Average: ", fg="black",  bg="#eded21")
         average_label.pack()
         average_entry= tk.Entry(second_root)
         average_entry.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         
         def save_data():
             file_name=file_name_entry.get()
             ide=id_entry.get()
             name=name_entry.get()
             age=age_entry.get()
             city=city_entry.get()
             average=average_entry.get()
             
             data={"id":ide, "name":name, "age":age, "city":city, "Average":average}
             message=helpers2.save_date_in_json(file_name, data)
             #empty container for white space:
             empty_container_frame = tk.Frame(second_root, bg="#eded21")
             empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
             empty_label.pack(side=tk.LEFT)
             empty_container_frame.pack()
             message_label=tk.Label(second_root, text="Process's result : "+message, fg="black",  bg="#eded21", font=("Times new Roman",12))
             message_label.pack()
             
         Save_button=tk.Button(second_root, text="Save in the file", command=save_data, fg="black", bg="#20e050")
         Save_button.pack()
         #empty container for white space:
         empty_container_frame = tk.Frame(second_root, bg="#eded21")
         empty_label= tk.Label(empty_container_frame, text="", fg="#eded21", bg="#eded21")
         empty_label.pack(side=tk.LEFT)
         empty_container_frame.pack()
         def exit_process():
             second_root.destroy()
         exit_button=tk.Button(second_root, text="Exit", command=exit_process, fg="black", bg="#20e050")
         exit_button.pack()
         second_root.mainloop()
         
     elif function == "Exit" :
           second_root.destroy()         
                 
       
def update_window_csv(file_name, ide) :
    root = tk.Tk()
    root.title("Update function GUI")
    root.configure(bg="#20e050")
    
    file=open(file_name, 'r', newline='\n')
    #found=0
    records=csv.reader(file)
    #newRecords=[]
    for r in records :
        if r[0] == ide :
            #diplay the recent informations of the given student:
            label1= tk.Label(root, text="The current informations of the given student: ", fg="black",  bg="#20e050", font=("Times new Roman",14))
            label1.pack()
            id_label = tk.Label(root, text=f"Id : {r[0]}", fg="black",  bg="#20e050")
            id_label.pack()
            name_label = tk.Label(root, text=f"Name : {r[1]}", fg="black",  bg="#20e050")
            name_label.pack()
            age_label = tk.Label(root, text=f"Age : {r[2]}", fg="black",  bg="#20e050")
            age_label.pack()
            city_label = tk.Label(root, text=f"City : {r[3]}", fg="black",  bg="#20e050")
            city_label.pack()
            average_label = tk.Label(root, text=f"Average : {r[4]}", fg="black",  bg="#20e050")
            average_label.pack()
            #empty container for white space:
            empty_container_frame = tk.Frame(root, bg="#20e050")
            empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
            empty_label.pack(side=tk.LEFT)
            empty_container_frame.pack()
            #message of guide:
            guide_label= tk.Label(root, text="Enter the new updates for the student, if you dont't want tp change them all give the old ones: ", fg="black",  bg="#20e050", font=("Times new Roman",14))
            guide_label.pack()
            #input fields:
            id_label = tk.Label(root, text="ID:", fg="black",  bg="#20e050")
            id_label.pack()
            id_entry = tk.Entry(root)
            id_entry.pack()
            
            name_label= tk.Label(root, text="Name: ", fg="black",  bg="#20e050")
            name_label.pack()
            name_entry= tk.Entry(root)
            name_entry.pack()
            
            age_labe= tk.Label(root, text="Age: ", fg="black",  bg="#20e050")
            age_labe.pack()
            age_entry= tk.Entry(root)
            age_entry.pack()
            
            city_label= tk.Label(root, text="City: ", fg="black",  bg="#20e050")
            city_label.pack()
            city_entry= tk.Entry(root)
            city_entry.pack()
            
            average_label= tk.Label(root, text="Average: ", fg="black",  bg="#20e050")
            average_label.pack()
            average_entry= tk.Entry(root)
            average_entry.pack()
            #empty container for white space:
            empty_container_frame = tk.Frame(root, bg="#20e050")
            empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
            empty_label.pack(side=tk.LEFT)
            empty_container_frame.pack()
            
            #The call of the update function after filling the fields:
            def update_function_in_csv() :
                ide=id_entry.get()
                name=name_entry.get()
                age=age_entry.get()
                city=city_entry.get()
                average=average_entry.get()
                #empty container for white space:
                empty_container_frame = tk.Frame(root, bg="#20e050")
                empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
                empty_label.pack(side=tk.LEFT)
                empty_container_frame.pack()
                #result message:
                message=helpers2.update_student_in_csv(file_name, ide, name, age, city, average)
                message_label= tk.Label(root, text="Process's result : "+message, fg="#000000",  bg="#20e050", font=("Arial",12))
                message_label.pack() 
            #The button of starting update process :
            update_button= tk.Button(root, text="Update student", command=update_function_in_csv, fg="#000000",  bg="#eded21")    
            update_button.pack() 
            #empty container for white space:
            empty_container_frame = tk.Frame(root, bg="#20e050")
            empty_label= tk.Label(empty_container_frame, text="", fg="#20e050", bg="#20e050")
            empty_label.pack(side=tk.LEFT)
            empty_container_frame.pack()
            def exit_process():
                root.destroy()
            exit_button=tk.Button(root, text="Exit", command=exit_process, fg="#000000",  bg="#eded21")
            exit_button.pack()
            root.mainloop()
            
            #end of update window ##########################################################################
            ################################################################################################
            
            
    
if __name__ == "__main__":
    initial_window()