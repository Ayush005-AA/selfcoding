# import re
# pattern = "my"

# text = "my name is ayush, my age  22 years old "

# match = re.findall(pattern,text)

# print(match)

# import re

# text = """I m Vipul Konar, and I am 17 years old.
# I study at Delhi Public School in the fourth standard.
# My father's name is Mr. Adhitya Konar, and my mother's name is Mrs. Alar Konar.
# my father age is 30 and my mother age is 38 years old.
# I have one younger sister who studies in the first standard in the same school.
# I like watching cartoons, and my favorite cartoon character is Sinchan.
# I also love playing Indoor games with my sister. And, I love playing cricketwith my friends.
# I am a very honest and decent boy and follow all the instructions from my parents and teachers.
# I complete my homework regularly and never get late to school.
# I pay attention and respect to my teachers and elders. Also, I follow every piece of advice from them.
# I try to help my mother and father by keeping all the toys at the right place after playing with them."""

# patrn = "my"

# match = re.findall(patrn,text)
# print(match)

# import re

# a = "my name is ayush and i love ayushi.don't love ayurshi"
# b = "my father name is Kamlesh kumar"
# c = "my mother name is sumana devi"
# d = "my brother name is akshay dhiman"
# e = "my gmail id is ayush12323@gmail.com"
# f = "my phone number is 1223355555"
# g = "my USA phone number is (1234)-653-2005-2001"

# match = re.findall(r"\(\d{4}\)\-\d{3}\-\d{4}\-\d{4}",g)

# match = re.findall(r"\d",f)

# print(match)

# ::::::::::::Reg ex sets::::::::::::::::

# import re

# a = "ayush20  dhiman @67557 # $ %"

# match = re.findall(r"\B",a)
# print(match)


import re

txt = """Im Vipul Konar, and I am 7 years old.
I study at Delhi Public School in the fourth standard.
My fathers name is Mr. Adhitya Konar, and my mothers name is Mrs. Alar Konar my father phone number is 9874561231.
I have one younger sister who studies in the first standard in the same school acvv125@gmail.com.
I like watching cartoons, and my favorite cartoon character is Sinchan.
I also love playing Indoor games with my sister. And, I love playing cricketwith my friends AAjjs22@gmail.com 
I am a very honest and decent boy and follow all the instructions from my parents and teachers.
I complete my homework regularly and never get late to school.
I pay attention and respect to my teachers and elders. Also, I follow every piece of advice from them.
I try to help my mother and father by keeping all the toys at the right place after playing with them"""

# paten = "[a-zA-Z0-9]+[@][a-z]+[.]+[a-z]{3}"
# patrn = "\d{10}"
# patrn = "I"
# match = re.search(patrn,"my",txt)
patrn = "I"
match = re.findall(patrn,txt)
print(match)