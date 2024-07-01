
# ::::::::::::::dictnory::::::::::::::

# :::kwds not same but no same not prblm::::

# a = {'age':20,'agee':20}
# b = a
# print(type(a))
# print(len(a))
# print(list(a))
# print(a.get(20))
# print(a)

# "::::::::::::::::indexing:::::::;

# a = [10,10.1,'True','rahul',10]
# print(type(a))
# print(a)

# print(a[3])  

# ::::::::::::slicing:::::::::::::  

# a = [10,10.1,'True','rahul',10]

# print(a[0:4])    

# ::::::::count list itemm::::::::::

# a = [10,10.1,'True','rahul',10,10]

# print(a.count(10))


    #::::::::::::::::::::::::index::::::::::::::

# a = [10,10.1,'True','rahul',10]
# print(a.index(10,1)) 

# ::::::::insert:::::::::::it takes two arguments one is postion and second you want:::::

# a = [10,10.1,'True','rahul',10]
# a.insert(2,"ayush")
# print(a)

# :::::::::::::::pop:::::::::::::only take postion::::::::::::::::::

# a = [10,10.1,'True','rahul',10]
# a.pop(2)
# print(a)

# ::::::::extend:::::

# a = [10,10.1,'True','rahul',10]

# b = ["ayush","dhiman"]

# b.extend(a)
# print(b)

# # :::::::::::copy::::::

# a = [10,10.1,'True','rahul',10]

# c = a.copy()
# print(c)

# :::::: sort it is use to maintain the items in aceding and discanding oder::

# a = [3,56,12,1,2,4]

# a.sort()
# print(a)

# :::::::::::discandingoder:::::::

# a = [3,56,12,1,2,4]

# a.sort(reverse=5)
# print(a)

# :::::::reverse::::::::::::::

# a = [3,56,12,1,2,4]

# a.reverse()
# print(a)


# :::::::::::::::::nested list:::::::
  
# a = [1,10,1.2,5,["ayush",["dhiman"]]]
# print(a)

# :::::::::::::list comprehension::::::::

# a = ["ayush","dhiman","akshu","amam","kumar"]

# b =[ word for word in a if word.startswith ('d')]
# print(b)



# """"""""""""""""""""""///////////////////set/////////////////""""""""""""""""""

# a = {10,2.0,'True','ayush','ayush'}

# print(a.pop())
# print(a)


# for i in range(6):
#     print("hyy")

# else:
#     print("gud night")
 
# # for i in range(10):
# #     print(i)
# #     if i == 4:
# #         break


# from turtle import *

# color("green")
# bgcolor("black")
# speed(200)
# hideturtle()

# b=0
# while b<200:
#     left(b)
#     forward(b)
#     b = b+1

a = "My name is bob"
b = " ".join(a.split()[::-1])
print(b)
