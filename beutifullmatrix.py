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


def calc_i():
    if(pos_i == 1 or pos_i == 5):
        return 2
        print("In 1 5  for i")
    elif(pos_i == 2 or pos_i == 4):
        return 1
        print("In 2 4 for i")
    else:
        return 0


def calc_y():
    if(pos_y == 0 or pos_y == 8):
        return 2
        print("In 0 8 for y")
    elif(pos_y == 2 or pos_y == 6):
        return 1
        print("In 2 6 for y")
    elif(pos_y == 4):
        return 0
        print("In 4 for y")
    else:
        pass
        print("In else for y")


moves_i = calc_i()
moves_j = calc_y()

moves = moves_i + moves_j

print(moves)

# print(matrix)
