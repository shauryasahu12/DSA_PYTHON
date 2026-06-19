class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        for i in range(n-2,-1,-1):
            is_swap = False
            for j in range(0,i+1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    
            if is_swap == False:
                break

arr = [1,2,3,4,5,8,]
Solution().bubbleSort(arr)
print(arr)