n, m = input().split()
n = int(n)
m = int(m)

a = input()

# print(a)

a = [int(i) for i in a.split()]

# print(a)

new_a = a

# for i in range(len(a)):
#     # print(a[i],i)
#     if(i % 2 == 0):
#         new_a.append(int(a[i]))

# print(new_a)


def move(moves):
    for i in range(n):
        # print(i+1)
        moves = moves + 1
        if(i+1 == new_a[0]):
            if(len(new_a) > 1):
                if(i+1 == new_a[1]):
                    # print("Popping same consecutive")
                    new_a.pop(1)
            new_a.pop(0)
            # print(new_a)
            if(len(new_a) == 0):
                return moves

    if(len(new_a) == 0):
        return moves
    # else:
    #     move(moves)

    return move(moves)


mo = move(0)
print(mo-1)

# print(new_a)

# print(a)
