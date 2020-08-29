

mySentence = "loves the color"
colorList = ["red", "blue", "black", "purple", "yellow"]

def color_func(name):
        lst = [ ]
        for i in colorList:
                msg = "{} {} {}".format(name, mySentence, i)
                lst.append(msg)
        return lst

def get_name():
        go = True
        while go:
                name = input ("What is your name?  ")
                if name == "":
                        print("You must provide a name")
                elif name == "Sally":
                        print("Sally you may not use this software.")
                else:
                        go = False
        lst = color_func(name)
        for i in lst:
                print(i)


get_name()



        
