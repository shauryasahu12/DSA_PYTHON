matrix = [[5,20,3],[7,-10,9],[1,-52,6]]
rows = len(matrix)
cols = len(matrix[0])

for i in range(0,rows):
    for j in range(0,cols):
        print(matrix[i][j],end=" ")
    print()