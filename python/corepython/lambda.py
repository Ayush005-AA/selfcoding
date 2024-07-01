
# a = [1,2,3,4,5,6]

# b = (lambda x:x + 10,a)

# print(list(b))

# a = [1, 2, 3, 4, 5, 6]

# b = (lambda x: x + 10, a)
# print(list(map(b[0], b[1])))
# print(b)

# from functools import reduce

# a = [1,2,3,4,5,6,7,8,20,30,40]
# b = reduce(lambda x,y : x + y,a)
# print(b)

# a = [1,2,3,4,5,6,7,8,20,30,40]
# b = filter(lambda x:x %2==0,a)
# print(a)

# //////////////Map////////////////////////////////////////


# a = [1,2,3,4,5,6]
# b = list(map(lambda x:x+1,a))
# print(b)

# //////////filter//////////////////

# a = [1,2,3,4,5,6]
# b = list(filter(lambda x:x %2 == 0, a))
# print(b)

# /////reduce///////////////////

# from functools import reduce

# a = [1,2,3,4]
# b = reduce(lambda x,y:x+y,a)
# print(b)


# def decolater(fun):
#     def wwrap(*args,**kwargs):
#         print("good morning")
#         fun(*args,**kwargs)
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

# a = lambda b,c: b+c

# print(a(5,5))



# v = filter(lambda x: x%2==0,range(21))
# print(list(v))

# from functools import reduce

# v = reduce(lambda x, y : x*y , range(1,6))
# print((v))
    


# x,y = "12"
# y,z = "45"
# print(x,y,z)


def fac(n):
    if n == 0: 
        return 1
    
    else:
       return n*fac(n-1)


print(fac(5))
