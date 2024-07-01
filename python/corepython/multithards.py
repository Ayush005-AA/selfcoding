# import re

# tet = "kzjbasbdbasbdkjasjbd9283498236 kagkabdkjasdbkjajdkas 7352836492 akjhdvjhasdad 9123798214"


# ptrn = "\d{10}"

# match = re.findall(ptrn, tet)

# print(match)


# a = sfbf* hsdf + 8923

# print(12 + 30)

# print('done')

# import threading


# class xyz:
#     def car(self):
#         for i in range(0, 12):
#             print("carrrr")



# class abc:
#     def bus(self):
#         for i in range(0, 12):
#             print("busssssss")

# obj1 = xyz()
# obj2 = abc()

# obj1.car()
# obj2.bus()

# 

# import threading

# class xyz:
#     def car(self):
#         for i in range(0, 120):
#             print("carrrr")

# class abc:
#     def bus(self):
#         for i in range(0, 120):
#             print("busssssss")

# obj1 = xyz()
# obj2 = abc()

# # obj1.car()
# # obj2.bus()

# th1 = threading.Thread(target=obj1.car)
# th2 = threading.Thread(target=obj2.bus)


# th1.start()
# th2.start()



# th1.join()
# print("ooooooooooooooooooo")


# from time import sleep
# from threading import Thread
# class a(Thread):
#     def run(self):
#         for i in range(5):
#             print("ayush")
#             sleep(1)

# class b(Thread) :
#     def run(self):
#         for i in range(5):
#             print("dhiman")
#             sleep(1)


# obj = a()
# obj1 = b()
# obj.start()
# obj1.start()


# from time import sleep
# from threading import Thread


# class a (Thread):
#     def run(self):
#         for i in range(5):
#             print("akshay")
#             sleep(1)

# class b (Thread):
#     def run(self):
    
#         for i in range(5):
#             print("dhiman")
#             sleep(1)

# ob = a()
# obj = b()
# ob.start()
# obj.start()



# import threading
# import time
# def myfun():
#     for i in range(20000):
#         print("firssstt")
        

# def secndfun():
#     for i in range(20000):
#         print("secondddd")

# st = time.perf_counter()
# myfun()
# secndfun()



# th1 = threading.Thread(target = myfun)
# th2 = threading.Thread(target = secndfun)

# th1.start()
# th2.start()

# print("Contiunueu,,,,,,")
# print("donnneeee")

# th1.join()
# th2.join()

# en = time.perf_counter()


# print(en - st)

# print("hello world")

import threading


class abc:
    def method(self):
        print("hyyy")

    def method1(self):
        for i in range(100):
            print("good morning....")

    def method2(self):
        print("okkkkkkk")


        print("code running....")

        print("done...")

       

        for i in range(50):
            print("good night...")

obj = abc()
trd = threading.Thread(target= obj.method)
trd1 = threading.Thread(target= obj.method1)
trd2 = threading.Thread(target= obj.method2)

trd.start()
trd1.start()
trd2.start()


trd.join()
trd1.join()
trd2.join()
print("enddddd..............")


import threading
class xyz:
    def mtd(self):
        print("hlo welcome ")

    def mtd1(self):
        print("i am starting>>")

    for i in range (10):
        print("code will be run in")

    print("hyyyyy")
    print("okkkkkkkk")




obj = xyz()
trd = threading.Thread(target=obj.mtd)
trd1 = threading.Thread(target=obj.mtd1)
trd.start()
trd1.start()

trd.join()
trd1.join()
trd2.join()
print("done")









