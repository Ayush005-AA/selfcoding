# what is genrator?

# def gen():
#     yield 1
#     yield 2
#     yield 3

# o = gen()
# # print(o)
# for i in o:
#     print(i)


# def gen2(n):
#     for i in range(n):
#         yield i

# v = gen2(10)
# for j in v:
#     print(j)


# what is static method

# class A:
#     @staticmethod
#     def mtd():
#         print("hello world")

#     def mtd1():
#         print("hello")

# class B(A):
#     def mtd2():
#         print("mtd2")


# obj = B()
# obj.mtd()


# what is decoraters?


# def decorator(*args):
#     def inner():
#         print("Welcome to my decorator")

#         for fun in args:
#             fun()

#         print("Goodbye..")

#     return inner

# def main():
#     print(f"THE SUM IS : {4+6}")


# def suj():
#     print("nope")

# o = decorator(main,suj)
# o()

# recursion?

# def fack(n):
#     if n == 0:
#         return 1
    
#     else:
#         return n*fack(n-1)

# o = fack(5)
# print(o)


# inheritence..

# class A:
#     def mtd(self):
#         print("mtd..")

#     def mtd1(self):
#         print("mtd1..")


# class B(A):
#     def mtd2(self):
#         print("mtd2..")

#     def mtd3(self):
#         print("mtd3..")

# o = B()
# o.mtd()

# class A:
#     def mtd(self):
#         print("mtd..")

#     def mtd1(self):
#         print("mtd1..")


# class B(A):
#     def mtd2(self):
#         print("mtd2..")

#     def mtd3(self):
#         print("mtd3..")


# class C(B):
#     def mtd4(self):
#         print("mtd4..")

# o = C()
# o.mtd()

# class A:
#     def mtd(self):
#         print("mtd..")

#     def mtd1(self):
#         print("mtd1..")


# class B(A):
#     def mtd2(self):
#         print("mtd2..")

#     def mtd3(self):
#         print("mtd3..")

# class C(B):
#     def mtd4(self):
#         print("mtd4..")



# class D(C):
#     def mtd5(self):
#         print("mtd5..")


# o = D()
# o.mtd()

# compiler Compiler  


# 1) method overloading
# 2) operator overloading


# Run time polymorphism

# 1) method overriding..


# methodoverloading


# class A:
#     def sum(self,a,b,c):
#         c = a+b+c
#         print(c)

#     def sum(self,a,b):
#         c = a+b
#         print(c)

#     def sum(self,a):
#         c = a
#         print(c)

# o = A()
# o.sum(12,5)

# .....................................selg logic..............

# class A:
#     def sum(self,a = None,b = None ,c = None):
#         if a!=None and b!=None and c!=None:
#             s = a+b+c
#         elif a!=None and b!=None:
#             s = a+b

#         elif a!=None:
#             s = a

#         return s
        
# o  = A()
# print(o.sum(10,5))

# class A():
#     def sum(self):
#         print("hello world!")

#     def sum1(self):
#         print("yup...")

# class B(A):
    
#     def sum(self):
#         super().sum()
#         print("ooooooop")

# o = B()
# o.sum()


# ///////////////////////operator overloading////////

# class A:
#     def __init__(self,a):
#         self.a = a

#     def __add__(self,other):
#         return self.a + other.b
        

# class B(A):
#     def __init__(self,b):
#         self.b = b

# o = A(10)
# o1 = B(10)

# print(o+o1)

        

# def decorator(func):
#     def inner():
#         print("start decorator...")

#         func()

#         print("end decorator...")

#     return inner

# @decorator
# def pop():
#     print("Running...")

# pop()

class ops:
    def dog():
        print("Dog")
    @staticmethod
    def cat():
        print("Cat")

class pos(ops):
    def mtd():
        pass

obj = pos()
obj.cat()
