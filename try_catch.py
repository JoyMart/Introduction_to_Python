

def get_Info():
        var1 = input("Please provide the first numeric value: ")
        var2 = input("Please provide the second numeric value: ")
        return (var1, var2)
        


def compute():
        go = True
        while go:
                var1, var2 = get_Info()
                try:
                        var3 = int(var1) + int(var2)
                        go = False
                except ValueError as e:
                        print("{}:  \n You did not provide a numeric value".format(e) )
                except:
                        print("Oops! You entered an invalid input. Program will now close")
        print("{} + {} + {}".format(var1, var2, var3))


compute()
