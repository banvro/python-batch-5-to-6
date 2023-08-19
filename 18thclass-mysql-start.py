
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

cruser.execute('create database newmydb')



