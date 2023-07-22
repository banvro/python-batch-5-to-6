                # Python Functions:

# functions are used for code optimization,
    
# code optimization : reduse the size of code...

# def = define

# def abc()

# int main(){
#     kjsbfkbajs
#     alsdjnadja
#     ajsdasbdkasdbj
#     aksdbaskdbksabdksakdsak

# }

# print()
# input()

# def abc():
#     print("hhhhhhhhhhhhhhhhhhhhh")


# abc()

# abc()


# perameters

# def sum(a, b):
#     print("1st value",a)
#     print("2st value",b)
#     c = a + b
#     print("he sum is : ", c)

# # arguments

# sum(b = 6, a = 10)




# def sum(a, b):
#     thesum = a + b
#     print("the sum is : ", thesum)


# num1 = int(input("ENter first number : "))
# num2 = int(input("ENter second number : "))


# sum(num1, num2)


# *args

# def mutisum(*args):
#     total = 0
#     for i in args:
#         total = total + i
    
#     print(total)


# mutisum(1, 2, 3 ,4 ,5 ,6 ,7,1000)

def sum(*args):
    total = 0
    for i in args:
        total = total + i
    return total

num = int(input("enter number you want to oprate : "))

inp = [int(input("enter number : ")) for i in range(num)]

xyz = sum(*inp)


print("teh sum is : ", xyz)
