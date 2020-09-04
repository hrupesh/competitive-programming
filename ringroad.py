n, m = input().split()
n = int(n)
m = int(m)

a = input()

new_a = []

for i in range(len(a)):
    # print(a[i],i)
    if(i % 2 == 0):
        new_a.append(int(a[i]))

print(new_a)


def move(moves):
    for i in range(n):
        print(i+1)
        moves = moves + 1
        if(i+1 == new_a[0]):
            new_a.pop(0)
            print("Popping")
            if(len(new_a) == 0):
                return moves

     if(len(new_a) == 0):
                return moves
    else:
        move(moves)

    return moves


mo = move(0)
print("Moves made : ", mo-1)

print(new_a)

# print(a)
