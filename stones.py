n = input()

n = int(n)

stones = input()

for i in range(len(stones)):
    print(i, stones[i])
    if(stones[i] != stones[i+1]):
        print(0)
