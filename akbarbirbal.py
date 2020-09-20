n = int(input())
for _ in range(n):
    sticks = []
    sticks_n = int(input())
    for _ in range(sticks_n):
        s = int(input()).split('')
        sticks.append(s)

print(sticks)
print(sticks_n)
