def printname(name):
    print(name)
    
printname("Benji")
Benji
def printname(*name):
    print(name)
    
printname("Benjamin", "Tony", "Bill")
('Benjamin', 'Tony', 'Bill')
def printname(*name):
    print(name[0])
    
printname("Tom", "Bill", "Matt")
Tom
def printname(name,age):
    print(name)
    print(age)
    
printname("Benji", 39)
Benji
39
