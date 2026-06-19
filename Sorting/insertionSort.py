#arrange in decending order
def insertionSort(num):
    n = len(num)
    for i in range(1,n):
        key = num[i]
        j = i-1
        while j>=0 and num[j] < key:
            num[j+1] = num[j]
            j -= 1
        num[j+1] = key

num = [5, 3, 6, 1, 4]
insertionSort(num)
print(num) 