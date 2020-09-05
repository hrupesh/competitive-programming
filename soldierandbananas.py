k, n, w = input().split()
k = int(k)
n = int(n)
w = int(w)

total = 0

for i in range(w):
    total =  k*i+1
    print(total,i)

print(total)

print(k, n, w)
