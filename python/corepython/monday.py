
# import tkinter as tk

# # app = tk.Tk()
# app = tk.Tk()

# app.geometry("400x400")
# app.title("My form")
# # app.configure(background="yellow")

# lb= tk.Label(app,text="Name:",font=("robort",10,"bold"))
# lb1= tk.Label(app,text="Phone No:",font=("robort",10,"bold"))
# lb2= tk.Label(app,text="Email Id:",font=("robort",10,"bold"))

# rn = tk.Entry(app,font=("robort",10,"bold"))
# rn1 = tk.Entry(app,font=("robort",10,"bold"))
# rn2= tk.Entry(app,font=("robort",10,"bold"))

# bt = tk.Button(app,text="submit",font=("robort",10,"bold"))

# lb.grid(row=0,column=0,sticky=tk.NW,padx=5,pady=5)
# lb1.grid(row=1,column=0,sticky=tk.NW,padx=5,pady=5)
# lb2.grid(row=2,column=0,sticky=tk.NW,padx=5,pady=5)
# rn.grid(row=0,column=1,sticky=tk.NW,padx=5,pady=5)
# rn1.grid(row=1,column=1,sticky=tk.NW,padx=5,pady=5)

# rn2.grid(row=2,column=1,sticky=tk.NW,padx=5,pady=5)
# bt.grid(row=3,column=1,sticky=tk.NW,padx=5,pady=5)


# app.mainloop()


# show image in page with the help of tkinter\\\\\\\\\\\


# import tkinter as tk
# from PIL import Image,ImageTk

# app = tk.Tk()



# app.geometry("500x700")
# app.title("Thar Introductions..")

# i = Image.open("front-left-side-47.webp")
# ig = ImageTk.PhotoImage(i)


# l = tk.Label(app,image=ig)
# l.pack(fill="y")



# ll = tk.Label(app,text="THAR INFO...",font=30)
# ll.pack()
# l1 = tk.Label(app,text='''The Mahindra Thar has 2 Diesel Engine
#                and 1 Petrol Engine on offer. The Diesel engine is 2184
#                cc and 1497 cc while the Petrol engine is 1997 cc .
#                It is available with Automatic & Manual transmission
#               .Depending upon the variant and fuel
#                type the Thar has a mileage of 15.2 kmpl''')
# l1.pack()


# l2 = tk.Label(app,text="Mahindra Thar on road price in Himachal Pardesh..",font=50)
# l2.pack(padx=10,pady=10)
# l3 = tk.Label(app,text='''AX Opt 4-Str Hard Top Diesel RWD(Diesel) (Base Model)
              
#                     Ex-Showroom PriceRs.10,98,000
              
#                     RTORs.1,42,740 Insurance Rs.53,164 OthersRs.10,980
              
#                     On-Road Price in Himachal Pardesh :Rs.13,04,884*
              
#                     EMI: Rs.24,847/month
#                      ''')
# l3.pack()


# b4 = tk.Button(app,text="Booking here")
# b4.pack()
# 
# app.mainloop()


import tkinter as tk

# def on_button_click(event):
#     text = event.widget.cget("text")

#     if text == "=":
#         try:
#             result = str(eval(screen.get()))
#             screen.set(result)
#         except Exception as e:
#             screen.set("Error")
#     elif text == "C":
#         screen.set("")
#     else:
#         screen.set(screen.get() + text)

# app = tk.Tk()
# app.title("Calculator with Ayush")
# app.geometry("400X500")



# screen = tk.StringVar()
# enty = tk.Entry(app,font=" lucida 20", bd=10,  width=14, )
# enty.grid(row=0, column=0)

# buttons = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     'C', '0', '=', '+'
# ]

# row_val = 1
# col_val = 0

# for button in buttons:
#     butonframe = tk.Frame(app, relief=tk.RIDGE, borderwidth=1)
#     butonframe.grid(row=row_val, column=col_val)

#     buttnwidget = tk.Button(button_frame, text=button, font='lucida 20', height=2, width=4)
#     buttnwidget.pack(expand=True, fill='both')

#     buttnwidget.bind("<Button-1>", on_button_click)

#     col_val += 1
#     if col_val > 3:
#         col_val = 0
#         row_val += 1

# app.mainloop()



# import tkinter as tk

# app = tk.Tk()

# app.geometry("400x400")

# app.title("Calculator with Ayush")

# l = tk.Label(app,text="Calculator",font=10,background="grey")
# l.pack(side="top")

# f = tk.Frame(app,background="grey",borderwidth=10,relief="sunken")
# f.pack(fill="x",pady=2)

# e = tk.Entry(f,font=30)
# e.pack(fill="x")

# app.mainloop()



from tkinter import *

win = Tk() # This is to create a basic window
win.geometry("312x324")  # this is for the size of the window 
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("Calculator")

###################Starting with functions ####################
# 'btn_click' function : 
# This Function continuously updates the 
# input field whenever you enter a number

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
 
expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
 
input_text = StringVar()
 
# Let us creating a frame for the input field
 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
#Let us creating another 'Frame' for the button below the 'input_frame'
 
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
 
btns_frame.pack()
 
# first row
 
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row
 
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
 
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
win.mainloop()












