grade = int(input("Enter the score from your math test: "))
if grade >= 90 and grade <= 100:
    print("You got an A")
elif (grade >= 75 and grade < 90):
    print("You got a B")
elif (grade >= 51 and grade < 75):
    print("You got a C")
elif (grade >= 35 and grade < 51):
    print("You got a D")
elif (grade >= 25 and grade < 35):
    print("You got an E")
elif (grade >= 0 and grade < 25):
    print("You are a dumb ass!!!")
else:
    print("You have not entered a correct score format. Scores must be between 0-100")
