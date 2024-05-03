list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
matrix = [[0]*4 for _ in range(4)]
row = 0
col = 0
r = 0

while True:
    if row <= 3 and col <= 3:
        print(row)
        matrix[row][col] = list1[r]
        r += 1
        row += 1
        col += 1
    else:
        break

print(matrix)