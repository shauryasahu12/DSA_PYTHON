#Brute Force
# n = 10
# num = n
# result = []
# for i in range(1,num+1):
#     if num%i==0:
#         result.append(i)

# print(result)

#Better solution
# n = 10
# num = n
# result = []
# for i in range(1,num//2+1):
#     if num % i == 0:
#      result.append(i)

# result.append(num)
# print(result)

#optimal solution square root method
from math import sqrt
n = 10
num = n
result = []
for i in range(1,int(sqrt(num))):
    if num % i == 0:
        result.append(i)
        result.append(num//i)

print(result)