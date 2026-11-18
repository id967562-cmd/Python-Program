#Writeing a file
f = open("Student.txt","w")  #Making a file

f.write("Name:Sagar\n")
f.write("Marks:85")

f.close()

#Reading from a file
f = open("Student.txt","r")
data = f.read()
print(data)
print(f.readline()) #readline()-->Reads one line
print(f.readline()) #readlines()-->Reads all line into a list
f.close()

#Appending to a file
f = open("Student.txt","a")
f.write("\nCollage: Hrit")
f.close()

#with Statement 
#Instead of calling close(),use with open()
#Python automatically closes the file when the block finishes ,even if an exception occurs.

with open("Student.txt","w") as f:
    f.write("Hello, Python!")
