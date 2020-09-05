k, n, w = input().split()
k = int(k)
n = int(n)
w = int(w)

total = 0

for i in range(w):
    total = total + k*(i+1)

# print(total)

if(total == 1 or n > 100000000 or total < 0):
    print(0)
else:
    print(total - n)
