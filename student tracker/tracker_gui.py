#
#               This is the gui part of my student tracker
#
#


import tkinter as tk
from tkinter import *

import tracker_main
import tracker_func

def load_gui(self):
        #student information labels
        self.lbl_fname = tk.Label(self.master, text = "First Name: ", bg = "#857777", fg = "#301a17")
        self.lbl_fname.grid(row =0, column = 0, padx = (10, 0), pady = (0, 0), sticky = N+W)
        self.lbl_lname = tk.Label(self.master, text = "Last Name: ", bg = "#857777", fg = "#301a17")
        self.lbl_lname.grid(row =2, column = 0, padx = (10, 0), pady = (0, 0),  sticky = N+W)
        self.lbl_phone = tk.Label(self.master, text = "Phone Number: ", bg = "#857777", fg = "#301a17")
        self.lbl_phone.grid(row =4, column = 0, padx = (10, 0), pady = (0, 0),  sticky = N+W)
        self.lbl_email = tk.Label(self.master, text = "Email: ", bg = "#857777", fg = "#301a17")
        self.lbl_email.grid(row =6, column = 0, padx = (10, 0), pady = (0, 0), sticky = N+W)
        self.lbl_course = tk.Label(self.master, text = "Course Name: ", bg = "#857777", fg = "#301a17")
        self.lbl_course.grid(row =8, column = 0, padx = (10, 0), pady = (0, 0),  sticky = N+W)
        #student info entry boxes
        self.txt_fname = tk.Entry(self.master, text = "", bg = "#a5af83")
        self.txt_fname.grid(row =1, column =0, rowspan =1, columnspan =2, padx=(15, 0), pady=(5, 5), sticky= N+E+W)
        self.txt_lname = tk.Entry(self.master, text = "", bg = "#a5af83")
        self.txt_lname.grid(row =3, column =0, rowspan =1, columnspan =2, padx=(15, 0), pady=(5, 5), sticky= N+E+W)
        self.txt_phone = tk.Entry(self.master, text = "", bg = "#a5af83")
        self.txt_phone.grid(row =5, column =0, rowspan =1, columnspan =2, padx=(15, 0), pady=(5, 5), sticky= N+E+W)
        self.txt_email = tk.Entry(self.master, text = "", bg = "#a5af83")
        self.txt_email.grid(row =7, column =0, rowspan =1, columnspan =2, padx=(15, 0), pady=(5, 5), sticky= N+E+W)
        self.txt_course = tk.Entry(self.master, text = "", bg = "#a5af83")
        self.txt_course.grid(row =9, column =0, rowspan =1, columnspan =2, padx=(15, 0), pady=(5, 5), sticky= N+E+W)
        #listbox
        self.scrollbar = Scrollbar(self.master, orient = VERTICAL)
        self.lst_1 = Listbox(self.master, yscrollcommand = self.scrollbar.set, bg = "#a5af83")
        self.lst_1.bind('<<ListboxSelector>>', lambda event: tracker_func.onSelect(self, event))
        self.scrollbar.config(command=self.lst_1.yview)
        self.scrollbar.grid(row = 1, column = 7, rowspan = 7, columnspan = 1, sticky = N+E)
        self.lst_1.grid(row = 1, column = 3, rowspan = 7, columnspan = 4, padx = (10, 0), sticky = N+E)
        #buttons
        self.btn_add = tk.Button(self.master, width = 10, height = 2, bg = "#968e77", text ="Add", command = lambda: tracker_func.addToList(self))
        self.btn_add.grid(row = 10, column = 0, padx = (20, 0), pady =(5, 0), sticky = W)
        self.btn_update = tk.Button(self.master, width = 10, height = 2, bg = "#968e77", text ="Update", command = lambda: tracker_func.onUpdate(self))
        self.btn_update.grid(row = 10, column = 1, padx = (10, 0), pady =(5, 0), sticky = W)
        self.btn_delete = tk.Button(self.master, width = 10, height = 2, bg = "#968e77", text ="Delete", command = lambda: tracker_func.onDelete(self))
        self.btn_delete.grid(row = 10, column = 6, padx = (0, 10), pady =(5, 0), sticky = E)
        #refference db and refresh fields
        tracker_func.create_db(self)
        tracker_func.onRefresh(self)


if __name__ == "__main__":
        pass

























        
        
