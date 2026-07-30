def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Driver Code
numbers = [12, 11, 13, 5, 6]

print("Original Array:", numbers)
print("Sorted Array:", insertion_sort(numbers))