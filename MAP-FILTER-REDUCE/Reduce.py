# reduce():- used to combine all items in an iterable into a single result

from functools import reduce 
nums = [2,3,4]

result = reduce(lambda a,b : a*b,nums)
print(result)

from functools import reduce
nums = [10,20,30,40]
result = reduce(lambda a,b:a+b , nums)
print(result)