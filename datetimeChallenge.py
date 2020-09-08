
import datetime
from pytz import timezone
import pytz
import time



utc = pytz.utc
utc.zone
fmt = "%H:%M"


Open = datetime.time(9, 0, 0).strftime(fmt)
Close = datetime.time(17, 0, 0).strftime(fmt)


PortlandHQ = datetime.datetime.now(pytz.timezone('US/Pacific'))
print(PortlandHQ.strftime(fmt))

NYCbranch = datetime.datetime.now(pytz.timezone('US/Eastern'))
print(NYCbranch.strftime(fmt))

LondonBranch = datetime.datetime.now(pytz.timezone('Europe/London'))
print(LondonBranch.strftime(fmt))

#time in Portland
timeHQ= PortlandHQ.strftime(fmt)
if timeHQ  > Open and timeHQ < Close:
        print("The Portland branch is open!\n")
else:
        print("I am sorry, but the Portland branch is currently closed. \nPlease check back at another time!\n")
        


#time in NYC
timeNYC= NYCbranch.strftime(fmt)
if  timeNYC > Open and timeNYC < Close:
        print("The NYC branch is open!\n")
else:
        print("I am sorry, but the NYC branch is currently closed. \nPlease check back at another time!\n")



#time in Portland
timeLON=LondonBranch.strftime(fmt)
if  timeLON  > Open and timeLON < Close:
        print("The London branch is open!\n")
else:
        print("I am sorry, but the London branch is currently closed. \nPlease check back at another time!\n")
