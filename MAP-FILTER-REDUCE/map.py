#map() --> Transform every item

nums = [1,2,3,4,5]

def square(n):
    return n*n

#map(function,iterable)
result = map(square,nums)
print(list(result))

