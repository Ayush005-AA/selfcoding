# fi = open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\pop.txt","x")
# print("file created")

# fi = open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\pop.txt","w")
# fi.write("my name is aayush \n i am from himchal pardesh\n i love cricket")
# print("write sucessfully")


# fi = open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\pop.txt","r")
# print(fi.read())
# try:
#     with open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\pop.txt") as fi2:
#         with open("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\hot.txt","w") as fi3:
#             for i in fi2:
#                 fi3.write(i)
#                 print("file will be created")


# except:
#     print(" file do not created")

# import os
# os.remove("C:\\Users\\Ayush Dhiman\\OneDrive\\Desktop\\python\hot.txt")

# print("file delted")

                
# import calendar
# year = 2023
# month = 8
# x = calendar.month(year,month)
# print(x)


# a = 1243
# i = 0
# for i in a:
#     i = i+a
#     print(i)

# a =10
# b = 0
# c = ""

# try:
#     c = a/b

# except:
#     print("not a valid")

# print(c)
# print("continue")
# print("exit ")

# import tkinter as tk

# app = tk.Tk()

# app.geometry("400x400")
# # grid
# labl = tk.Label(app, text = "this is my text")
# labl.grid(row=0, column=0, padx=20)

# btn = tk.Button(app, text = "subit")
# btn.grid(row=1, column=0)


# help("keywords")

# x,y = "12"
# y,z = "34"
# print(x,y,z)

# print(x+y+z)


# a = [1,2,3]

# a.insert(8,6)
# print(a)


# for x in range(0.5, 5.5, 0.5):
#   print(x)


# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append( 2"Scott")
# print(sampleList)

# valueOne = 5 ** 2
# valueTwo = 5 ** 3

# print(valueOne)
# print(valueTwo)

# var= "James Bond"
# print(var[2::-1])

# var = "James" * 1  * 6
# print(var)
# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]

# print(listOne == listTwo)
# print(listOne is listTwo)


# pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
# pat.sort()
# print(pat)

# for p in pat:
# #    pass
#    if (p == 0):
#        current = p
#        break
#    elif (p % 2 == 0):
#        continue
#    print(p)    # output => 1 3 1 3 1
# print(current)    # output => 0



# class a:
    # def mtd(self):
        # print("i am a mtd")

#     def mtd1(self):
#         print("i am a mtd1")

#     @staticmethod
#     def mtd2():
#         print("i am a mtd2")

# obj = a()
# obj.mtd2()
# a.mtd2()


# a,b = "12"
# b,n = "10"
# print(a+b+n)


# x = y = 5,10
# a = x == y
# print(a)


# def con(data):
#     if all(data):
#         return "yes"
#     elif not all(data):
#         return "no"
#     else:
#         return "nooo"
    
# Value = [True,False,True,False]
# print(con(Value))

# a = {"a":1,"b":2,"c":3}
# print(a["a"])
# print(a.items()[1])

# print(all([]))
# print(any([]))

# l = ["a","b","c","d"]
# b = "".join(l)
# print(type(b),b)

# a = [2,2,2,5,63,5,2,5,5,5,5,5,5,5]
# b = max(a,key=a.count)
# print(b)

# l = [1,2]
# l.extend([3])
# a,b,c= l
# print(a,b,c)


# for i in range(0,7):
#     print(i)

# 6 5 4
# _ 3 2
# _ _ 1


# n = 6

# for i in range(n):
#     # print(i)
#     for j in range(i):
#         print("_",end="")
#         # print(j)
#     for k in range(n, i, -1):
        
#         print(k - i,end="")
#     print()


# class Test:
#     def __init__(self):
#         print("1")


#     def __init__(self):
#         print("2")


# obj = Test()

# d = {1:2,3:6}
# for i ,j in d.items():
#     print(i,j,sep=":")

# def fun(nun):
#     def fun1():
#         print("start function")

#         nun()
#         print("end function")

#     return fun1


# def fun2():
#     print(10+2)


# fun2 = fun(fun2)
# fun2()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            



# def fun(nun):
#     def fun1():
#         print("start function")

#         nun()
#         print("end function")

#     return fun1

# @fun
# def fun2():
#     print(10+2)

# fun2()


# print(type(range(5)))



# def o():
    
#     x = 10

#     return x

# o()
# print(x)


# print(bool(0), bool(32131), bool(2121321), bool(0))


# print(type(FFx0), type(FFx1), type(FFx2), type()

# str1 = 'str1'

# print(str1)

# x = 10

# def o():
#     global x

#     x = 20


# o()


# print(x)    

# print("print")

# def mtd(x = 1 , y = 2):
#     x = x + y
#     print(x)
#     y += 1
#     # print(y)
#     print(x,y)


# mtd()


def gen(n):
    for i in range(n):
        yield i


obj = gen(10)
for j in obj:
    print(j)

# a = [1,2,3,4,5]
# b = a.index(3)
# print(b)


# python code to demonstrate working of reduce() 

# importing functools for reduce() 
# import functools 

# # initializing list 
# lis = [1, 3, 5, 6, 2] 

# # using reduce to compute sum of list 
# # print("The sum of the list elements is : ", end="") 
# print(functools.reduce(lambda a, b: a+b, lis)) 

# using reduce to compute maximum element from list 
# print("The maximum element of the list is : ", end="") 
# print(functools.reduce(lambda a, b: a if a > b else b, lis)) 

# from functools import reduce
# # 
# a = [1,2,3,4,5,5]
# b = reduce(lambda a, b: a+b,a)
# print(f"the sum is {b}")


# from functools import reduce

# a = [i for i in range(1,11)if i % 2 == 0]
# b = reduce(lambda a,b: a+b,a)
# print(b)

# while True:
#     if 5 < 0:
#         print("The maximum element of the list is")
#     else:
#         print("hello")
























    


