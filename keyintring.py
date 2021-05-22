string = input("Enter a long string: ")
key = input("Enter the letter to search for: ")
if(key in string):                  #Checks if key is in the string
    print("Letter found in string") #If the Bool value is TRUE
else:
    print("Letter not found in string")
input("Press enter to exit")
