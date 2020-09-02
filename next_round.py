n, k = input().split()
# contestants = []
n = int(n)
k = int(k)
contestants = (input().split())
advanced = 0
try:
    l = int(contestants[k])
# print(l)
except:
    print("Error")

for i in contestants:
    i = int(i)
    # print(i)
    if(i >= l and i != 0):
        advanced = advanced + 1

print(advanced)

# print(contestants)
