5# print("JAI MALIK BABA GUGA CHARTI")

# ////////////////////////////////////////////change the value b to a

# a = 5
# b = 6

# c = a

# a = b

# b = c

# print(a,b)


# a = 5 
# b = 6

# a,b = b,a

# print(a,b)

  
# //////////////////////////////how to know even to odd numbers//////////////////

# a = int(input("enter the number"))
# b = int(input("enter second number"))

# c = a/b

# if c%2  == 0:
#     print(f"Even number {c}")


# else:
#     print("this is odd number")

# user  = int(input("enter number"))

# if user%2 == 0:
#     print("even number")

# else:
#     print("odd number")


# import random

# a = random.randint(0,6)
# print(a)

# s  = "my name is ayush"

# print(s.upper())

# a = 1,2,4,6,3,5,7,9,8,10
# b = a.index(2)
# print(b)



# a = (1,2,4,6,3,5,7)
# b = list(a)
# b.append(100)
# a = tuple(b)
# print(a)



# user = int(input("Enter a table number:: "))

# for u in range(1,11):
#     print(f"{user} X {u} = {u*user}")


# class myClass:
#     def __init__(self,x):
#         self.x = x

#     @staticmethod
#     def staticMethod():  
#         return "i am a static method"




# class a:
#     def S(self):
#         print("class")


#     @a
#     def d(self):
#         print("i m C")


# def fun():
#     return 10,20,30

# print(fun())


# a = [1,5,6,5,595,2,952,6]
# b = set([2,6,2,5,2,8,66])
# print(len(a) ,len(b))

# a = set([1,4,7,9,7,4])
# print(a.__len__())


# x = lambda a,b,c,d,e: a+b+c+d+e 
# print(x(1,2,3,4,5))


# a = 12,2,5,3,6,8
# b = list(a)
# b.append(100)
# a = tuple(b)
# print(a)


# x = 10

# def fun():
#     x = 3
#     x = x+3
#     print(x)

# x = 4
# print(x)

# a = 10

# b = 1

# c = 10


# print(id(a))
# print(id(b))

# print(id(a)==id(b)==id(c))



class stat:
    def hop():
        print("hey")
    
    def gop():
        print("gud morning..")

    def nop():
        print("nop")

class lop(stat):
    def sop():
        print("i am sop")

    def ups():
        print("i am ups")

obj = lop()
# obj.