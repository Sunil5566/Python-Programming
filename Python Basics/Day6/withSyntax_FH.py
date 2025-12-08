#Practice to use with syntax in file handling in python
with open("demo.txt", "r") as f:
    print(f.read())

with open("demo.txt", "w") as w:
    w.write("I am writing for with syntax")

with open("demo.txt", "r") as f:
    print(f.read())

#To delete file in python..we first have to import os in our file..then syntax for deleting is 
# os.remove(filename)  
import os
os.remove("demo.txt")  

    
