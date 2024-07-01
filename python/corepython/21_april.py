# print("hello world")

# def gen():
#     yield 1
#     yield 2
#     yield 3

# obj = gen()
# print(next(obj))
# print(next(obj))
# print(next(obj))

# for i in gen():
#     print(i)

# def gen(n):
#     for i in range(n):
#         yield i


# obj=  gen(11)



# for j in obj:
#     print(j)    





# def decorater(fun,*args,**kw):
#     def inner():
#         print("programming star now.....")
#         print(f"THE SUM IS {2+6}")
#         print("ENJOINTING programing..........")

#         fun()

#     return inner

# @decorater
# def main():
#     print("programming ending now....")


# main()


# from abc import ABC ,abstractmethod

# class pop(ABC):
#     @abstractmethod
#     def mtd(self):
#         print("mtd now.")

#     def mtd1(self):
#         print("mtd 1 now.")

#     def mtd2(self):
#         print("mtd 2 now.")




# class opp(pop):
#     def mtd3(self):
#         print("mtd 3 now.")

#     def mtd(self):
#         print("mtd now.....")


# obj = opp()
# obj.mtd()



class A:
    def __init__(self,x,l):
        self.x = x
        self.l = l


    def __add__(self,other):
        a = self.x + other.x
        b = self.l + other.l
        return A(a,b)
        

class B:
    def __init__(self,y,b):
        self.y = y
        self.b = b


a = A(100,12)
b = B(100,45)

print(a+b)



# class hop:
#     def sum(self):
#         print("sum")


# class d(hop):
#     def sum(self):
#         super().sum()
#         print("hello")


# o = d()
# o.sum()




# class d:
#     @staticmethod
#     def hel():
#         print("hello")

#     def hel1(self):
#         print("hello world....")


# o = d()
# o.hel()






    




    