
#
#               Gui to browse for files
#
#
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
import os




class MainWindow(Frame):
        def __init__(self, master):
                Frame.__init__(self)

                self.master = master
                self.master.resizable(width  = True, height = True)
                self.master.geometry("500x200")
                self.master.title("Check Files")
                self.master.config(bg ="#ECECEC")
                
                self.dirPath = StringVar()

#creating  buttons
                self.btnBrowse1 = Button(self.master, text = "Browse", width = 15, height = 1, command=lambda: self.browse())
                self.btnBrowse1.grid(row =1, column =0, padx =(15, 0), pady =(40, 0), sticky = NW)
                self.txtBrowse1 = Entry(self.master, text = self.dirPath, font = ("Lexend Peta", 10), fg = "black", bg = "white", width = 40)
                self.txtBrowse1.grid(row =1, column =2, padx =(30, 0), pady =(40, 0))

                self.btnBrowse2 = Button(self.master, text = "Browse", width = 15, height = 1, command=lambda: self.browse())
                self.btnBrowse2.grid(row =2, column =0, padx =(15, 0), pady =(10, 0), sticky = NW)              
                self.txtBrowse2 = Entry(self.master, text = self.dirPath, font = ("Lexend Peta", 10), fg = "black", bg = "white", width = 40)
                self.txtBrowse2.gid(row =2, column =2, padx =(30, 0), pady =(10, 0))


                self.btnCheck = Button(self.master, text = "Check for files...", width = 15, height = 2)
                self.btnCheck.grid(row = 3, column = 0, rowspan = 2, columnspan = 1, padx = (15, 0), pady = (10, 0), sticky = SW)
                
                self.btnClose = Button(self.master, text = "Close Program", width = 15, height = 2)
                self.btnClose.grid(row = 3, column = 2, padx = (15, 0), pady = (10, 0), sticky = SE)
                

                
        def browse(self):
                file = fd.askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
                if file is not None: 
                        content = file.read() 
                        print(content) 
                
                
                



if __name__ == "__main__":
        root = Tk()
        app = MainWindow(root)
        root.mainloop()
