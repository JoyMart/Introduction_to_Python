#
#               this is the function part of my student tracker
#
#
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3

import tracker_gui
import tracker_main



#centering the form window
def center_window(self, w, h):
        screen_w = self.master.winfo_screenwidth()
        screen_h = self.master.winfo_screenheight()
        x = int((screen_w/2) -(w/2))
        y = int((screen_h/2) - (h/2))
        centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        return centerGeo


#closing the window
def ask_quit(self):
        if messagebox.askokcancel("Exit student tracker", "Are you sure you want to close the student tracker?"):
                self.master.destroy()
                os._exit(0)

#_________create db_________________
def create_db(self):
        conn = sqlite3.connect("tracker.db")
        with conn:
                cur = conn.cursor()
                cur.execute("CREATE TABLE if not exists tbl_student_tracker( \
                        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                        col_fname TEXT, \
                        col_lname TEXT, \
                        col_fullname TEXT, \
                        col_phone TEXT, \
                        col_email TEXT, \
                        col_course TEXT \
                        );")
                conn.commit()
        conn.close()
        first_run(self)

def first_run(self):
        v_data = ("student", "name", "student name", "111-111-1111", "student@email.com", "course title")
        conn = sqlite3.connect('tracker.db')
        with conn:
                cur = conn.cursor()
                cur, count = count_records(cur)
                if count <1:
                        cur.execute("""INSERT INTO tbl_student_tracker (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?, ?, ?, ?, ?, ?)""", ("student", "name", "student name", "111-111-1111", "student@email.com", "course title"))
                        conn.commit()
        conn.close()

def count_records(cur):
        count = ""
        cur.execute("""SELECT COUNT (*) FROM tbl_student_tracker""")
        count = cur.fetchone() [0]
        return cur, count

#select entry
def onSelect(self, event):
        varList = event.widget
        select = varList.curselection()[0]
        value = varList.get(select)
        conn = sqlite3.connect('tracker.db')
        with conn:
                cur = conn.cursor()
                cur.execute("""SELECT col_fname, col_lname, col_phone, col_email, col_email FROM tbl_student_tracker WHERE col_fullname = (?)""", [value])
                varBody = cur.fetchall()
                for data in varBody:
                        self.txt_fname.delete(0, END)
                        self.txt_fname.insert(0, data[0])
                        self.txt_lname.delete(0, END)
                        self.txtl_lname.insert(0, data[1])
                        self.txt_fullname.delete(0, END)
                        self.txtl_fullname.insert(0, data[2])
                        self.txt_phone.delete(0, END)
                        self.txt_phone.insert(0, data[3])
                        self.txt_email.delete(0, END)
                        self.txt_email.insert(0, data[4])
                        self.txt_course.delete(0, END)
                        self.txt_course.insert(0, data[5])

def addToList(self):
        var_fname = self.txt_fname.get().strip().title()
        var_lname = self.txt_lname.get().strip().title()
        var_fullname = ("{} {}".format(var_fname, var_lname))
        print("fullname: {}".format(var_fullname))
        var_phone = self.txt_phone.get().strip().title()
        var_email = self.txt_email.get().strip().title()
        var_course = self.txt_course.get().strip().title()
        if not "@" or not "." in var_email:
                print("incorrect email format!!!")
        if(len(var_fname)>0) and (len(var_lname)>0) and (len(var_phone)>0) and (len(var_email)>0) and (len(var_course)>0):
                conn = sqlite3.connect('tracker.db')
                with conn:
                        cur = conn.cursor()
                        cur.execute("""SELECT COUNT (col_fname) FROM tbl_student_tracker WHERE col_fullname ='{}' """.format(var_fullname))
                        count = cur.fetchone()[0]
                        checkname = count
                        if checkname ==0:
                                cur.execute("""INSERT INTO tbl_student_tracker (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?, ?, ?, ?, ?, ?)""", (var_fname, var_lname, var_fullname, var_phone, var_email, var_course))
                                self.lst_1.insert(END, var_fullname)
                                onClear(self)
                                conn.commit()
                        else:
                                messagebox.showerror("Name Error", " '{}' already exists in this database! Please choose a different name.".format(fullname))
                                onClear(self)
                conn.close()
        else:
                messagebox.showerror("Missing Text Error", "Please enter information in all the fields, thanks!")


