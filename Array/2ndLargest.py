arr = [22,4,2,5,33,5,3,45,22]

# def s_largest(arr):
#     n = len(arr)
#     largest = float("-inf")
#     s_largest = float("-inf")

#     for i in range(0,n):
#         if arr[i] > largest:
#             largest = arr[i]

#     for i in range(0,n):
#         if arr[i] > s_largest and arr[i] != largest:
#             s_largest = arr[i]

#     return s_largest

# print(s_largest(arr))

#OPTIMAL
def s_largest(arr):
    largest =float("-inf")
    s_largest =float("-inf")
    n = len(arr)

    for i in range(0,n):
        if arr[i] > largest:
            s_largest = largest
            largest = arr[i]
        
        elif arr[i] > s_largest and arr[i] != largest:
             s_largest = arr[i]

    return s_largest

print(s_largest(arr))