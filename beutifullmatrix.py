matrix = []
for i in range(5):
    m = input()
    matrix.append(m)

pos_i = 1
pos_y = 0

for i in matrix:
    if("1" in i):
        print(pos_i)
        # print(i.find("1"))
        pos_y = i.find("1")
        print(pos_y)
    pos_i = pos_i + 1

moves = 0

if(pos_i == 1 or pos_i == 5):
    moves = 2
    print("In 1 5  for i")
elif(pos_i == 2 or pos_i == 4):
    moves = 1
    print("In 2 4 for i")
elif(pos_i == 3):
    pass
    print("In 3 for i")
else:
    pass
    print("In else for i")

if(pos_y == 0 or pos_y == 8):
    moves = moves + 2
    print("In 0 8 for y")
elif(pos_y == 2 or pos_y == 6):
    moves = moves + 1
    print("In 2 6 for y")
elif(pos_y == 4):
    pass
    print("In 4 for y")
else:
    pass
    print("In else for y")

print(moves)

# print(matrix)
