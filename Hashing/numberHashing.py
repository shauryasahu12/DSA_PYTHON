n =[5,3,2,2,1,5,5,7,5,10]
m =[10,111,1,9,5,67,2]

hash_list = [0]*11

for num in n:
    hash_list[num] +=1

for num in m:
    if num <0 or num >10:
        print(0)

    else:
        print(hash_list[num])

#usnig dictonary
# freq = {}
# num = len(n)

# for i in range(0,num):
#     freq[n[i]] = freq.get(n[i],0)+1
#     print(freq)

# for j in m:
#     if j<0 or j>10:
#         print(0)

#     else:
#         print(freq.get(j,0))