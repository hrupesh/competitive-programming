n = input()
n = int(n)
stones = input()
steps = 0

for i in range(len(stones)):
    if(i < len(stones)-1):
        if(stones[i] == stones[i+1]):
            steps = steps + 1

    if(i < len(stones) - 1 and i > 0):
        if(stones[i] != stones[i+1] and stones[i] != stones[i-1]):
            pass

print(steps)
