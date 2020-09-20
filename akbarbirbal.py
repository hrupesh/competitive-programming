n = int(input())
for _ in range(n):
    sticks_n = int(input())
    sticks = input().split()
    for i in range(sticks_n):
        sticks[i] = int(sticks[i])

print(sticks)
print(sticks_n)
