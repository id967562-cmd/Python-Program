#Tail Recursion
print("Tail-Recursion")
def fun(n):
    if n==0:                                 
     return 0
    else:
     print(n)
     return fun(n-1) 
 
fun(3)

print("\n")

#Non-Tail Recursion
print("Non-Tail Recursion")
def num(i):
  if i==0:
    return 0
  num(i-1)
  print(i)

num(3)

#Example of Recursion
print("\n")
def recursion(x):
  if x==1:
   return 0
  else:  
    return  1 + recursion(x//2)

print(recursion(8))
print(recursion(16))


