#
#
#               UI for automated file transfer
#               see file: transferFilesEvery24hrs.py
#
#
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
import os, time
import datetime
import datetime as dt
import shutil




class GuiWindow(Frame):
        def __init__(self, master, *args):
                Frame.__init__(self, master, *args)

                self.master = master
                self.master.minsize(500, 300)
                self.master.maxsize(500, 300)
                self.master.title("File Transfer Interface")
                self.master.config(bg = "#FF9AA2")

                
                self.btn_browse1 = tk.Button(self.master,  width = 15, height = 2, text = "Origin Folder: ", bg = "#FFDAC1", fg = "black", command = lambda: self.browse1())
                self.btn_browse1.grid(row = 0, column = 0, padx =(25, 0), pady =(10, 0), sticky = N+W)
                self.btn_browse2 = tk.Button(self.master, width = 15, height = 2, text = "Destination Folder: ", bg = "#FFDAC1", fg = "black", command = lambda: self.browse2())
                self.btn_browse2.grid(row = 2, column = 0, padx =(25, 0), pady =(10, 0), sticky = N+W)
                
                
                self.btn_transfer = tk.Button(self.master,  width = 10, height = 2, text = "Transfer Files", bg = "#FFDAC1", command = lambda: self.Transfer())
                self.btn_transfer.grid(row =3, column =1,  padx=(30, 40), pady=(0, 0), sticky= NW)

        def browse1(self):
                self.master.browse1 = askdirectory()
                print(self.master.browse1)
                
        def browse2(self):
                self.master.browse2 = askdirectory()
                print(self.master.browse2)
        

        def Transfer(self):
                now = dt.datetime.now()
                last24 = now-dt.timedelta(hours = 24)
                strftime = "%H:%M %m/%d/%Y"
                for root, dirs, files in os.walk(self.master.browse1):
                        for fname in files:
                                path = os.path.join(root, fname)
                                st = os.stat(path)
                                mtime = dt.datetime.fromtimestamp(st.st_mtime)
                                if mtime > last24:
                                        print("True: ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
                                        shutil.move(path, self.master.browse2)
                                else:
                                        print (False)


if __name__ == "__main__":
        root = tk.Tk()
        App = GuiWindow(root)
        root.mainloop()
