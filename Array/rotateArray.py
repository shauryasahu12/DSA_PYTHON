arr = [2, 4, 2, 5, 2, 442, 22]
k = 5
n = len(arr)

def rotate(arr, k):
    k = k % n                         

    def reverse(arr, left, right):     
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1                 

    reverse(arr, 0, n - k - 1)        
    reverse(arr, n - k, n - 1)
    reverse(arr, 0, n - 1)

    return arr

print(rotate(arr, k))                 