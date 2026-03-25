def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

n = int(input("Enter number of elements: "))
arr = [int(input()) for i in range(n)]

print("1. Linear Search")
print("2. Binary Search")

choice = int(input("Enter choice: "))
key = int(input("Enter element to search: "))

if choice == 1:
    result = linear_search(arr, key)
else:
    arr.sort()
    result = binary_search(arr, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")


