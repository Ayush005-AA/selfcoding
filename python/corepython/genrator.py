# def opp(d):
#     for i in range(d):
#         yield i

# obj = opp(10)
# print(iter(obj))


# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))


# a = [1,2,23,565,5,485,6]
# b = iter(a)

# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))


# \\\\\\\object delte

# class ddd:
#     def mn(self):
#         print("heloo i am mn")

#     def nn(self):
#         print("hello i am nn")

# obj = ddd()
# del  obj
# obj.nn()


# a = 10
# a /=2
# print(a)


# genter is a python fucntion it return iterator using the yield function


# def gen():
#     yield 1
#     yield 2
#     yield 3


# obj = gen()
# print(next(obj))
# print(next(obj))

# for i in gen():
#     print(i)



# decorator


# def decorator(fun):
#     def wrapper():
#         print("start decorator")
#         fun()

#         print("end decorator")

#     return wrapper

# def main():
#     print("loading decorator")


# def ss():
#     print("hello")

# obj1 = decorator(main)
# obj = decorator(ss)
# obj1()
# obj()


# @ using in decorator


# def decorator(fun):
#     def wrapper(a,b):
#         print("start program")

#         fun(a,b)

#         print("this program is end..")

#     return wrapper

# @decorator
# def ad(a,b):
    
#     print(f"output is {a+b}")


# ad(10,20)



# a = 10
# b = a*11
# c = "ca"
# a = (b-len(c))
# print(a)
    


# fib_sequence = [0, 1]

# for i in range(2, 20):
#     next_num = fib_sequence[-1] + fib_sequence[-2]
#     fib_sequence.append(next_num)

# print(f"[{', '.join(map(str, fib_sequence))}]")


# a = [0, 1]

# for i in range(2,20):
#     b = a[-1]+a[-2]
#     a.append(b)

# print(f"[{', '.join(map(str, a))}]")







# a = [1,2,3,4]
# def m(n):
#     return n*n



# o = map(m,a)
# for j in o:
#     print(j)

    




    


