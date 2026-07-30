def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element found

    return -1  # Element not found


# Driver Code
numbers = [10, 25, 30, 45, 50, 60]
target = 45

result = linear_search(numbers, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")