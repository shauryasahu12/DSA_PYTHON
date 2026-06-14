#print 1 to N using recursion
def func1(x,n):
    if x > n:
        return
    print(x)
    func1(x+1,n)

func1(1,10)

print("--------")

# #head recursion(backtracking)
def func2(x,n):
    if x>n:
        return
    func2(x+1,n)
    print(x)

func2(1,5)

print("--------")

#print 1 to N using head recursion(backtracking) in acending order
def func3(x,n):
    if x > n:
        return
    func3(x+1,n)    
    print(n - x+1) 

func3(1,10)