def left_rotation(arr, d):
    n = len(arr)
    d = d % n  # Ensure d is within the range of array size

    rotated = arr[d:] + arr[:d]
    print(arr[d:])
    print(arr[:d])
    return rotated

# Example usage
original_array = [1, 2, 3, 4, 5]
rotation_steps = 2
result = left_rotation(original_array, rotation_steps)
print(result)  # Output: [3, 4, 5, 1, 2]
