with open("someFile.txt","r") as file:
    contains = file.read() #causes error

with open ("anotherFile.txt","r",encoding="latin-1" ) as file:
    insideFile = file.read()