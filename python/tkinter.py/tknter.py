import tkinter as tk

app = tk.Tk()

app.geometry("500x500")
app.title("MY FIRST TKINTER APP")
app.configure(background="red")

lbl = tk.Label(app,text="WELCOME TO TKINTER",font="cursive")
lbl.pack(fill="x",padx=50)


entr = tk.Entry(app,font=("cursive",))
entr.pack(ipadx=10,ipady=5)

ck = tk.Checkbutton()
# ck = tk.Radiobutton()
ck.pack()

btn = tk.Button(app,text="submit")
btn.pack(pady=20)


app.mainloop()

import tkinter as tk

app = tk.Tk()

app.geometry("400x400")
app.title("My form")
# app.configure(background="yellow")

lb= tk.Label(app,text="Name:",font=("robort",10,"bold"))
lb1= tk.Label(app,text="Phone No:",font=("robort",10,"bold"))
lb2= tk.Label(app,text="Email Id:",font=("robort",10,"bold"))
lb.pack()
lb1.pack()
lb2.pack()

rn = tk.Entry(app,font=("robort",10,"bold"))
rn1 = tk.Entry(app,font=("robort",10,"bold"))
rn2= tk.Entry(app,font=("robort",10,"bold"))

bn = tk.Button(app,text="submit",font=("robort",10,"bold"))



# lb.grid(row=0, column=0, pady=10)
# lb1.grid(row=1, column=0, pady=10, padx=50)
# lb2.grid(row=2, column=0, pady=10)
# rn.grid(row=0, column=2, pady=10)
# rn1.grid(row=1, column=2, pady=10)
# rn2.grid(row=2, column=2, pady=10)
# bn.grid(row=3, column=1, pady=10)

# labl4.grid(row=0, column=1)
# labl5.grid(row=1, column=1)
# labl6.grid(row=2, column=1)


app.mainloop()




# import tkinter as tk
# import mysql.connector
# import re
# con  = mysql.connector.connect(host ="localhost", username = "root", password = "ayush22001", database = "school")
# cursr = con.cursor()


# def savedata():
#     en1 = entr1.get()
#     en2 = entr2.get()
#     en3 = entr3.get()


#     pt = "[A-z{8}]"
#     if re.search(pt,en1):
#         print("")

#     else:
#         print("invalid name..!")


#     ptr = "\d{10}"

#     if re.match(ptr, en2):
#         print("")
#     else:
#         print("invalid phone number..!")

#     ptrn = "[a-z]+\d{4}@[a-z]+\.{4}"
#     if re.match(ptrn, en3):
#         print("")

#     else:
#         print("Invalid email address....!")


#     if re.match(pt,ptr,ptrn):
#         cursr.execute(f"insert into bbb values('{en1}',{en2},'{en3}')")
#         con.commit()

#     else:
#         print("sorry your data not found")
        


        

#     # cursr.execute(f"insert into bbb values('{en1}',{en2},'{en3}')")
#     # con.commit()

#     labl4.config(text="Data saved..! ")
# app = tk.Tk()

# app.geometry("900x400")
# app.title("My Form")



# labl1 = tk.Label(app, text = "Name : ", font=("robort", 20, "bold"))
# labl2 = tk.Label(app, text = "Phone Number : ", font=("robort", 20, "bold"))
# labl3 = tk.Label(app, text = "Email : ", font=("robort", 20, "bold"))
# labl4 = tk.Label(app,text="",font=("robort",20,"bold"))


# entr1 = tk.Entry(app, font=("robort", 20, "italic"))
# entr2 = tk.Entry(app, font=("robort", 20, "italic"))
# entr3 = tk.Entry(app, font=("robort", 20, "italic"))

# btn = tk.Button(app, text="Submit", font=("robort", 20, "bold"),command= savedata)


# labl1.grid(row=0, column=0, pady=10)
# labl2.grid(row=1, column=0, pady=10, padx=50)
# labl3.grid(row=2, column=0, pady=10)
# entr1.grid(row=0, column=2, pady=10)
# entr2.grid(row=1, column=2, pady=10)
# entr3.grid(row=2, column=2, pady=10)
# btn.grid(row=3, column=1, pady=10)




# app.mainloop()
# print("sucessfully submited in database...!")


# from tkinter import *

# root = Tk()


# root.geometry("400x400")
# root.configure(background="white")

# l  = Label(root,text="this is place",font=("cursive",20,"bold"))
# l.place(x = 100,y=200)
# l1  = Label(root,text="this is place",font=("cursive",20,"bold"))
# l1.place(x=300,y=100)
# l2  = Label(root,text="this is place",font=("cursive",20,"bold"))
# l2.place(x=400,y=400)


# root.mainloop()


