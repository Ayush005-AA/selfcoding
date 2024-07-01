# import tkinter as tk
# def click(event):
#     global scv
#     text = event.widget.cget("text")

#     print(text)
#     if text == "=":
#         scv.set()
#         sc.update()

#     elif text =="C":
#         scv.set("")
#         sc.update()
        

#     else:
#         scv.set(scv.get() + text)
#         sc.update()



# app = tk.Tk()

# app.geometry("400x650")
# scv = tk.StringVar()
# scv.set("")
# sc = tk.Entry(app,textvariable=scv,font="lucida 20 bold")

# sc.pack(padx=5,pady=5)
# app.title("Calculator with Ayush")

# f = tk.Frame(app,bg="grey")
# f.pack()
# b = tk.Button(f,text="9",padx=15,pady=15,font="lucida  15 bold")
# b1 = tk.Button(f,text="8",padx=15,pady=15,font="lucida  15 bold")
# b2 = tk.Button(f,text="7",padx=15,pady=15,font="lucida  15 bold")
# b.pack(side="left",padx=15,pady=15)
# b.bind("<Button-1>",click)
# b1.pack(side="left",padx=15,pady=15)
# b1.bind("<Button-1>",click)
# b2.pack(side="left",padx=15,pady=15)
# b2.bind("<Button-1>",click)

# f = tk.Frame(app,bg="grey")
# f.pack()

# b = tk.Button(f,text="6",padx=15,pady=15,font="lucida  15 bold")
# b1 = tk.Button(f,text="5",padx=15,pady=15,font="lucida  15 bold")
# b2 = tk.Button(f,text="4",padx=15,pady=15,font="lucida  15 bold")
# b.pack(side="left",padx=15,pady=15)
# b.bind("<Button-1>",click)
# b1.pack(side="left",padx=15,pady=15)
# b1.bind("<Button-1>",click)
# b2.pack(side="left",padx=15,pady=15)
# b2.bind("<Button-1>",click)

# f = tk.Frame(app,bg="grey")
# f.pack()

# b = tk.Button(f,text="3",padx=15,pady=15,font="lucida  15 bold")
# b1 = tk.Button(f,text="2",padx=15,pady=15,font="lucida  15 bold")
# b2 = tk.Button(f,text="1",padx=15,pady=15,font="lucida  15 bold")
# b.pack(side="left",padx=15,pady=15)
# b.bind("<Button-1>",click)
# b1.pack(side="left",padx=15,pady=15)
# b1.bind("<Button-1>",click)
# b2.pack(side="left",padx=15,pady=15)
# b2.bind("<Button-1>",click)

# f = tk.Frame(app,bg="grey")
# f.pack()

# b = tk.Button(f,text="0",padx=15,pady=15,font="lucida  15 bold")
# b1 = tk.Button(f,text="-",padx=15,pady=15,font="lucida  15 bold")
# b2 = tk.Button(f,text="*",padx=15,pady=15,font="lucida  15 bold")
# b.pack(side="left",padx=15,pady=15)
# b.bind("<Button-1>",click)
# b1.pack(side="left",padx=15,pady=15)
# b1.bind("<Button-1>",click)
# b2.pack(side="left",padx=15,pady=15)
# b2.bind("<Button-1>",click)

# f = tk.Frame(app,bg="grey")
# f.pack()

# b = tk.Button(f,text="/",padx=15,pady=15,font="lucida  15 bold")
# b1 = tk.Button(f,text="+",padx=15,pady=15,font="lucida  15 bold")
# b2 = tk.Button(f,text="=",padx=15,pady=15,font="lucida  15 bold")
# b.pack(side="left",padx=15,pady=15)
# b.bind("<Button-1>",click)
# b1.pack(side="left",padx=15,pady=15)
# b1.bind("<Button-1>",click)
# b2.pack(side="left",padx=15,pady=15)
# b2.bind("<Button-1>",click)

# f = tk.Frame(app,bg="grey")
# f.pack()

# b = tk.Button(f,text="C",padx=15,pady=15,font="lucida  15 bold")
# # b1 = tk.Button(f,text="8",padx=15,pady=15,font="lucida  15 bold")
# # b2 = tk.Button(f,text="7",padx=15,pady=15,font="lucida  15 bold")
# b.pack(side="left",padx=15,pady=15)
# b.bind("<Button-1>",click)



# app.mainloop()


from tkinter import *

app = Tk()
app.geometry("350x380")
app.title("Calculator with Ayush")

def btclick(item):
    global expression
    expression = expression + str(item)
    inptxt.set(expression)

def btclear():
    global expression
    expression = ""
    inptxt.set("")

def btequal():
    global expression
    re = str(eval(expression))
    inptxt.set(re)
    expression = ""


expression = ""
inptxt = StringVar()

input_frame = Frame(app, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2).grid()
 
# input_frame.pack(side=TOP)

 
inptfield = Entry(input_frame, font=('lucida', 18, 'bold'), textvariable=inptxt, width=50, bg="#eee", bd=0, justify=RIGHT).grid(row=0,column=0,ipady=10)
 
# inptfield.grid(row=0, column=0)
 
# inptfield.grid(ipady=10)
 
btns_frame = Frame(app, width=312, height=272.5, bg="grey")
 
btns_frame.grid()


clear = Button(app, text = "C", fg = "black",font="lucida 10 bold", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btclear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(app, text = "/", fg = "black",font="lucida 10 bold", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btclick("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

 
seven = Button(app, text = "7", fg = "black",font="lucida 10 bold", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btclick(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(app, text = "8", fg = "black",font="lucida 10 bold", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btclick(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(app, text = "9", fg = "black",font="lucida 10 bold", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btclick(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(app, text = "*", fg = "black",font="lucida 10 bold", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btclick("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 

 
four = Button(app, text = "4", fg = "black",font="lucida 10 bold", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btclick(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(app, text = "5", fg = "black",font="lucida 10 bold", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btclick(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(app, text = "6", fg = "black",font="lucida 10 bold", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btclick(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(app, text = "-", fg = "black",font="lucida 10 bold" ,width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btclick("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 

 
one = Button(app, text = "1", fg = "black",font= "lucida 10 bold", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btclick(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(app, text = "2", fg = "black",font="lucida 10 bold", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btclick(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(app, text = "3", fg = "black",font="lucida 10 bold", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btclick(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(app, text = "+", fg = "black",font="lucida 10 bold", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btclick("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
 
zero = Button(app, text = "0", fg = "black",font="lucida 10 bold", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btclick(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(app, text = ".", fg = "black",font="lucida 10 bold", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btclick(".")).grid(row = 4, column = 2, padx = 1, pady = 1)

equals = Button(app, text = "=", fg = "black",font="lucida 10 bold" ,width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btequal()).grid(row = 4, column = 3, padx = 1, pady = 1)

app.mainloop()

