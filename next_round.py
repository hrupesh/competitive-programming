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
    # print(i)
    if(i >= l and i != 0):
        advanced = advanced + 1

print(advanced)

# print(contestants)
