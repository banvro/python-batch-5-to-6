# Veriables : to store some data we are using variables...

# a = 10
# b = 20
# c = 10

# Rules to define a variables:
# 1) Varibles always start from characters or underscore..
# 2) Variables never start from degi
# tes or any spacil symbols/
# 3) Varible can not define after a space..

# abc12 = 20

# print("Hello words")
# print("zjhvcjshdvfjhsdfvj")

# a = 10
# b = 20

# print(a + b)

# data type:

# 1) Integer  => 1, 2, 3, 4, -12, 232, 234, 324, 
# 2) Flot  ==>  1.5, 10.6, 9.10
# 3) String ==> "asdhvaskad18723871238112..123123.123"
# 4) Boolean  ==> True,  False
# 5) Complex = > i + j


# abc = True
# # type()
# print(type(abc))

# 1) print()
# 2) input()

# 1) print() : to print someting on console..

# a = 10
# print("yyyyyyyyyyy", a)


# a = 1
# b = 5

# c = a + b

# print("the sum is : ", c)


# 2) input function => use to get imput from user....

# addation of two numbers

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter secondd number : "))

# sum = num1 + num2


# print("The sum is : ", sum)


# comments: => are use to increse the code readability...


# 1) Single line comment

# kjbskjsdbfjsdkf  skdjfbdsk fsdkf jsdf 

# 2) Multiline comment...

"""
    skdjbfksdbfdsf
    sdjfbsdkjbfkdsf
    sdjfbsdkfbsdf
    sdfjbskfbksdbfds
"""

# print("hlooooooo")


















# calculator: basic using if else

print("******************Calculater**************")

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("""
      ......PLease choose any of one........
    1) Adation
    2) Substraction
    3) Multiplication 
    4) Devsion
""")
      
choce = input("Enter what you want to do : ")
# 3
# "3" == "1"
if choce == "1":
    sum = num1 + num2
    print("the sum is : ", sum)

elif choce == "2":
    sub = num1 - num2
    print("The substraction is : ", sub)


elif choce == "3":
    mul = num1 * num2
    print("The multiplication is : ", mul)


elif choce == "4":
    div = num1 / num2
    print("The devsion is : ", div)

else:
    print("Something went wrong..")
