# # functions: function is a block of code.
# # use to optimize the code: (reduse the size of code)


# # type of function:
# # 1) predefine
# # print()
# # input()
# # sum()'
# # '

# # 2) manually created function

# # decleration of function::::::
# def abc():
#     print("this is a function dagta....")


# # # call a function 

# # abc()


# # abc()


# # abc()


# # # perameters or arguments:::
# # # arguments
# def summ(a, b):
#     c = a + b
#     print("sum is : ", c)



# # # call a function::::::::::
# # # perametersd::::
# summ(12, 10)


# summ(1, 2)
# hey

# l =[3,8,4,2,3,1,10,6,11,15,14] 

# # print(l.__len__())

# for i in range(0,len(l)):
#     for x in range(i+1,len(l)):
#         # print(x)

#         if l[i] >= l[x]:
#             l[i],l[x] = l[x],l[i]
# print(l)
        
            

# def factorial(n):
#     if n == 0 or n == 1:            
#         return 1
#     else:
#         return n * factorial(n - 1)

# number = int(input("Enter a Number: "))
# result = factorial(number)
# print(f"The factorial of {number} is: {result}")

# n = int(input("Enter a number::" ))

# def fac(n):

#     if  n == 1:
#         return 1 
    
#     else:
#         return n * fac(n-1)

# print(fac(1))
# print(f"output is ::{fac(n)}")



# def f(n):
#     if n ==1: return 1
#     return n*f(n-1)

# print(f(4))

# def greet(px):
#     def ner():
#         print("Welcome")
#         px()
#         print("see you later.")

#     return ner

# @greet
# def home():
#     print("Home")

# home()
    
# def decortaer(inpt):
#     def inerfunction(a,b):
#         print("welcome")
#         inpt(a,b)
#         print("thanks")

#     return inerfunction

# @decortaer
# def main(a,b):
#     print(a+b)

# main(10,20)

# a = "I Love India"


# print(a[::-1])



# n = int(input("Enter a number.."))

# def fun(n):
#     if n == 1:
#         return 1
        
#     else:
#         return n*fun(n-1)



# print(fun(n))








# def ourcalculater():
#     print(":::::::::: Basic Calculater ::::::::::::")
#     print("****::::::::::::::::::::::::::::::::*****")

#     val1 = int(input("Enter first number : "))
#     val2 = int(input("Enter second number : "))

#     print("Please Chosse what you want:")


#     print(""" 
#     1.) Addation
#     2.) Substraction
#     3.) mUltiplication 
#     4.) Divsion      
#     """)


#     userchoice = input("Please Choose what you want to do : ")

#     if userchoice == "1":
#         sum = val1 + val2
#         print("The sum is : ", sum)

#     elif userchoice == "2":
#         sub = val1 - val2
#         print("The subsration is : ", sub)

#     elif userchoice == "3":
#         multi = val1 * val2
#         print("The multiplication is : ", multi)

#     elif userchoice == "4":
#         div = val1 / val2
#         print("The devsion is : ", div)


#     else:
#         print("You entered somthing wrong, choose any from the options....!!!")




# # print("""
# # 1.) calculater
# # 2.) simple print something
# # """)

# # x = input("Please choose what you want : ")



# # if x =="1":
# #     ourcalculater()
# # elif x=="2":
# #     abc()
# # else:
# #     print("something went wrong...")




# len() function:::

# a = 87238213728

# print(len(a))
# print(type(a))

# def sum(a, b):
#     abc = a + b
#     print(abc)



# decleration of function 
# def abc():
#     print("hlooooooooo")




# abc()


# abc()


# abc()






# def sum():
#     c = 12 + 10
#     print(c)

# sum()

# sum()

# sum()

# 1) peramerterss
# 2) arguments

# def sum(a, b):
#     abc = a + b 
#     print("the sum is : ",abc)



# sum(1, 2)


# sum(12, 5)


# sum(0, 9)


# def substrcation(a, b):
#     abc = a - b 
#     print("the substraction is : ",abc)


# substrcation(10, 6)

# sum(7, 10)


# def sub(a,b):
#     bcd = a - b
#     print("solve value  = ", bcd)

# sub(12,10)

# def myfun():
#     av = 41 + 12
#     print(av)

# myfun()
# # myfun()
# myfun()
# myfun()






# *args
# a = (1, 2,34 ,56,8 ,8)

# for ai in a:
#     print(ai)


# arbitrary arguments:

# def xyzsum(*args):
#     total = 0

#     for i in args:
#         total = total + i

#     return total


# xz = sum(1,2,3, 3, 4, 5, 6, 8)

# print("the sum is : ", xz)



# userwant = int(input("Enetr number of inputs you want to enter : "))


# xzy = [int(input("Enter number : ")) for i in range(userwant)]

# print(xzy)



# zxzxz = sum(*xzy)


# print("the sum is : ", zxzxz)

# for i in range(start, end, incremnt):
#     print("hloooo")



# functions
# if else elif 
# variables
# for loop
# arguments
# perametes
# arbigtrary args


# def decolater(abc):
#     def wwrap(a,b):
#         print("good morning")
#         abc(a,b)
#         print("thanks for using")
        
#     return wwrap

# @decolater
# def abc(a,b):
#     c = a + b
#     print("the output is::::",c)

# abc(100,20)

# @decolater
# def bbb(a,b):
#     print("hello world")

# bbb(20,30)

# def ops(a,b,c):
#     num = a+b+c
#     return num

# print(ops(1,2,3))

# a = 2**8


# print(a)


# a = [23,5,6,7,8,90]
# a.sort()
# print(a)

# for i in a():


# a.append(1)
# print(a)

# for i in a(1,7):
#     print(i)


# x = [2,5,8,5,1656,965,2]
# x.append(55)
# print(x)

# x = [2,5,8,5,1656,965,2]
# x.insert(0,55)
# print(x)

# a = 10,2,2,655,385,11,2

# v = a[:2]
# print(type(v),v)

# print(a.count(2))

# a = {12,12,56,56,4,2,5,8,9,7}
# b = list(a)
# print(b)


# a = {5,4,3,2,1,6}
# b = list(a)
# print(b)

# a = {"name":"ayush",
#      "language":"python",
#      "version":"3.0",
#      "salary":"15lkpa"
     
     
#      }

# # b = a["name"]
# # print(a.keys())
# # print(a.values())
# a.pop("version")
# print(a)

# a = {2,5,56,89,1}

# a.update(32)
# # a[0] ="system"
# print(a)


# a = ["this is a car"]
# b = a[0].split()
# print(b)


a = ("a", "b", "c", "d")
b = [1, 2, 3, 4]
l = []
v = list(a)
m = list(b)

c = zip(v, m)
l.extend(c)
print(l)





# print(type(b),b)



# v = []
# c = zip(a,b)
# l = list(c)
# print(l)

# v.extend(c)
# print(v)


# a = ("a", "b", "c", "d")
# b = [1, 2, 3, 4]

# c = []


# for i in zip(a,b):
#     c.extend(i)
# print(c)
    








