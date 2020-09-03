matrix = []
for i in range(5):
    m = input()
    matrix.append(m)

index_y= 1
index_x= 0

for i in matrix:
    if("1" in i):
        print(index_y)
        # print(i.find("1"))
        index_x = i.find("1")
        print(index_x)
    index_y = index_y + 1

# print(matrix)
