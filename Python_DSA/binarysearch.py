def binary_search(list, target):
    first = 0
    last = len(list)-1
    
    while first <= last:
        midpoint = (first + last)//2
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1

    return None
list = [1,2,3,4,5,6,7,8,9,10]
target = 8
print(binary_search(list, target))

# The key steps it follows are:

# Initialize bounds of search space (first and last indices)

# Calculate midpoint index from bounds

# Compare midpoint value to target

# Adjust bounds based on comparison

# Repeat steps 2-4 until target found or bounds collapse