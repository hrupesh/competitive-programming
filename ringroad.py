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
        # if()
        moves = moves + 1

    if(moves == n):
        return moves
    move(moves)


moves = move(0)
print("Moves made : "+str(moves))

print(a)
