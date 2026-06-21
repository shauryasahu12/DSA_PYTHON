arr = [22,4,2,5,33,5,3,45,22]

def largest(arr):
    n = len(arr)
    largest = float("-inf")

    for i in range(0,n):
        if arr[i] > largest:
            largest = arr[i]

    return largest

print(largest(arr))