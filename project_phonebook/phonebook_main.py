#Python Var:        3.8.5 
#
#
#Author:                Joy Mart
#Title:                     Joy's Phonebook
#
#Purpose:              Creating phonebook gui, Tkinter module, 
#                               using parent child relationships
#
#Tested OS:           Windows 10


from tkinter import *
import tkinter as tk

import phonebook_gui
import phonebook_func

#Frame is the Tkinter class that our own class will inherit from
class ParentWindow(Frame):
        def __init__ (self, master, *args, **kwargs):
                Frame.__init__(self, master, *args, **kwargs)

                #define master frame config
                self.master = master
                self.master.minsize(500, 300)
                self.master.maxsize(500, 300)
                #centering window on screen
                phonebook_func.center_window(self, 500, 300)
                self.master.title("Joy's Phonebook")
                self.master.config(bg = "#a2ac94")
                #user clicks the upper corner "x" on windows OS
                self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
                arg = self.master

                #load in the GUI widgets from a separate module,
                #keeping your code compartementalized and clutter free
                phonebook_gui.load_gui(self)
        





if __name__ == "__main__":
        root = tk.Tk()
        App = ParentWindow(root)
        root.mainloop()
