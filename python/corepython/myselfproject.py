# import pyttsx3

# e = pyttsx3.init()

# text = "What is your name.."

# ip = input("Please enter your name..")

# e.say(text)
# e.say(ip)
# e.runAndWait()

# print(f"{text}\n{ip}")


# from sketchpy import library as lib

# obj = lib.rdj()
# obj.draw()



a = int(input("Enter a number.."))
b = int(input("Enter a second number.."))

print("what you want to do..")

print("""
1 = addtions
2 = subtraction
3 = division """)


userchoice = int(input("choose a number.."))

if userchoice == 1:
    print(f"output is {a+b}")


elif userchoice == 2:
    print(f"output is {a-b}")


elif userchoice == 3:
    print(f"output is {a/b}")


else:
    print("not defined.")
