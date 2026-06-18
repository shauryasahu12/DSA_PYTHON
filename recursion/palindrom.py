s="ANBCDDCBNA"

def func(s,l,r):
    if l >= r:
        return True
    
    elif s[l] != s[r]:
        return False
    
    return func(s,l+1,r-1)

print(func(s,0,len(s)-1))

    
