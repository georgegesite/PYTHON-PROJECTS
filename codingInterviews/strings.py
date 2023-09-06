s = "abc"

print(s[0:2])

# So this creates a new string
s += "def"
print(s)

# Valid numeric strings can be converted
print(int("123") + int("123"))

# And numbers can be converted to strings
print(str(123) + str(123))

# In rare cases you may need the ASCII value of a char
print(ord("a"))
print(ord("b"))

# Combine a list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))