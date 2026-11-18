#Build in Modules
import math

print(math.sqrt(16))
print(math.sqrt(49))

import random
print(random.randint(4,10))

#User-defined Modules
import Calc
print(Calc.add(10,20))
print(Calc.substract(50,30))

#External(Third-Party)Modules:
import requests
r = requests.get("https://example.com")
print(r.status_code)


