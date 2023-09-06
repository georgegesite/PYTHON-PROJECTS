# Get all factors of n
# O( sqrt(n) )

import math
n = 12
factors = set()
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        factors.add(i)
        factors.add(n // i)

print(factors)
