n = int(input())

q = []

S = ""

for i in range(n):
    try:
        t, w = input().split()
    except ValueError:
        t = 4
        w = "Undo"
    t = int(t)
    q.append([t, w])

for i in q:
    print(i[0], i[1])
