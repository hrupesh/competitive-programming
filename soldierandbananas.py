k, n, w = int(input()).split()

total = 0

for i in range(w):
    total = total + k*n+1

print(total)

print(k, n, w)
