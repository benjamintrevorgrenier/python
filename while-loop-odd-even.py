while True:
    d1a = input("Pick Odd or Even: [ODD/EVEN]? : ")
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [number for number in a if number % 2 == 0]
    c = [number for number in a if number % 2 != 0]
    # check if d1a is equal to one of the strings, specified in the list
    if d1a in ['ODD', 'EVEN']:
        # if it was equal - break from the while loop
        break
# process the input
if d1a == "ODD":
    print(c)
elif d1a == "EVEN":
    print(b)
