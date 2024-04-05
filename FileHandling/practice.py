

file = open('demoFile.txt', 'r')
str1 = file.read(30)
print(str1)

file.write('Goodbyess')
file.close()