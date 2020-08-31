


#create parent class with a method
class Pizza:
        crust = "unknown"
        sauce = "unknown"
        cheese = "mozerella"
        toppings = "unknown"
        name = "unknown"

        def creation(self):
                msg = "This pizza comes with a delicious {} crust, \na layer of {} sauce, and fresh {}. \nTopped with {}, \nits certain to be a hit at any party!\n".format(self.crust, self.sauce, self.cheese, self.toppings)
                return msg


#create child class that inherits with polymorphism method, changes pizza ingredients, calls creation func
class Pepperoni(Pizza):
        crust = "stuffed"
        sauce = "italian tomato"
        toppings = "pepperoni"
        name = "Popular Pepperoni Pizza:"

        def creation(self):
                msg = Pizza.creation(self) + "\nSo why not order one today?\n\n"
                return msg






#create another child class that inherits polymorphism method
class Hawaiian(Pizza):
        crust = "thin"
        sauce = "lite tomato"
        toppings = "ham, pinapple, and bacon"
        name = "Maui-Good Pizza:"

        def creation(self):
                msg = Pizza.creation(self) +"\nWhy not throw yourself a pizza-luau?\n\n"
                return msg






if __name__ =="__main__":
        pep = Pepperoni()
        haw = Hawaiian()
        piz = Pizza()
        print(piz.creation())
        print(pep.name)
        print(pep.creation())
        print(haw.name)
        print(haw.creation())





























        
        
