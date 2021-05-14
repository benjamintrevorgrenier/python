name = (input("What is your name? "))
def Greeting(name):
    print("Hi " + name + "!")
Greeting(name)

feeling = int(input("Out of 1-10, how are you feeling today?: "))
if feeling >= 8 and feeling <= 10:
    print("WOW! That is great to hear")
elif (feeling > 5 and feeling < 8):
    print("Keep on trucking!")
elif (feeling >=0 and feeling < 5):
    print("I am sorry to hear that")
else:
    print("ERROR: You have not made a valid entry!")
