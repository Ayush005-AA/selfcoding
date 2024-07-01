# print("hello world!")



# oops stnds for object oriented programing 

# class 
# object
# inheritance
# encaplucation
# polymorphism
# abstraction


# class is a blue print

# object is the inntance of class



# inheritance 
# parents and children relationships
# 1) single inheritance
# 2) multipal inheritance (2parents and 1 children)
# 3) multilevel inheritance
# 4) herirical inheritance




# ////////////////////////single inheritance//////////////////////////

# class parents:
#     def mtd(self):
#         print("hi i am mtd..")


#     def _mtd1(self):
#         print("hi i am mtd1")

#     def mtd2(self):
#         print(" hi i am mtd2")

# # obj = parents()
# # obj._mtd1()


# class childern(parents):
#     def metd3(self):
#         print("hi i am metd3")


# obj = childern()
# obj._mtd1()




# ///////////////////////////////////////multipal inheritance///////////////////////////////////

# class parent:
#     def mtd(self):
#         print("hi i am mtd")

#     def mtd1(self):
#         print("i am mtd1")

#     def mtd2(self):
#         print("i am mtd2")

# class parent2():
#     def mtd3(self):
#         print("hi i am mtd3")

#     def mtd4(self):
#         print("i am mtd4")

# class childrec(parent,parent2):
#     pass


# obj = childrec()
# obj.mtd2()


# ///////////////////////////multilevel inheritance/////////////////////

# class parent:
#     def mtd(self):
#         print("hi i am mtd")

#     def mtd1(self):
#         print("i am mtd1")

#     def mtd2(self):
#         print("i am mtd2")

# class parent2(parent):
#     def mtd3(self):
#         print("hi i am mtd3")

#     def mtd4(self):
#         print("i am mtd4")

# class childrec(parent):
#     def mtd5(self):
#         print("hi i am mtd5")


#     def mtd6(self):
#         print("i am mtd6")


# class childreccc(parent2,childrec):
#     def mtd7(self):
#         print("hi i am mtd7")

#     def mtd8(self):
#         pass        


# obj = childreccc()
# obj.mtd1()



# class cls1:
#     def mthd1(self):
#         print("i am from class 1")
    
#     def mthd2(self):
#         print("i am form class1 and mthd 2")
        
# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2 and mehtd 3")

# class cls3(cls1):
#     def mthd4(self):
#         print("i am from class 3")
        
# class cls4(cls2, cls3):
#     pass

# obj = cls4()
# obj.mthd1()
# obj.mthd1()


# 3) abstraction = ABC stands for abstract base class 

# from abc import ABC ,abstractmethod

# class abs(ABC):

#     @abstractmethod
#     def mtd(self):
#         print("hiding mtd")

#     def mtd2(self):
#         print("i am mtd2")

#     def mtd3(self):
#         print("i am mtd3")


# class dof(abs):
#     def mtd4(self):
#         print("i am mtd4")


    
#     def mtd(self):
#         print("hiding mtd")



# obj = dof()
# obj.mtd()


# do you know constructor don't worry i m explaining

# constr call automatically don't need calling


# class cls:
#     def __init__(self):
#         print(" i am constructor....")

#     def mtd(self):
#         print("i am mtd..")          //////////////////prime example of constructor////////////

#     def mtd1(self):
#         pass


# obj = cls()




# class cls:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
        
        

#     def mtd(self):
#         print(f"Age is : {self.a} and name is : {self.b}")

#     def mtd1(self):
#         pass

# obj = cls(12,"ayush")
# obj.mtd()



#/////////////////////////////////////// *args and **kwargs

# class plp:
#     def __init__(*args, **kwargs):
#         print(args)
        

#     def mtd(self):
#         print("i m mtd...")


#     def mtd1(self):
#         print("i mtd1...")


# obj = plp("ayush","dhiman")


# //polymorphism 

# poly = more
# phism = forms


# compile time polymorphism
# 1) method overloading 
# 2)operator overloading

# run time polymorphism
# 1) method overriding


# print(True)


# class physm:
#     def __init__(self,a,b):
#         self.num = a
#         self.num1 = b

#     def __add__(self,another):
#         a = self.num+another.num
#         b = self.num1+another.num1 

#         sum = physm(a,b)
#         return sum
    
#     def __sub__(self,d):
#         a = self.num - d.num
#         b = self.num1 - d.num1

#         sub = physm(a,b)

#         return sub


# obj = physm(10,20)
# obj1 = physm(40,50)
# c = obj-obj1
# print(c.num)

# ///////////////////////// operator overloading

# class oop:
#     def sum(self,a,b,c):
#         x = a+b+c
#         print(x)

        
    
#     def sum(self,a,b):
#         x = a+b
#         print(x)
       


#     def sum(self,a):
#         x = a
#         print(x)



# obj = oop()
# obj.sum(50,2)



















# ////////////////////////////////////method overriding


# a = 10
# a  = 20
# print(a)

# class ovr:
#     def mtd(self):
#         print("i am mtd....")

#     def mtd1(self):
#         print("i am mtd1..")

# class ovrr(ovr):
#     def mtd(self):
#         print("i am mtd 2nd ....")

#     def mtd1(self):
#         print("i am mtd1..")


# obj = ovrr()
# obj.mtd()

# Encapsluation................... 

# class vv:
#     def __init__(self):
#         self.a = 12
#         self.__b = 10



#     def mtd(self):
#         print("i am mtd..")

#     def _mtd1(self):
#         print(f"i am mtd1..{self.__b}")

#     def mtd2(self):
#         print("i am mtd2..")


# obj = vv()
# # obj._mtd1()

# class ovr:
#     def mtd(self):
#         print("i am mtd....")

#     def mtd1(self):
#         print("i am mtd1..")

#     def __mtd2(self):
#         print("i am mtd 222nd ....")

#     def mtd3(self):
#         print("i am mtd333333..")
#         # print("i am mtd333333333333..",obj.__mtd2())


#     # def mtd4(self):
#     #     obj.__mtd2()
    

# obj = ovr()
# obj.mtd3()


# class popo:
#     def car():
#         print("i am car")


#     def bus():
#         print("i am bus")

#     @staticmethod
#     def show():
#         print("i am show")

# popo.bus()

# obj = popo()

# obj.show()












# zx = 3
# num1 = 6
# k = 0
# t = 0

# for i in range(num1):
#     print(t * "_",end=" ")

#     for i in range(zx):
#         print(num1,end=" ")
#         num1 = num1 - 1

#     print()
#     t = t + 1
#     zx = zx - 1
#     if t > 2:
#         break





# operator overloading//////////////


class A:
    def __init__(self,x):
        self.x = x


#   thhis is operator method call in + operator
    def __add__(self,other):
        return self.x + other.x
    



class B:
    def __init__(self,x):
        self.x = x


obj = A(100)
obj1 = B(100)

print(obj+obj1)
















        













