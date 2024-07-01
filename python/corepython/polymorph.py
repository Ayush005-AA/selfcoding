# class reson:
#     def __init__(self, a,b):
#         self.var = a
#         self.var2 = b
#     def method (self):
#         print("hello world")

#     def __sub__(abc,efg):
#         med = abc.var - efg.var
#         med1 = abc.var2 - efg.var2
#         sub = reson(med,med1)
#         return sub
    

# obj = reson(2400,2200)
# obj1 = reson(1400,1200)

# sub = obj - obj1

# print(sub.var)
# print(sub.var2)

    #  __add__(kk,jj):
#         mt = kk.vr + jj.vr
#         mt1 = kk.vr1 + jj.vr1
#         sum = popin(mt,mt1)
#         return sum

# obj = popin(100,10)
# obj1 = popin(120,10)

# sum = obj + obj1

# print(sum.vr)
# print(sum.vr1)
 # class popin:
#     def __init__(self , a, b ):
#         self.vr = a
#         self.vr1 = b

#     def mtd(self):
#         print("hello world")

#

#:::::polymorphism  are two types , overloading, overriding::::::::::: 


# :::::::::::overloading:::::::function same parameter unik acooding you::::

# class me:
#     def metoh(self,name):
#         print("heloo buddy",name)

# obj = me()
# obj.metoh("dilpreet")


# ::::::overriding:::::::::::::::::::::

# class me:
#     def metoh(self):
#         print("heloo buddy")

# class you(me):        
#     def metoh(self):
        
#         print("good night")
# obj = you()
# obj.metoh()

# class me:
#     def metoh(self):
#         print("heloo buddy")

# class you(me):        
#     def metoh(self):
#         super().metoh()
#         print("good night")
# obj = you()
# obj.metoh()

# \\\\\\\\\\\\\\\\\\\\\\\overloading\\\\\\\\\\\\\\\

# class mmm:
#     def sum(self,a,b,c):
#         print(a+b+c)

#     def sum(self,a,b):
#         print(a+b)

#     def sum(self,a):
#         print(a)

# obj = mmm()
# obj.sum(10)
  


# class A:
#     def show(self):
#         print("i am first method")

#     def show(self,a):
#         print("i am ",a)

#     def show(self,a,b):
#         print("i am ",b)


# obj = A()
# obj.show("ayush")



# class S:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def __str__(self):
#         return f"{self.a},{self.b},{self.c}"
    
#     def __add__(self,x):
#         return f"{self.a+x.a},{self.b+x.b},{self.c+x.c}"


# obj = S(4,22,2001)
# print(obj)

# # obj1 = S(2,2,6)
# # print(obj1)


# class abk:
#     def mtd(self,a,b,c):
#         x = a+b+c
#         print(x)

#     def mtd(self,a,b):
#         x = a+b
#         print(x)


#     def mtd(self,a):
#         x = a
#         print(x)


# obj  = abk()

# obj.mtd(20,5)

# operator overloading//////////////


# class A:
#     def __init__(self,x):
#         self.x = x


# #   thhis is operator method call in + operator
#     def __add__(self,other):
#         return self.x + other.x
    



# class B:
#     def __init__(self,x):
#         self.x = x


# obj = A(100)
# obj1 = B(100)

# print(obj+obj1)


# /  method overloading////////////




# class a:
#     def sum(self,a):
#         print("i am sum method...",a)

#     def sum(self):
#         print("i am sum2 method...")

# obj = a()
# obj.sum()
# obj.sum(10)

# method overloading.....................

# class mycls:
#     def sum(self,a = None,b = None,c = None):
#         if a!=None and b!=None and c!=None:
#             s = a+b+c
        
#         elif a!=None and b!=None:
#             s = a+b

#         else:
#             a!=None

#             s = a
        
#         return s


# obj = mycls()
# print(obj.sum(10,2,8))
# print(obj.sum(10,2))
# print(obj.sum(10))



# method overriding......................


# class Add:
#     def result(self, a,b):
#         print("add is ",a+b)


# class multi(Add):
#     def result(self, a, b):
#         super().result(10,20)
#         print("multi is ",a*b)
        


# obj = multi()
# obj.result(10,20)

# i = i + 1
# i = 2 + 1

# i = 3 + 1
# i = 4 + 1


# x = True
# y = False

# print(x or x and y)
        


# x = 5

# def add():
#     x = 3
#     x = x + 5
#     print(x)

# add()
# print(x)




class abl:
    def __init__(self,x):
        self.x = x

    def __add__(self,a):
        return self.x + a.c


class acl:
    def __init__(self,c):
        self.c = c



obj = abl(10)
obj1 = acl(20)

print(obj+obj1)

        


