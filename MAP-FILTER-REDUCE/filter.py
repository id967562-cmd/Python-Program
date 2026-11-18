#filter:- select only those items that satisfy a condition form an iterable , such as list.
#filter(function,iterable)

def is_adult(age):
    return age >= 18

ages = [12,17,18,22,15,25]

adults = list(filter(is_adult,ages))
print(adults)