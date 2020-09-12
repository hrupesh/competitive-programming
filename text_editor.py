n = int(input())

q = []

S = ""

for i in range(n):
    t, w = input().split()
    t = int(t)
    q.append([t, w])

for i in q:
    print(i)
