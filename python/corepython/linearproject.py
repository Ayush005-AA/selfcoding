from tkinter import *

def check_pack():
    print ("Checking")

app = Tk()

app.geometry("500x500")

l = Label(app,text="Check your package" , font = "itallic 25")
# l.pack()


l1 = Label(app,text = "Enter CGPA :", font= "bold 15 ")
# l1.pack(ipadx=1,ipady = 10)


entr = Entry(app,font=("cursive",))
# entr.pack(ipadx=1,ipady = 4)


ck = Checkbutton()

# ck.pack()

btn = Button(app,text="Checkpackages", font = "italic 10" , command=check_pack)
# btn.pack(pady=20)
l.grid(row=0, column=1, pady=10 , padx=20)
l1.grid(row=1, column=0 , pady=10)
entr.grid(row=1, column=1 , pady=10)
btn.grid(row=4, column=1 , pady=10)






app.mainloop()


