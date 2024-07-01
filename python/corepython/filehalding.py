# fi = open('test.py',"r+")

# print(fi.read)
# print(fi.readline())
# print(fi.readline())
# print(fi.readline())

# fi = open('storedfile.py','w')
# fi.write("i am buy a new car")

#  ::::::::how to create new file:::::::::::

# fi = open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\ooi.txt","x")

# print("your file created sucessfully")


# fi = open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\ooi.txt","w")

# fi.write("hells sir\n my name is ayush")

# print("write succesfully")

# fi = open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\ooi.txt","r")

# print(fi.readline())
# print(fi.readline())

# try:
#     fi = open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\oob.txt","r")
#     print(fi.readlines())
   

# except:
#     print("file not avaible plz create first")

# else:
#     fi.close()
#     print("file closed")

# ::::::::::::::::::::data copy one file to another file::::::::::


# try:
#      with open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\ooi.txt") as fi2:
#         with open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\mmi.txt","w") as fi3:
#             for i in fi2:
#                 fi3.write(i)
   

# except:
#     print("fine not avaible plz create first")

# else:
#     fi2.close()
#     print("file closed")


# ::::::::::::how to delte file::::::::::::::.

# import os
# if os.path.exists("oii.txt"):
#     os.remove("oii.txt")

# else:
#     print("file del sucessfully")

# import os
# if os.path.exists("oii.txt"):
#     os.remove("oii.txt")

# else:
#     print("file not exits")

# file = open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\hope.txt","x")

# print("your file created sucessfully")

# file = open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\hope.txt","w")
# file.write("my name is ayush, \n i am from himachal pardesh\n i love playing cricket")

# print(f"write  sucessfully")


# import os

# os.remove("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\hope.txt")

# exception handeling

# print("i am strat")


# a = 10

# b = 3

# print(a / b)


# print("i am conitnue")

# print("i am end")




# try:
#     print("ok")
# except Exception:
#     pass
# finally:
#     pass



# print("i am start")

# a = 10

# b = 0

# print(a / b)


# print("i am conitnue")

# print("i am end")



# 1) Complile time error

# if 10 == 10:
#     print("ok")

# a = 1%


# 2) Logical error

# a = 12

# b = 0

# print(a/b)


# 3) Run time error

# a = int(input("Enter you number : "))






# print("i am start")

# a = 10

# b = 0


# try:
#     a = int(input("Enter you number : "))
#     # print(a / b)
# except ZeroDivisionError:
#     print("you cant devide zero to any number")

# except ValueError:
#     print("ENter valid phone number..")
    
# except Exception as e:
#     print(e)
    
    
# finally:
#     print("i am finnely")

# print("i am conitnue")

# print("i am end")

# # exception handeling

# print("i am strat")


# a = 10

# b = 0

# print(a / b)


# print("i am conitnue")

# print("i am end")




# try:
#     print("ok")
# except Exception:
#     pass
# finally:
#     pass



# print("i am start")

# a = 10

# b = 0

# print(a / b)


# print("i am conitnue")

# print("i am end")



# 1) Complile time error

# if 10 == 10:
#     print("ok")

# a = 1%


# 2) Logical error

# a = 12

# b = 0

# print(a/b)


# 3) Run time error

# a = int(input("Enter you number : "))






# print("i am start")

# a = 10

# b = 0


# try:
#     a = int(input("Enter you number : "))
#     # print(a / b)
# except ZeroDivisionError:
#     print("you cant devide zero to any number")

# except ValueError:
#     print("ENter valid phone number..")
    
# except Exception as e:
#     print(e)
    
    
# finally:
#     print("i am finnely")

# print("i am conitnue")

# print("i am end")
# a = 20
# b = 0
# c = a/b

# print(c)

# try:
#     print("ohkkkkkkk")
# except Exception:
#     pass

# print("code will be continue")




# print("code will be running")


# print("code will be end")

# print("code starting")
 
# a = 10
# b = 0


# print("code will be continue")

# try:
#     print(a/b)

# except :
#     print("not division by zero")

# print("code will be running")



# print("code will be end")


# :::::::::::exception handling:::::::::::::::::::::::::

# print("code will be started")

# a = int(input("enter a number"))
# b = int(input("enter second value"))


# try:
#     c = a/b
#     print(c)
  

# except:
#     print("cant't divide zero")

# else:
#     print("hiiiiiiiiiiiii")

# print("code will be run")


# print("code will be continue ")


# print("code end")

# f = open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\self.txt","x")
# print('file created sucessfully')


# a = 10
# b = 20
# c = a + b 

# v = str(c)

# f  = open("mmi.txt","w")
# f.write(f"the sum is :: {c}")
# print("sum sucessfully")


# how to read the file\\\\\\\\\\\\\\\ 

# f = open("self.txt","r")
# d = f.read()
# print(d)
# f.close()

# how to writing the file\\\\\\\\\\\

# f = open("self.txt","+")
# d = f.write("i am ayush\n i am  ")
# print(d)
# f.close()

# with open("self.txt","w") as f:
#    d = f.write("hy am ayush")
# print(d)
# print("write sucessfully")

# import os

# os.remove("mmi.txt")
# print("file removed sucessfully")

# a = ("abhay","ayush","Aman")
# b = list(a)

# b.append("Dhiman")
# a = tuple(b)
# print(a)

# a = input("Enter Password:")

# if a == 123456:
#     print("Welcome")
# elif a == "#$%^":
#     print("special characters not allowed") 
# else:
#     print("Fuck Off")    



