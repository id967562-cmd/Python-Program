#changing case
text='hello worLd\n'
print(text.upper())
print(text.lower())
print(text.capitalize()) # only first letter of word become capital

#Removing whitespaces
string=" hello world \n"
print(string.strip())
print(string.lstrip())
print(string.rstrip())

#Finding and Replacing 
x="Python is fun"
print(x.find("is"))# by using unicode
print(x.replace("fun","enjoying"))

#Splitting and joining
y="apple,banana,orange"
fruits=y.split(",")
print(fruits)

new_y='-'.join(fruits)
print(new_y)

#Checking string properties
z="Python123"
print(z.isalpha())
print(z.isalnum())
print(z.isdigit())
print(z.isspace())

#Build-in String function
sentence='Hello,Python!'
print(len(sentence))

print(ord('C'))
print(chr(69))

#Formatting and f-string
name="Alice"
age=34
print("My name is {} and i am {} years old".format(name,age))
print("My name is {name} and i am {age} years old".format(name='sagar',age=56))

#f-string
print(f"My name is {name} and I am {age} years old.")

#Padding and Alignment
q="Python"
print(f"{q:>10}") #right align
print(f"{q:<10}") #Left align
print(f"{q:^10}") #Center align

# important in string
list_of_string=["Hello","World"]
result=''.join(list_of_string)

t='Sagar'
convert_to_byte=t.encode()
print(type(convert_to_byte))
data=b"hello"
convert_to_str = data.decode()
print(type(convert_to_str))

