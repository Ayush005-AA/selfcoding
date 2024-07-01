# def outer(pt):
#     def inner(a,b):
#         print("hello world")
#         print("good morning")
#         pt(a,b)
#         print("end")
#     return inner


# @outer
# def main(a,b):
#     print(f"output is {a+b}")


# main(1,2)


a = [0, 1]
for i in range(2, 7):
    next_num = a[i-1] + a[i-2]
    a.append(next_num)

for num in a:
    print(num,end=",")


# a = [1,2,3,4,56,5,8,10]

# for i in a:
#     if i%2  == 0:
#         print(i,end=",")

# b = 0

# for m in i:
#     b+=m

# print(b)





# a = [1, 2, 3, 4, 56, 5, 8, 10]


# total_sum = 0

# for num in a:
#     total_sum += num

# print("Sum of the series:", total_sum)


# a = [1,2,3,4,5,8,10]

# b = 0

# for i in a:
#     b += i

# print(b)

# for i in range(1,11):
#     if i%2 == 0:
#         j = i 

# from functools import reduce

# for i in range(1,11):
#     if i%2 == 0:
#         # print(i,end=",")

#         j = i

#         b = lambda x,y : x+y
#         c = reduce(b,j)

#         print(c,end=",")

         

b = 0
for i in range(1,11):
    if i%2 == 0:
        print(i,end="")

        b += i


print("\n sum is ",b)




# a = 0   
# for i in range(1,11):
#     a += i
    
# print("\n sum is ",a)
        


# Define the first two elements of the Fibonacci series
# a, b = 0, 1

# # Print the first element of the series
# print(a, end=", ")

# # Print the second element of the series
# print(b, end=", ")

# # Generate and print the rest of the series
# for i in range(8):  # We need 5 more elements after the first two
#     # Calculate the next element in the series
#     c = a + b
#     # Update a and b for the next iteration
#     a, b = b, c
#     # Print the next element of the series
#     print(c, end=", ")



# a,b = 0,1

# print(a, end=", ")
# print(b, end=", ")


# for i in range(8):

#     c = a + b

#     a,b = b,c
#     print(c, end=", ")


# a = [1,5,6,100,5000,550000,6000000]

# b = min(a)

# if b == min(a):
#     print(b, end=", ")


# a = ["hello", "world","bike","plane","car"]

# print(a[2])


# a = 10

# b = a*11

# c = "ca"

# d = b - len(c)

# print(d, end=", ")


a = [1,5,6,100,5000,550000,6000000]

b = a[0]

for i in a:
    if i > b:
        b = i

        
print(b)


# for i in range(10):
#     print(i*"*", )


# def fun():
#     yield "good"
#     yield "morning"
#     yield "Guys"

# x = fun()

# for i in x:
#     print(i)


# generttor

def gen(n):
    for i in range(n):
        yield i

b = gen(10)
print(next(b))
print(b.__next__())


for j in b:
    print(j)






