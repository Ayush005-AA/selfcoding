# a = {"name":"kriss","age":20,"phone":9852695296,
#      "car":"bmw"}

# print(list(dict.keys(a)))
# print(list(dict.values(a)))


a = 1234
dd = str(a)
b = 0

for i in dd:
    b = b + int(i)

print(b)

# # ~


# a = 10
# a = a+a+a+a+a+a+a+a+a+a+a
# b = len("oo")
# print((a-b))

# a= ["hello","hyyy","car","bike","tharr"]

# for i in a:
#     if i 
        
# x = [i if i%2!=0 else str(i)*i for i in range(
#    0,11)]
# print(x)       
            
# for i in range(0,11):
#    if 2 >=1:

#       if i %2 ==0:
#        print(i)

import re

txt = """In today's digital age, communication has evolved significantly. Gone are the days when sending a letter via postal mail was the primary means of conveying information. Instead, we now rely heavily on electronic communication. Here are some example email addresses that illustrate the diversity of email domains and formats:

John.Doe@example.com is a classic email address format with a straightforward name and a generic domain.
In contrast, alice_smith1234@gmail.com reflects the popular use of email services like Gmail, known for its user-friendly interface and large storage capacity.

info@company.co.uk demonstrates a business-oriented email with a UK domain, emphasizing the global reach of email communication.
In today's interconnected world, support@my-website.io is essential for any online business, ensuring customers can easily seek assistance.

contact_me@subdomain.example.net exemplifies the use of subdomains, a common practice for organizing different sections of a website.

webmaster@another-site.org is a classic technical email address often responsible for maintaining website functionality.

marketing@company-name.biz highlights the role of email in marketing strategies and its potential impact on businesses.

sales@domain_name.museum is a unique address showcasing how even museums use email for ticket sales and event promotions.

help@myapp.travel caters to travelers seeking assistance with travel apps, underlining the versatility of email for various industries.

contact@local-organization.jobs reflects the importance of email in the job application and hiring process.

The convenience and speed of email have transformed the way we interact personally and professionally. Whether you're sending a quick message to a friend or conducting business negotiations, email addresses
"""



ptrn = "[A-z.@a-z\d{4}]+[@]+[a-z.-_]+[a-z-+.{3}]+"

mtch = re.findall(ptrn,txt)
print(mtch)


# a = 6562

# c  = str(a)
# b = 0
# for i in c:
#     b = b+int (i)
# print(b)


# class employee:

#     company = "google"

# ayush = employee()
# print(ayush.company)
# employee.company = "you tube"
# print(ayush.company)


# import tkinter as tk

# app = tk.Tk()

# app.geometry("400x400")
# app.title("My form")
# app.configure(background="yellow")

# lb= tk.Label(app,text="Name:",font=("robort","bold",10))
# lb1= tk.Label(app,text="Phone No:",font=("robort","bold",10))
# lb2= tk.Label(app,text="Email Id:",font=("robort","bold",10))


# rn = tk.Entry(app,font=("robort","italic",10))
# rn1 = tk.Entry(app,font=("robort","italic",10))
# rn2= tk.Entry(app,font=("robort","italic",10))

# bn = tk.Button(app,text="submit",font=("robort","bold",10))











# app.mainloop()








    













