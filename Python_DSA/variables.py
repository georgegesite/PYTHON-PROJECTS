a = 10 # a is assigned an integer value
b = 20 # b is assigned an integer value 

def my_function():
    global a # global keyword declares a as a global variable
    a = 11 # updates the global a to 11
    b = 21 # updates local b to 21  
    a = b + a # updates local a to the sum of global a and local b

my_function() 
print(a) # prints the updated global a 
print(b) # prints the original b which was not updated

# The bool class
isValid = True
if isValid:
    print('This Statement is Valid')

# The int class
#The integer constructor, int( ), returns value 0 by default
intConstructor = int()
print(intConstructor) #prints 0

# print(int('helloworld'))

print(int('1234')) #prints 1234

print(int( '7f' , 16)) #evaluates to the integer 127.
