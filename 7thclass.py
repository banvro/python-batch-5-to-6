# OOPs = > Object Oriented Programming
# its an relations between classes and objects...

# Clase :=> A blueprint of an object..
# object : are instance of a class

# class Person:
#     def employ(self):
#         print("Hello world/...!")
    
#     def abc(self):
#         print("uuuuuuuuuuuuuuuu")


# obj = Person()   # create an object for Person class

# obj.employ()

# obj.abc()

# class Humam:
#     name = "Vishal"
#     age = 12
    
#     def hlo(self):
#         print(f"{self.name} have the {self.age} age.")

# abc = Humam()
# abc.hlo()

# self is used for rafrencing...

# Constructer: when we crate object of a class, then constructer of that class automaticlly call.
    
#     __init__

class Human:
    def __init__(self, n, a):
        print("xyyyyyyyyyyyyyyzzzzzzzzzzz")
        self.name = n
        self.age = a
        
    def User(self):
        print(f"{self.name} have the {self.age} age.")
        
obj = Human("ayush", 20)
obj1 = Human("Kristina", 19)
obj2 = Human("yxz", 10)

# obj.User()
# # obj1.User()

# 1) Inharitance: child class  get some properties from their parent class.


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         # self.age = age

#     def hlo(self):
#         print("Heyy..! How are you...")

# class Employe(Person):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def tech(self):
#         print(f"{self.name} is a good person")

# obj1 = Person("vishal")

# obj2 = Employe("hlo")

# class Person:
#     def __init__(self, name):
#         self.name = name
        
#     def hlo(self):
#         print("ok")
        
# class Human(Person):
#     def __init__(self, car, name):
#         super().__init__(name)
#         self.car = car
        
#     def hlo(self):
#         print(f"{self.name} is your name")

# obj = Person("vishal")

# obj1 = Human("xxx", "kriss")

# obj1.hlo()








