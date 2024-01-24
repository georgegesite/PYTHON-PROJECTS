a = 10
b = 20
def my_function():
    global a
    a = 11
    b = 21
    a = b + a

my_function()
print(a)
print(b)