def onDelete(self):
        select = self.lst_1.get(self.lst_1.curselection())
        conn = sqlite3.connect('tracker.db')
        with conn:
                cur = conn.cursor()
                cur.execute("""SELECT COUNT(*) FROM tbl_student_tracker""")
                count = cur.fetchone() [0]
                if count > 1:
                        confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with ({})\nwill be perminately deleted. \n\nProceed with deletion request?".format(select))
                        if confirm:
                                cur.execute("""DELETE FROM tbl_student_tracker WHERE col_fullname ='{}' """.format(select))
                        onDelete(self)
                        conn.commit()
                else:
                        confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(select, select))
        conn.close()

def onDeleted(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_course.delete(0, END)
        try:
                index = self.lst_1.curselection()[0]
                self.lst_1.delete(index)
        except IndexError:
                pass

def onClear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_course.delete(0, END)

                         

def onRefresh(self):
        self.lst_1.delete(0, END)
        conn = sqlite3.connect('tracker.db')
        with conn:
                cur = conn.cursor()
                cur.execute("""SELECT COUNT (*) FROM tbl_student_tracker""")
                count = cur.fetchone()[0]
                i = 0
                while i < count:
                        cur.execute("""SELECT col_fullname FROM tbl_student_tracker""")
                        List = cur.fetchall()[i]
                        for item in List:
                                self.lst_1.insert(0, str(item))
                                i +=1
                conn.commit()
        conn.close()

def onUpdate(self):
        try:
                select = self.lst_1.curselection() [0]
                value= self.lst_1.get(select)
        except:
                msg = messagebox.showinfo("Missing selection", "No name was selected from the list box. \nCancelling the Update request.")
                return msg
        phone = self.txt_phone.get().strip()
        email = self.txt_email.get().strip()
        course = self.txt_course.get().strip()
        if (len(phone)>0) and (len(email)>0) and (len(course)>0):
                conn = sqlite3.connect('tracker.db')
                with conn:
                        cur = conn.cursor()
                        cur.execute("""SELECT COUNT (col_phone) FROM tbl_student_tracker WHERE col_phone = '{}'""".format(phone))
                        count = cur.fetchone()[0]
                        cur.execute("""SELECT COUNT (col_email) FROM tbl_student_tracker WHERE col_email = '{}'""".format(email))
                        count1 = cur.fetchone()[0]
                        cur.execute("""SELECT COUNT (col_course) FROM tbl_student_tracker WHERE col_course = '{}'""".format(course))
                        count2 = cur.fetchone()[0]
                        print(count)
                        print(count1)
                        print(count2)
                        if count ==0 or count1 ==0 or count2 ==0:
                                reponse = messagebox.asktocancel("Update Request", "The following changes ({}), ({}) and ({}) will not be implemented for ({}). \n\nProceed with the update request?".format(phone, email, course, value))
                                print(response)
                                if response:
                                        with conn:
                                                cur = conn.cursor()
                                                cur.execute("""UPDATE tbl_student_tracker SET col_phone = '{0}', col_email ='{1}', col_course = '{2}' WHERE col_fullname = '{3}' """.format(phone, email, course, value))
                                                onClear(self)
                                                conn.commit()
                                else:
                                        messagebox.showinfo("Cancel Request", "No changes have been made to ({}).".format(value))
                        else:
                                messagebox.showinfo("No changes detected", "({}), ({}) and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(phone, email, course))
                        onClear(self)
                conn.close()
        else:
                messagebox.showerror("Missing information",  "Please select a name from the list. \nThen edit the phone, email, or course information.")
        onClear(self)

if __name__ =="__main__":
        pass




































