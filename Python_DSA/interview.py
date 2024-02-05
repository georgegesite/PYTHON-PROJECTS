def sayWhatYouSee(test):

  count = 1
  encoded = ""
  for i in range(len(test)):
    print(i)

  for i in range(len(test)):
    if i < len(test) - 1 and test[i] == test[i+1]:
      count += 1
    else:
      encoded += str(count) + test[i]  
      count = 1

  return encoded

test = "AAAABBCCC"
print(sayWhatYouSee(test))
