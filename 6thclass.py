def sum(*args):
    total = 0
    for i in args:
        total = total + i
    
    return total

def subtraction(*args):
    total = 0
    for i in args:
        total = total - i
    
    return total

def multi(*args):
    total = 1
    for i in args:
        total = total * i
    
    return total


def devsion(*args):
    total = 0
    for i in args:
        total = total/ i
    return total


while True:
    wish = input("Press s to start or q to stop : ")

    if wish == "q":
        break

    print(":::::::Calculator:::::::::")

    usewaunt = int(input("How many numbers want to Enter : "))

    nums = [int(input("Enter number : ")) for i in range(usewaunt)]

    print("""
        **** Enter what you wish to do ****
        1) Adation
        2) Sustraction
        3) Multiplication
        4) Devsion 
    """)
        
    choice = input("Enter What to want : ")

    if choice == "1":
        xyz = sum(*nums)
        print("The output is : ", xyz)

    elif choice == "2":
        xyz = subtraction(*nums)
        print("The output is : ", xyz)

    elif choice == "3":
        xyz = multi(*nums)
        print("The output is : ", xyz)

    elif choice == "4":
        xyz = devsion(*nums)
        print("The output is : ", xyz)

    else:
        print("Somthing went wrong....")