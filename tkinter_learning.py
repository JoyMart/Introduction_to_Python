
#importing module
import tkinter
from tkinter import *


#blueprint to create window
class ParentWindow(Frame):
        def __init__ (self, master):
                Frame.__init__(self)
                
                self.master = master
                self.master.resizable(width  = True, height = True)
                self.master.geometry("700x400")
                self.master.title("Learning TkInter!")
                self.master.config(bg ="lightgrey")

                self.varFname = StringVar()
                self.varLname = StringVar()

#labeling first name box
                self.lblFname = Label(self.master, text = "First Name: ", font = ("Lexend Peta", 16), fg = "black", bg = "lightgrey")
                self.lblFname.grid(row = 0, column = 0, padx =(30, 0), pady =(30, 0) )
#labeling last name box
                self.lblFname = Label(self.master, text = "Last Name: ", font = ("Lexend Peta", 16), fg = "black", bg = "lightgrey")
                self.lblFname.grid(row = 1, column = 0, padx =(30, 0), pady =(30, 0))
                #displaying fname and lname
                self.lblDisplay =Label(self.master, text = "", font = ("Lexend Peta", 16), fg = "black", bg = "lightgrey")
                self.lblDisplay.grid(row = 3, column = 1, padx =(30, 0), pady =(30, 0))

                
#creating first name box
                self.txtFname = Entry(self.master, text = self.varFname, font = ("Lexend Peta", 16), fg = "black", bg = "lightblue")
                self.txtFname.grid(row =0, column =1, padx =(30, 0), pady =(30, 0))
#creating last name box
                self.txtLname = Entry(self.master, text = self.varLname, font = ("Lexend Peta", 16), fg = "black", bg = "lightblue")
                self.txtLname.grid(row =1, column =1, padx =(30, 0), pady =(30, 0))
                
#creating 2 buttons
                self.btnSubmit = Button(self.master, text = "Submit", width = 10, height = 2, command = self.submit)
                self.btnSubmit.grid(row =2, column =1, padx =(0, 0), pady =(30, 0), sticky = NE)
                
                self.btnCancel = Button(self.master, text = "Cancel", width = 10, height = 2, command = self.cancel)
                self.btnCancel.grid(row =2, column =1, padx =(0, 90), pady =(30, 0), sticky = NE)
                
        def submit(self):
                FN = self.varFname.get()
                LN = self.varLname.get()
                self.lblDisplay.config(text = "Hello, {} {}!".format(FN, LN))
                
        def cancel(self):
                self.master.destroy()
                
                

















if __name__ == "__main__":
        root = Tk()
        app = ParentWindow(root)
        root.mainloop()
        
