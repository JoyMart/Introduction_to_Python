

#       Python:       3.8.5
#
#       Author(s):      Joy Mart
#               
#       Purpose:        makes a game
#                               passes varables from func to func
#
#
#

def start(nice=0, mean=0, name=""):
        # get user's name
        name = describe_game (name)
        nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
        """check if this is a new game or not
        if it isnew, get the user's name
        if it is not a new game, thank the player for
        playing again and continue the game"""
        #meaning is this a new player or returning player
        if name!= "":
                print("\n Thank you for playing again,  {}!".format(name))
        else:
                stop = True
                while stop:
                        name = input("\n What is your Name? \n >>>").capitalize()
                        if name != "":
                                print("\n Welcome, {}".format(name))
                                print("\n In this game, you will be greeted \n by several different people. \n You can choose to be nice or mean.")
                                print("\n However, at the end of the game your fate \n will be sealed by your actions.")
                                stop = False
        return name



def nice_mean(nice, mean, name):
        stop = True
        while stop:
                show_score(nice, mean, name)
                pick = input("\n A stranger approaches you for a \nconversation. Will you be nice \nor mean (N/M) \n>>>").lower()
                if pick =="n":
                        print("\n The stranger walks away smiling...")
                        nice = (nice +1)
                        stop = False
                if pick == "m":
                        print("\nThe stranger glares at you \nmenacingly and storms off...")
                        mean = (mean + 1)
                        stop = False
        score(nice, mean, name) #passing the 3 var to the score()


def show_score(nice, mean, name):
        print("\n{}, your current total: \n({}, nice) and ({}, mean)".format(name, nice, mean))


def score(nice, mean, name):
        # score func is being passed the values stored within the 3 vars
        if nice>2: # if condition is valid, call win function passing in the variables so it can use them
                win(nice, mean, name)
        if mean > 2: # if condition is valid, call win function passing in the variables so it can use them
                lose(nice, mean, name)
        else:                   #else, call nice_mean func passing in the var so it can use them
                nice_mean(nice, mean, name)

def win(nice, mean, name):
        #Substitute the {} wildcards with our var values
        print("\nNice job {}, you win! \nEveryone loves you and you've \nmade friends along the way!".format(name))
        #call again func and pass in our vars
        again(nice, mean, name)

def lose(nice, mean, name):
        #Substitute the {} wildcards with our var values
        print("\nAHHHHH too bad, game over! \n{}, you live in a dirty, beat-up \nvan by the river; wretched and alone!".format(name))
        #call again func and pass in our vars
        again(nice, mean, name)



def again(nice, mean, name):
        stop=True
        while stop:
                choice = input("\nDo you want to play again? (y/n): \n>>>".lower())
                if choice == "y":
                        stop = False
                        reset(nice, mean, name)
                if choice == "n":
                        print("\nOh so sad, sorry to see you go! ")
                        stop = False
                        quit()
                else:
                        print('\nEnter ( Y ) for "yes'", ( N ) for \"no\": \n>>>")
                               
                
def reset(nice, mean, name):
        nice = 0
        mean = 0
        # I don't call the name because the same user selected to play again
        start(nice, mean, name)
        




















if __name__ == "__main__":
        start()
