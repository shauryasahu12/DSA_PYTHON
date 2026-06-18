num = [5, 7, 3, 2, 6, 1, 5, 9]

def reverseArray(nums,l,r):
    
    _reverse(num,l,r)
    return num

def _reverse(num,l,r):
    if l>=r:
        return
    num[l],num[r] = num[r],num[l]
    _reverse(num,l+1,r-1)

print(reverseArray(num,0,7))