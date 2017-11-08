'''
Inheritance and Method Overriding


'''



class ParentPerson():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name :" + self.last_name)
        print("Eye Color :" + self.eye_color)



class Child(ParentPerson):
    def __init__(self, number_of_toys,last_name, eye_color):
        print ("Child Constructor Called")
        ParentPerson.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys


    def show_info(self):
        print (self.number_of_toys, self.last_name, self.eye_color)

bobby_newark = Child(5,"Newark","blue")
bobby_newark.show_info()

#print bobby_newark.last_name

