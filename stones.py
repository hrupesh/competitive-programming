n = input()

n = int(n)

stones = input()

steps = 0

for i in range(len(stones)):
    # print(i, stones[i])
    if(i < len(stones) - 1 and i > 0):
        if(stones[i] != stones[i+1] and stones[i] != stones[i-1]):
            # print(0)
            break

    if(i < len(stones) - 1):
        if(stones[i] == stones[i+1]):
            # print(stones[i], steps)
            steps = steps + 1

print(steps)
