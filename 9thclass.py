# 1) Inharitance
# 2) Polymorphism
# 3) Encapsulaton
# 4) Abstraction
# from abc import ABC, abstractmethod

# class Person(ABC):
#     def __init__(self):
#         self.name = "kriss"
#         self.age = 12
        
#     def mthd1(self):
#         print("this is mthd1 class.")

#     @abstractmethod
#     def security(self):
#         pass

# class Human(Person):
#     def __init__(self):
#         pass
    
#     def mthd2(self):
#         print("this is seond method..")
    
#     def security(self):
#         print("alright")

# obj1 = Human()

# obj1.mthd1()



# Encapsulaton:
#  is a combnation of abstraction or datahiding

# class Person(ABC):
#     def __init__(self):
#         self.name = "kriss"
#         self.age = 12




# class Person:
#     def __init__(self):
#         self.name = "kriss"
#         self.__age = 12
#     def car(self):
#         print("aaaaaaaaaaaaaaaa")

# obj = Person()

# obj.car()

# print(obj.name)
# print(obj.age)


# a = 10
# b = 20

# print(a + b)

# 10 + 20




# Polymorphsim:
    
# ploy = many
# morphism = form

# 1) Opertor overloaing
# 2) Method Overloading
# 3) Method Overridding....

# a + b

# a, b = opernds
# + = operator

# 10 + 20

class Xyz:
    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y
    
    def alright(self):
        print("i am outpiut")
    
    def __add__(hg, ac):
        m1 = hg.num1 + ac.num1
        m2 = hg.num2 + ac.num2
        sum = Xyz(m1, m2)
        return sum

obj = Xyz(12, 10)
obj1 = Xyz(10, 20)

# print(obj)
# print(obj + obj1)
zx = obj1 + obj

print(zx.num2)







