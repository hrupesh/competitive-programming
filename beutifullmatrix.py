matrix = []
for i in range(5):
    m = input()
    matrix.append(m)

index_y = 1
index_x = 0

for i in matrix:
    if("1" in i):
        print(index_y)
        # print(i.find("1"))
        index_x = i.find("1")
        print(index_x)
    index_y = index_y + 1

moves = 0

if(index_x == 1 or index_x == 5):
    moves = 2
elif(index_x == 2 or index_x == 4):
    moves = 1
elif(index_x == 3):
    moves = 0
else:
    moves = 0

if(index_y == 0 or index_y == 8):
    moves = moves + 2
elif(index_y == 2 or index_y == 6):
    moves = moves + 1
elif(index_y == 4):
    pass
else:
    pass

print(moves)

# print(matrix)
