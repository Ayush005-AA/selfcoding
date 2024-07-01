# from playsound import playsound
# playsound('/path/to/a/sound/file/you/want/to/play.mp3') 

# import os
# print(os.listdir())

# a = "1234"
# a = int(a)
# print((a+5))

# a = 1!=11
# print(a)

# a = input("enter name::::")
# a = int(a)
# print(type(a))


# a = int(input("enter number:::"))
# b = int(input("enter second number:::"))

# c = a+b/2
# print(c)


# myslf = '''my name is abc i am from delhi my father name is xxv and my mother is oop i love playing cricket
#             i love playing'''

# print(myslf.startswith("my"))
# print(myslf.count("my"))
# print(myslf.capitalize())
# print(myslf.replace("abc","ayush"))


# a = "my name is abc \ti am from delhi \t my father name is xxv"

# print(a)


# a = '''dear '<|NAME|>'
# congrats you are selected in tp company 
# have a good day
# your joning is <|DATE|>
# '''

# nam = input("enter name:::")
# date = input("enter date :::")

# a = a.replace("<|NAME|>",nam)
# a = a.replace("<|DATE|>",date)

# print(a)

# list method::::


# a = [1,25,2,6,3,5,8]
# a.reverse()
# a.pop()
# a.append()
# a.count()
# print(a)


# tuple:::::::; tuple are immutable  , they can not change the element


# a = (1,23,4,5,6,1,45,3,1)
# print(a.index(6))

# print(a.count(6))


#  \\\\\\\\\\\\\\\dictonary\\\\\\\\\\\\\\\\

#     keys    value  :::::::::::::::::::::
# a = { "name":"ayush" ,
#     "ayush" : "python developer",
#     "salary" : [9,500000]}

# print(a["name"])
# print(a["ayush"])
# # print(a["salary"])
# a["salary"] = [10000000]
# print(a["salary"])

# print(a.keys())
# print(a.items())
# print(a.values())


# b = {"akshu":"brother"}
# a.update(b)
# print(a)
# print(a.get("name1"))  
# print(a["name1"])


# \\\\\\\\\\\set\\\\\\\\\\\\\

# a = {1,2,2,3,45,6,7,89}
# print(type(a))
# print(a)
# a.remove(3)
# print(a)
# a.add(166)
# print(a)

#   this is set it is not the repeated the value


# num1 = int(input("enter number1\n"))
# num2 = int(input("enter number2\n"))
# num3 = int(input("enter number3\n"))
# num4 = int(input("enter number4\n"))
# num5 = int(input("enter number5\n"))

# s = {num1,num2,num3,num4,num5}
# print(s)


# a = {20,"20",20.0}
# print(len(a))


# a = int(input("enter your age:::"))
# if(a>18):
#     print("you are eligable for voat")

# if(a ==18):
#     print("welcome you are eligable for fist vaot::")

# else:
#     print("sorry you are under the age")

# a = 10
# if (a>15):
#     print("greater")
# else:
#     print("lesser")

# a=10,12,14,52
# # print(10 in a)
# li = []
# for i in a:
#     li.append(a)
#     print(li)

# n = int(input("enter factorial number:::"))
# p = 1
# for i in range(n):
#     p = p*(i+1)
# print(p)

# print("hello",end =" ")
# print("world",end =" ")
# print("how",end =" ")
# print("are",end =" ")
# print("you",end =" ")

n = int(input("enter number  "))
for i in range(n):
    print("*" *(n-i))
