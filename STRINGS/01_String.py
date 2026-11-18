print("SINGLE-LINE STRING\n")
a='GFG'
b="greeksForGeeks"
print(a)
print(b)

print("MULTI-LINE STRING\n")
s="""I am Learning
Python String on GeeksforGeeks"""
print(s)

s='''I'm a 
Geek'''
print(s)

z='ABCDEF'
print(z[0]) #Positive indices
print(z[4])
print(z[-6]) #Negative indices
print(z[-5])

#slicing
w='ABCDEF'
print(w[1:4])
print(w[2:5])
print(w[::-1])

#Loop through Strings
s="ABCDEF"
for char in s:
    print(char)

#string are immutable
s='aBCDEF'
s='A'+s[1:]
print(s)

#string deletion and updating
s="abc"
del s

s='ABCD EF'
s1="H"+ s[1:]
s2=s.replace("ABC","abc")

print(s1)
print(s2)