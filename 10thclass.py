# polymorphism:
# 1) operator overloading
# 2) Method overloading
# 3) Method overrring
# 4) Duck typing

10 + 20


# operands = 10, 20

# operator = +

# +




class abc:
    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y

    def mysum(self):
        print("i am nothing")
        
    def __add__(uuu, other):
        var1 = uuu.num1 + other.num1
        var2 = uuu.num2 + other.num2
        summ = abc(var1, var2)
        return summ
        

obj1 = abc(12, 10)

obj2 = abc(2, 6)

sumr = obj1 + obj2

print(sumr.num2)








# 2) Method overloading:
# python do not support method overloadding

class uio:
    def abc(self, a=None, b=None, c=None):
        
        if a != None and b != None and c != None:
            usm = a + b +c
            print(usm)
        
        elif a != None and b != None:
            usm = a + b
            print(usm)
        
        elif a != None:
            print(a)
        
obj = uio()

obj.abc(100, 23, 34)



