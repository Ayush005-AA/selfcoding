from tkinter import *

root = Tk()

root.geometry("500x500")

root.title("My Form")

l = Label(root,text="name :",font="comicsansms 20 bold ")
l1 = Label(root,text="Email :",font="comicsansms 20 bold ")
l2 = Label(root,text="Phone No :",font="comicsansms 20 bold ")
l.pack(anchor="nw")
l1.pack(anchor="nw")
l2.pack(anchor="nw")

en = Entry(root,font="comicsansms 20 bold")
en1 = Entry(root,font="comicsansms 20 bold")
en2 = Entry(root,font="comicsansms 20 bold")
en.pack()
en1.pack()
en2.pack()

btn = Button(root,text="submit",font="comicsansms 30 bold")


root.mainloop()

# from tkinter import *
# import mysql.connector

# con  = mysql.connector.connect(host ="localhost", username = "root", password = "ayush22001", database = "school")
# cursr = con.cursor()


# def data():
#     en1 = entr1.get()
#     en2 = entr2.get()
#     en3 = entr3.get()

#     cursr.execute(f"insert into  hello values('{en1}',{en2},'{en3}')")
#     con.commit()


# root = Tk()

# root.geometry("900x400")
# root.title("My Form")
# root.configure(bg= "red")

# labl1 = Label(root, text = "Name : ", font=("comicsansms 20 bold"))
# labl2 = Label(root, text = "Email : ", font=("comicsansms 20 bold"))
# labl3 = Label(root, text = "Phoneno : ", font=("comicsansms 20 bold"))



# entr1 = Entry(root, font=("comicsansms 20 bold"))
# entr2 = Entry(root, font=("comicsansms 20 bold"))
# entr3 = Entry(root, font=("comicsansms 20 bold"))

# btn = Button(root, text="Submit", font=("robort", 20, "bold"),command= data)


# labl1.grid(row=0, column=0, pady=10)
# labl2.grid(row=1, column=0, pady=10, padx=50)
# labl3.grid(row=2, column=0, pady=10)
# entr1.grid(row=0, column=2, pady=10)
# entr2.grid(row=1, column=2, pady=10)
# entr3.grid(row=2, column=2, pady=10)
# btn.grid(row=3, column=1, pady=10)



# root.mainloop()








import tkinter as tk
# from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("400x400")
root.title('Login')
# root.resizable(10, 10)

# # # configure the grid
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=3)


# username
username_label = tk.Label(root, text="Username:",font=20)
username_label.grid(column=0,row=0,sticky=tk.NW,padx="5",pady="5")

# username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = tk.Entry(root)
username_entry.grid(column=1,row=0,sticky=tk.NW,padx=5,pady=10)
# username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# # password
password_label = tk.Label(root, text="Password:",font=20)
password_label.grid(column=0,row=1,sticky=tk.NW,padx=5,pady=10)
# password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = tk.Entry(root,  show="*")
password_entry.grid(column=1,row=1,padx=5,pady=10)
# password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# # login button
login_button = tk.Button(root, text="Login")
login_button.grid(column=1,row=3,padx=5,pady=5)
# login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop()



