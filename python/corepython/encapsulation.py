# class y:
#     _a = 10    ("protected")

#     __b = 20  ("private")
    
# class y:
#     _a = 10    
#     __b = 20  

# def show(self):
#     print("a = ",self._a)
#     print("b =",self.__b)

# obj = y()
# obj.show()

# class z:
#     _a = 10
#     __b = 20

#     def show(self):
#         print("a =", self._a)
#         print("b =", self.__b)

# obj = z()
# obj.show()
# print(obj._a)


# class uper:
#     def __init__(self):
#         self._value  = 100
#         self.__value1  = 200

#     def fun(self):
#         print(self._value)
#         print(self.__value1)
        

# class sub(uper):
#     def __init__():
#         super().__init__()    



# class n:
#     _a  = 10
#     __b = 20

#     def ops(self,):
#         print("a =",self._a)
#         print("b =",self.__b)
#         print("c=",self._a+ self.__b)

# obj = n()
# obj.ops()

# class oop:

#     def __init__(self):
#         self._num = 11
#         self.__num1 = 12
        
#     def mtd1(self):
#         # print("hllo")
#             print("i am first method",self.__num1 + self._num)
    
    
#     def mtd2(self):
#         print("i am second method")

# obj  = oop()
# obj.mtd1()

# print(obj.__num1)


# class opp1(oop):
#     def mtd3(self):
#         print("i am third method")


      

# obj = opp1()
# obj.__mtd1()



# class ddd:
#     def __init__(self,a):
#         self.__name = a

#     def __llo(self):
#         print("a am llo",self.__name)
    
#     def ool(self):
#         print("i am ool",)

#     def _loo(self):
#         # self.__ool()
#         # print(self.__name)
#         print("i am loo")


# obj = ddd()
# obj.__llo("ayush ")


# class fff(ddd):
#     def olo(self):
#         print("i am olo")

# obj = fff()
# obj.__ool()

# obj = fff()
# obj.__loo()



class ddd:
    def __init__(self):
        self.__name = "ayush"

    def _llo(self):
        print("i am llo",self.__name)
        
    
    def ool(self):
        print("i am ool")

    def _loo(self):
        # self.__ool()
        # print(self.__name)
        print("i am loo")

obj = ddd()
obj._llo()  # Call the private method within the class

   
        




        
