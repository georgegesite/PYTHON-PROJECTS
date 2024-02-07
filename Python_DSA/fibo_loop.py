prev2 = 1
prev1 = 0

print(prev2)
print(prev1)
for fibo in range(11):
    newFibo = prev1 + prev2
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo