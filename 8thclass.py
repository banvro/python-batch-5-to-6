# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def body(self):
#         print("I am a body.!")

# class Man(Human):
#     def __init__(self, ego, name, age):
#         super().__init__(name, age)
#         self.ego = ego

#     def abc(self):
#         print("this is ok")

# obj = Man("None", "vishal", 12)
# obj.body()




# Abstraction: To hide the actual flow from the users...

from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def abc(self):
        pass

    def car(self):
        print("ok")

class Car(Person):
    def myname(self):
        print("uuuuuuuuuu")

    def abc(self):
        print("iiiiiiii")


obj = Car()

obj.myname()