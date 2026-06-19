n = 121
num = n
result = 0

while num>0:
    ls = num%10
    result = (result*10)+ls
    num = num//10

if result == n:
    print("It is a palindrome")

else:
    print("It is not a palindrom")