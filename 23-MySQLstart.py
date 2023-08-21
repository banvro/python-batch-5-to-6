# MYSQL : sql

# 1) DDL (Data Defination Language)
# 2) DCL  (Data Control Language)
# 3) DML  (Data Manupulation language)
# 4) TCL  (Transmission Control language)

import mysql.connector

conn = mysql.connector.connect(host = "localhost", user = "root", password = "abc@123", database = "hello", auth_plugin='mysql_native_password')

# if conn.is_connected():
#     print("Database connected")


cruser = conn.cursor()

# cruser.execute('insert into employee values(3, "xyz", "yzx", 4000);')
# cruser.execute('insert into employee values(4, "abc", "cba", 5000);')

# cruser.commit()

# cruser.execute('select * from employee;')
cruser.execute('select * from employee where enployee_id = 3;')

fetahthis = cruser.fetchall()

# print(fetahthis)

for i in fetahthis:
    print(i)
conn.commit()








# mysql aLL used commands:


# use hello;

# create table employee(enployee_id INT, first_name varchar(40), last_name varchar(30), salary decimal);

# insert into employee values(1, "Kriss", "Moris", 20000);

# show tables;

# select * from employee;
