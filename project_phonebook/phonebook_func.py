#
#               this is the function part of my phonebook
#
#
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3

import phonebook_gui
import phonebook_main



def center_window(self, w, h):
        #get user's screen w and h
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        #calculate x and y coordinate to paint app centered on user's screen
        x = int((screen_width/2) - (w/2))
        y = int((screen_height/2) -(h/2))
        centerGEO = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        return centerGEO

#catch if the user clicks on the upper-right 'X' to enxure they want to close the window
def ask_quit(self):
        if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #this is the pop-up that will close app
                self.master.destroy()
                os._exit(0)


#------------------------------------------------------------------
def create_db(self):
        conn = sqlite3.connect("phonebook.db")
        with conn:
                cur = conn.cursor()
                cur.execute("CREATE TABLE if not exists tbl_phonebook(  \
                        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                        col_fname TEXT, \
                        col_lname TEXT, \
                        col_fullname TEXT, \
                        col_phone TEXT, \
                        col_email TEXT \
                        )")
                #must commit to save changes
                conn.commit()
        conn.close()
        first_run(self)


#first run
def first_run(self):
        data = ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com')
        conn = sqlite3.connect("phonebook.db")
        with conn:
                cur = conn.cursor()
                cur, count= count_records(cur)
                if count <1:
                        cur.execute("""INSERT INTO tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) \
                                                VALUES (?, ?, ?, ?, ?)""", (data))
                        conn.commit()
        conn.close()


def count_records(cur):
        count = ""
        cur.execute("""SELECT COUNT (*) FROM tbl_phonebook""")
        count = cur.fetchone() [0]
        return cur, count

#select and item in List box
def onSelect(self, event):
        #self.lstList1 widget
        varList = event.widget
        select = varList.curselection() [0]
        value = varList.get(select)
        conn = sqlite3.connect('phonebook.db')
        with conn:
                cur = conn.cursor
                cur.execute("""SELECT col_fname, col_lname, col_phone, col_email FROM tbl phonebook WHERE col_fullname = (?)""", [value])
                var_body = cur.fetchall()
                #returns tuple to slice into parts
                for data in varBody:
                         self.txt_fname.delete(0, END)
                         self.txt_fname.insert(0, data[0])
                         self.txt_lname.delete(0, END)
                         self.txtl_lname.insert(0, data[1])
                         self.txt_phone.delete(0, END)
                         self.txt_phone.insert(0, data[2])
                         self.txt_email.delete(0, END)
                         self.txt_email.insert(0, data[3])

def addToList(self):
        var_fname = self.txt_fname.get().strip().title()
        var_lname = self.txt_lname.get().strip().title()
        var_fullname = ("{} {}".format(var_fname, var_lname))
        print("var_fullname: {}".format(var_fullname))
        var_phone = self.txt_phone.get().strip()
        var_email = self.txt_email.get().strip()
        if not "@" or not "." in var_email:
                print("Incorrect email format!!!")
        if (len(var_fname) > 0 ) and (len(var_lname) >0) and (len(var_phone) >0) and (len(var_email) >0):
                conn = sqlite3.connect('phonebook.db')
                with conn:
                        cur = conn.cursor()
                        cur.execute("""SELECT COUNT (col_fname) FROM tbl_phonebook WHERE col_fullname = '{}' """.format(var_fullname))
                        count = cur.fetchone()[0]
                        chkname = count
                        if chkname == 0:
                                print("chkname: {}".format(chkname))
                                cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                                self.lst_List1.insert(END, var_fullname)
                                onClear(self)
                        else:
                                messagebox.showerror("Name Error", " '{}' already exists in the database! Please choose a different name.".format(car_fullname))
                                onClear(self)
                        conn.commit()
                conn.close()
        else:
                messagebox.showerror("Missing Text Error", "Please ensure that there is data in all four fields.")


def onDelete(self):
        var_select = self.lst_List1.get(self.lst_List1.curselection())
        conn = sqlite3.connect('phonebook.db')
        with conn:
                cur = conn.cursor()
                cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
                count = cur.fetchone() [0]
                if count > 1:
                        confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenatly deleted from the database. \n\nProceed with deletion request?".format(var_select))
                        if confirm:
                                with conn:
                                        cur.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}' """.format(var_select))
                                onDeleted(self)
                                conn.commit()
                else:
                        confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add anotherrecord first before you can delete ({}).".format(var_select, var_select))
        conn.close()


def onDeleted(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_emaile.delete(0, END)
        try:
                index = self.lst_List1.curselection()[0]
                self.lst_list1.delete(index)
        except IndexError:
                pass


def onClear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_email.delete(0, END)


def onRefresh(self):
        #populate the list
        self.lst_List1.delete(0, END)
        conn = sqlite3.connect("phonebook.db")
        with conn:
                cur = conn.cursor()
                cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
                count = cur.fetchone() [0]
                i = 0
                while i < count:
                        cur.execute("""SELECT col_fullname FROM tbl_phonebook""")
                        varList = cur.fetchall()[i]
                        for item in varList:
                                self.lst_List1.insert(0, str(item))
                                i += 1
        conn.close()


def onUpdate(self):
        try:
                var_select = self.lst_List1.curselection() [0]
                var_value = self.lst_List1.get(var_select)
        except:
                messagebox.showinfo("Missing selection", "No name was selected from the list box. \nCancelling the Update request.")
                return
        var_phone = self.txt_phone.get().strip()
        var_email = self.txt.email.get().strip()
        if (len(var_phone) > 0) and (len(var_email)> 0):
                conn = sqlite3.connect('phonebook.db')
                with conn:
                        cur = conn.cursor()
                        cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}' """.format(var_phone))
                        count = cur.fetchone()[0]
                        print(count)
                        cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}' """.format(var_email))
                        count2 = cur.fetchone()[0]
                        print(count2)
                        if count ==0 or count2 == 0:
                                response = messagebox.askokcancel("Update Request", "The following changes ({}) and ({}) will not be implemented for ({}). \n\nProceed with the update request?".format(var_phone, var_email, var_value))
                                print(response)
                                if response:
                                        with conn:
                                                cursor = conn.cursor()
                                                cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}', col_email = '{1}', WHERE col_fullname = '{2}' """.format(var_phone, var_email, var_value))
                                                onClear(self)
                                                conn.commit()
                                else:
                                        messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
                        else:
                                messagebox.showinfo("No changes detected", "Both ({}) and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_phone, var_email))
                        onClear(self)
                conn.close()
        else:
                messagebox.showerror("Missing information",  "Please select a name from the list. \nThen edit the phone or email information.")
        onClear(self)



if __name__ =="__main__":
        pass

































        
