k, n, w = input().split()
k = int(k)
n = int(n)
w = int(w)

total = 0

for i in range(w):
    total = total + k*(i+1)

print(total)

needed = total - n

if(total == 1 or needed < 0):
    print(0)
else:
    print(needed)
