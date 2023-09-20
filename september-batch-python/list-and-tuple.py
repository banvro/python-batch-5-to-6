# spcial data types : 
# a = 10
# 1) List
# ordered, allow duplicasy, mutable (changeable)

# 2) Tuple
# ordered, allow duplicate values, imutable

# 3) Set
# unordered, do not allow duplicasy, mutable


# 4) Dictionry
# orered, do not allow duplicaasy, mutable

# to collect mutipal data in a single variable
# List : 
# []
# ordered, allow duplicasy, mutable (changeable)

# lst = [12, 100, 89, 67, "hello", 100.9, 89]
# print(lst, type(lst))

# print(lst[1])
# print(lst[-2])


# slicing :
# lst = [12, 100, 89, 67, "hello", 100.9, 89, 12]
# print(lst)
# [start : end : increanet]
# print(lst[1 : 5 : 2])

# print(lst[-1 : -3])

# print(lst[-2 : ])

# print(lst[: : -1])



# Mutable : 

# lst = [12, 100, 89, 67, "hello", 100.9, 89]

# to add data
# 1) append()
# 2) insert()

# lst.append(2000)
# lst.append(300)

# lst.insert(1, 5000)

# print(lst)



# lst = [12, 100, 89, 67, "hello", 100.9, 89]

# to delete data
# 1) pop()
# 2) remove()

# lst.pop()
# lst.remove(100)
# lst.remove(67)

# print(lst[3])

# lst.remove(lst[3])
# lst.clear()



# print(lst)



# 2) Tuple
# ordered, allow duplicate values, imutable
# ()

# tpl = (100, 100, 89, "hello", "car", 190.0)
# # print(tpl, type(tpl))

# print(tpl[3])

# print(tpl[1 : 4])

# Type Casting : 


# a = 10
# print(a, type(a))

# b = float(a)
# print(b, type(b))


# tpl = (100, 100, 89, "hello", "car", 190.0)
# print(tpl)

# lst = list(tpl)
# lst.append(2000)
# print(lst)

# x = tuple(lst)

# print(x)