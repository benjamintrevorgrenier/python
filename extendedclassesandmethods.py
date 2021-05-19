class class1:
    var1="I am class 1"
    
class class2:
    var2="I am class 2"
    
class class3:
    var3="I am class 3"
   
class class5(class1,class2):
    var5="I am class 5"
    
example = class5()
example.var1
'I am class 1'
example.var2
'I am class 2'
example.var5
'I am class 5'
