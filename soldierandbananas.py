k, n, w = input().split()
k = int(k)
n = int(n)
w = int(w)

total = 0

for i in range(w):
    total = total + k*(i+1)

# print(total)

if(total == n-1):
    print(total)
else:
    print(total - n)
