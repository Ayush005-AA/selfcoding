a = int(input("enter a number::"))
b = int(input("enter a number::"))


try:
    c = a/b
    

except Exception:
    print("this is error")

else:
    print("the output is ::",c)

finally:
    print("done")



# a = (1,2,3)
# b = a,(3,4)
# a = b+a
# print(a)