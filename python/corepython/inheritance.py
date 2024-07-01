#  types of inharitance///////
# 1) single inharitance
# 2) multipal inharitance
# 3) multilevel inharitance
# 4) hirerachical inharitance
# 5) hybrid inharitance


# class cls:
#     def mth(self):
#         print("i am class  method")

#     def mth1(self):
#         print("i am class method 1")


# class cls1(cls):
#     def mth2(self):
#         print("i am first class method 2 ")


# class cls2(cls1):
#     def mth3(self):
#         print("i am second class method 2")

# class cls3(cls2):
#     def mth4(self):
#         print("i am third class method 4")

# obj = cls3()
# obj.mth4()


# class cls:
#     def __init__(self,a,b):
#         self.name = a
#         self.age = b

#         # print(f"user name is:::{self.name} user age is::{self.age}")

# # obj = cls("ayush",22)

# class cls1(cls):
#     def __init__(self,a,b,c):
#         super().__init__(a,b)
#         self.id = c

#         print(f"user name is:::{self.name} user age is::{self.age} user id is::{self.id}")

# obj = cls1("ayush",22,2001)


import calendar
year = 2024
month = 5
x = calendar.month(year,month)
print(x)

# class av:
#     def __init__(self,a,b):
#         self.name = a
#         self.age = b
#         print(f"user name is :: {a} user age is :: {b}")        

#     def mmm(self):
#         print("hyy i am mmm")

#     def mmn(self):
#         print("hyy i am mmn ")

#     def mnn(self ):
#         print(" hy i am mnn")
 
# class ap(av):
#     def nnn(self):
#         print("hyy i am nnn")

#     def nno(self):
#         print("hy i am nno")

# oob  = av("Aman",22)
# oob.mnn()

# \\\\\\\\\\\\\\\\\overide???????????

class a:
    def ops(self):
        print("hy i am a ops.")

    def lop(self):
        
        print("hi i am lop")

class b(a):
    def ops(self):
        print("hy i am2333 ops")

o = b()
o.ops()




    




        





