matrix = []
for i in range(5):
    m = input()
    matrix.append(m)

index_y= 1

for i in matrix:
    if("1" in i):
        print(index_y)
    index_y = index_y + 1

print(matrix)
