# Multithreading

# print("hello")


# print("om")

# print("rrrrrrrrrrrr")

import threading

class cls1:
    def car(self):
        for i in range(100):
            print("carrrrr")

class cls2:
    def bus(self):
        for i in range(100):
            print("busssss")

obj1 = cls1()
obj2 = cls2()

# obj1.car()
# obj2.bus()

th1 = threading.Thread(target = obj1.car)
th2 = threading.Thread(target = obj2.bus)

th1.start()
th2.start()

print("I am going to done")

print("The sum is : ", 12 + 10 )

th1.join()
print("Code finish")