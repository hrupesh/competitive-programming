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
        print("In 1 5  for i")
        return 2
    elif(pos_i == 2 or pos_i == 4):
        print("In 2 4 for i")
        return 1
    else:
        return 0


def calc_y():
    if(pos_y == 0 or pos_y == 8):
        print("In 0 8 for y")
        return 2
    elif(pos_y == 2 or pos_y == 6):
        print("In 2 6 for y")
        return 1
    elif(pos_y == 4):
        print("In 4 for y")
        return 0
    else:
        print("In else for y")
        pass


moves_i = calc_i()
moves_j = calc_y()

moves = moves_i + moves_j

print(moves)

# print(matrix)
