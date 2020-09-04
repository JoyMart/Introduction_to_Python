#Python Var:        3.8.5 
#
#
#Author:                Joy Mart
#Title:                     Student Tracking
#
#Purpose:              Creating student tracker gui, Tkinter module, 
#                               using parent child relationships
#
#Tested OS:           Windows 10

import tkinter as tk
from tkinter import *
import tracker_gui
import tracker_func

class TrackerWindow(Frame):
        def __init__(self, master, *args, **kwargs):
                Frame.__init__(self, master, *args, **kwargs)

                self.master = master
                self.master.minsize(500, 300)
                self.master.maxsize(700, 500)
                tracker_func.center_window(self, 500, 300)
                self.master.title("Student Tracker")
                self.master.config(bg = "#857777")
                self.master.protocol("WM_DELETE_WINDOW", lambda: tracker_func.ask_quit(self))
                arg = self.master
                tracker_gui.load_gui(self)



if __name__ =="__main__":
        root = tk.Tk()
        App = TrackerWindow(root)
        root.mainloop()
