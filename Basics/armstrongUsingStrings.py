n = 153
digits = str(n)
count = len(digits)

total = sum(int(d) ** count for d in digits)

print(f"{n} is {'an' if total == n else 'not an'} Armstrong number")