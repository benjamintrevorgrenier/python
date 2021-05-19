file = open('C:/users/PC56/Desktop/ggg.txt', 'r')
file.read()
'hi how are you'
file.readline()
''
file.seek(0)
0
file.readline()
'hi how are you\n'
file.seek(0)
0
file.readlines()
['hi how are you\n', 'I am great\n', 'I like to code\n', 'I am me']
file.seek(0)
0
listdata = file.readlines()
listdata
['hi how are you\n', 'I am great\n', 'I like to code\n', 'I am me']
listdata[2] = "third line edited"
file.close()
file = open('C:/users/PC56/Desktop/ggg.txt')
