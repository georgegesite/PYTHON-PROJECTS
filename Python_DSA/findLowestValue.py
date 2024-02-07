def findLowestValue(array):
    lowestValue = array[0]
    for i in range(1, len(array)):
        print(array[i])
        if array[i] < lowestValue:
            lowestValue = array[i]
    return lowestValue


array =[7, 12, 9, 4, 11]
print( findLowestValue(array))