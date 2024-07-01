
# from abc import ABC 
# class startdd(ABC):
#     def method(self):
#         print("hello")


#     def method1(self):
#         pass



# class drugss(startdd):
#     def method2(self):
#         print("good morning")

#     def method1(self):   
#        print("buddy")

# obj = drugss()
# obj.method()
# obj.method1()

# obj.method2()



# from abc import ABC
# class reson:
#     def initer(self):
#         print("hello")

#     def toopr(self):
#         print("rahul verma")
    

#     @abstractmethod
#     def oopss(self):   this is interface
#         pass

# class loopiu(reson):
#     def oopss(self):
#         print("good evening")


# obj = loopiu()
# obj.initer()
# obj.toopr()
# obj.oopss()
        
# from abc import ABC,abstractmethod

# class car(ABC):
#     def show(self):
#         print("Every car have four wheel")

#     @abstractmethod
#     def speed (self):
#         pass

# class honda(car):
#     def speed (self):
#         print("honda car speed is 100km/hours")
  
# class maruti(car):
#     def speed (self):
#         print("maruti car speed is 80km/hours")

# obj = honda()
# obj.show()
# obj.speed()

# obj1 = maruti()
# # obj.show()
# obj1.speed()

# from abc import ABC , abstractmethod

# class jio(ABC):
#     @abstractmethod
#     def mtd(self):
#         print("i am first mtd")


#     @abstractmethod
#     def mtd1(self):
#        pass


# class jio1(jio):

#     def mtd2(self):
#         print("i am mtd 2")


#     def mtd(self):
#         print("i am  mtd")


#     def mtd1(self):
#         print("i am mtd1")
       



# obj = jio1()
# obj.mtd()


# from abc import ABC , abstractmethod

# class oop(ABC):

#     @abstractmethod
#     def mtd(self):
#         print("i am method")


#     @abstractmethod
#     def mtd1(self):
#         print("i am first method")
    
#     @abstractmethod
#     def mtd2(self):
#         print("i am second method")


# class opp1(oop):
#     def mtd3(self):
#         print("i am third method")

    
#     def mtd(self):
#         print("i am method")


#     def mtd1(self):
#         print("i am first method")
    
#     def mtd2(self):
#         print("i am second method")
    

# obj = opp1()
# obj.mtd2()

# from abc import ABC , abstractmethod

# class no(ABC):

#     @abstractmethod
#     def oop(self):
#         print("i am oop")

#     @abstractmethod
#     def yes(self):
#         print(" i am yes")

#     @abstractmethod
#     def fal(self):
#         print("i am fal")


# class oo(no):
#     def ko(self):
#         print("i am ko")

#     def oop(self):
#         print("i am oop")

#     # @abstractmethod
#     def yes(self):
#         print(" i am yes")

#     # @abstractmethod
#     def fal(self):
#         print("i am fal")


# obj=  oo()
# obj.fal()

# from abc import ABC ,abstractmethod

# class oop(ABC):

#     @abstractmethod
#     def pp(self):
#         print( "i am pp")

#     @abstractmethod
#     def ll(self):
#         print("i am ll")


# class iio(oop):
#     def ee(self):
#         print( " i am ee")


# #     def pp(self):
# #         print( "i am pp")

# #     def ll(self):
# #         print("i am ll")



# # obj = iio()
# # obj.pp()
    

# from abc import ABC , abstractmethod


# class lop(ABC):
#     @abstractmethod
#     def mtd(self):
#         print("hyy i am mtd")

#     def mtd1(self):
#         print("hyy i am mtd1")

# class ppp(lop):
#     def mtd3(self):
#         print("hyy i am mtd3")

#     def mtd(self):
#         print("hyy i am mtd")

# obj = ppp()
# obj.mtd1()       

# from abc import ABC , abstractmethod    
   
# class a(ABC):
#     @abstractmethod
#     def metd(self):
#         print("hello i am metd")

#     def metd1(self):
#         print("hello i am metd1")

# class b(a):
#     def mtd(self):
#         print("hello i am mtd")

#     def metd(self):
#         print("hello i am metd")


# obj = b()
# obj.metd1()


a = (1,2,3,456,89,1)

b = list[a]

a.append(12)

print(b)