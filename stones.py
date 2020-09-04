n = input()

n = int(n)

stones = input()

steps = 0

for i in range(len(stones)):
    # print(i, stones[i])
    if(i < len(stones) - 1 and i > 0):
        if(stones[i] != stones[i+1] and stones[i] != stones[i-1]):
            print(0)
            break
        elif(stones[i] == stones[i+1] or stones[i] == stones[i-1]):
            steps = steps + 1

print(steps)