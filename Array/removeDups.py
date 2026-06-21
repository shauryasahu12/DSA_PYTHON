arr = [1,1,1,2,3,4,4,7,9,9,9,10]
def duplicate(arr):
    n = len(arr)
    i=0

    for j in range(1,n):
            if arr[j] != arr[i]:
                i+=1
                arr[i] = arr[j]
    
    return i+1

print(duplicate(arr))

            