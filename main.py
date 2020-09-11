# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:15:57 2020

@author: rache
"""

#import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.Font as tkFont
from tkinter import *
import tkinter.messagebox as messagebox




# Main page display
class MainPage:
    def __init__(self, main_window):
        main_window.destroy()
        
        self.window = tk.Tk()
        self.window.title('Student Management System')
        self.window.geomerty('300x470')
        
        label = Label(self.window, text = 'Student Management System', font=('Verdana', 20))
        label.pack(pady = 100)
        
        Button(self.window, text="Faculty Log-in", font=tkFont.Font(size=16), command=lambda: AdminPage(self.window), \
               width=30, height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="Student Log-in", font=tkFont.Font(size=16), command=lambda: StudentPage(self.window), \
               width=30, height=2,fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="About", font=tkFont.Font(size=16), command=lambda: AboutPage(self.window), \
               width=30, height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text='Exist', height=2, font=tkFont.Font(size=16), width=30, command=self.window.destroy, \
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        
        self.window.mainloop()


# Professor's log-in page        
class FaclutyPage:
    # Sign-in page
    def __init__(self, main_window):
        main_window.destroy()
        
        self.window = tk.Tk()
        self.window.title("Sign-in As Faculty")
        self.window.geometry('300x450')
        
        label = tk.Label(self.window, text="Faculty Sign-in:", bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack()
        
        Label(self.window, text="Username:", font=tkFont.Font(size=14)).pack(pady=25)
        self.faculty_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.faculty_username.pack()
        
        Label(self.window, text="Password:", font=tkFont.Font(size=14)).pack(pady=25)
        self.faculty_password = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.faculty_password.pack()
        
        Button(self.window, text="Sign-in", width=8, font=tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text="Back to main page", width=8, font=tkFont.Font(size=12), command=self.back).pack()
        
        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()
    
    # Login system and compare password with SQL database
    def login(self):
        print(str(self.faculty_username.get()))
        print(str(self.faculty_password.get()))
        fact_password = None
        
        db = pymysql.connect("localhost", "root", "root", "student")
        cursor = db.cursor()
        sql = "SELECT * FROM admin_login_k WHERE fact_username = '%s'" % (self.faculty_username.get())
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                fact_username = row[0]
                fact_password = row[1]
                print("fact_username = %s, fact_password = %" % ( fact_username, fact_password))
            
        except:
                print("Error: unable to fecth data")
                messagebox.showinfo("Error: Username or Password incorrect!")
        db.close()
        
        print("Loading the faculty management system!")
        print("self", self.faculty_password)
        print("local", fact_password)
        
        if self.faculty_password.get() == fact_password:
            FaclutyPage(self.window)
        else:
            messagebox.showinfo("Error: Username or Password incorrect!")
    
    # Back and display main page
    def back(self):
        MainPage(self.window)
        
        
# Student's log-in system
class StudentPage:
    # Sign-in page
    def __init__(self, main_window):
        main_window.destroy()
        
        self.window = tk.Tk()
        self.window.title("Sign-in As Student")
        self.window.geometry('300x450')
        
        label = tk.Label(self.window, text="Student Sign-in:", bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack()
        
        Label(self.window, text="Username:", font=tkFont.Font(size=14)).pack(pady=25)
        self.student_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.student_username.pack()
        
        Label(self.window, text="Password:", font=tkFont.Font(size=14)).pack(pady=25)
        self.student_password = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.student_password.pack()
        
        Button(self.window, text="Sign-in", width=8, font=tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text="Back to main page", width=8, font=tkFont.Font(size=12), command=self.back).pack()
        
        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()         
        
    # Login system and compare password with SQL database
    def login(self):
        print(str(self.student_username.get()))
        print(str(self.student_password.get()))
        stu_password = None
        
        db = pymysql.connect("localhost", "root", "root", "student")
        cursor = db.cursor()
        sql = "SELECT * FROM admin_login_k WHERE stu_username = '%s'" % (self.student_username.get())
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                stu_username = row[0]
                stu_password = row[1]
                print("stu_username = %s, stu_password = %" % (stu_username, stu_password))
            
        except:
                print("Error: unable to fecth data")
                messagebox.showinfo("Error: Username or Password incorrect!")
        db.close()
        
        print("Loading the student management system!")
        print("self", self.student_password)
        print("local", stu_password)
        
        if self.student_password.get() == stu_password:
            StudentView(self.window, self.sutdent_username.get())
        else:
            messagebox.showinfo("Error: Username or Password incorrect!")
    
    # Back and display main page
    def back(self):
        MainPage(self.window)    
        
        
 
        
 
# Facluty Management System   
#class FacultySystem:
     
     
     
     
     
     
# Student Management System
#class StudentSystem:
    
 
    
 
    
 
# About page from main page    
class AboutPage:
    def __init__(self, main_window):
         main_window.destryo()
         
         self.window = tk.TK()
         self.window.title('About')
         self.window.geometry('300x450')
         
         label = tk.Label(self.window, text='Student Management System', bg='green', font=('Verdana', 20), width=30, height=2)
         label.pack()
         
         Label(self.window, text='Made by Rachel', font=('Verdana', 18)).pack(pady=30)
         Label(self.window, text='github.com/rachelhyeh', font=('Verdana', 18)).pack(pady=5)

         Button(self.window, text="Back to main page", width=8, font=tkFont.Font(size=12), command=self.back).pack(pady=100)
         
         self.window.protocol("WM_DELETE_WINDOW", self.back)
         self.window.mainloop()
         
    def back(self):
        MainPage(self.window)
     
     
     
# Run the main
if __name__ == '__main':
    try:
        db.pymysql.connect("loalhost", "root", "root", "student")
        cursor = db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS student_k(
				id char(20) NOT NULL,
				name char(20) default NULL,
				gender char(5) default NULL,  
				age char(5) default NULL,
				PRIMARY KEY (id)
				
				) ENGINE = InnoDB 
				DEFAULT	CHARSET = utf8
				"""
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS admin_login_k(
						admin_id char(20) NOT NULL,
						admin_pass char(20) default NULL,
						PRIMARY KEY (admin_id)
						) ENGINE = InnoDB 
						DEFAULT	CHARSET = utf8
                        """
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS stu_login_k(
						stu_id char(20) NOT NULL,
						stu_pass char(20) default NULL,
						PRIMARY KEY (stu_id)
						) ENGINE = InnoDB 
						DEFAULT	CHARSET = utf8
						"""
        cursor.execute(sql)
        db.close()
        window = tk.TK()
        MainPage(window)
    except:
        messagebox.showinfo('Error!', "Failure to connect database!")
     
     
     
     
    
 
    
 
    
 
    
 
        
        