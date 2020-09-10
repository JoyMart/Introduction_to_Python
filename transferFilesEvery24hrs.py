#
#
#               copying files that have been edited in the last 24 hrs
#               to a new folder, every 24 hrs 
#               to send to HomeOffice computer
#
#
#
import os, time
import datetime
import shutil
import datetime as dt



def Transfer(self):
        now = dt.datetime.now()
        last24 = now-dt.timedelta(hours = 24)
        strftime = "%H:%M %m/%d/%Y"
        origin = 'C:\\Python\\File_transfer\\CustomerOrders\\'
        destination = 'C:\\Python\\File_transfer\\Destination_sendHomeOffice\\'
        for root, dirs, files in os.walk(origin):
                for fname in files:
                        path = os.path.join(root, fname)
                        st = os.stat(path)
                        mtime = dt.datetime.fromtimestamp(st.st_mtime)
                        if mtime > last24:
                                print("True: ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
                                shutil.move(path, destination)
                        else:
                                print (False)

                
