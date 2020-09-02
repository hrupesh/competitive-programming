n, k = input().split()
# contestants = []
n = int(n)
k = int(k)
contestants = (input().split())
advanced = 0
l = int(contestants[k])
# print(l)

for i in contestants:
    i = int(i)
    if(i >= l):
        advanced = advanced + 1

print(advanced)

# print(contestants)
