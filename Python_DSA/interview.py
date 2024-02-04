input =input("Enter String: ")
output = ""
count = 1
for i in range(0,len(input)):
    print(input[i])
    if input[i] == input[i+1]:
        count = count + 1
    else:
        output = output + str(count) + input[i]
        count = 1
print(output)