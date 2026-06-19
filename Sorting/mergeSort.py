arr = [2,5,3,6,9,4,7,6,555,6,33]

def mergeArray(left,right):
    n,m = len(left),len(right)
    i,j =0,0
    result = []

    while i<n and j<m:
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    while i<n:
        result.append(left[i])
        i+=1

    while j<m:
        result.append(right[j])
        j+=1

    return result

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    
    mid_index = len(arr)//2
    left_half = arr[:mid_index]
    right_half = arr[mid_index:]

    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    return mergeArray(left_half,right_half)

print(mergeSort(arr))
    
