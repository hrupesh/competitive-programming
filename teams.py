n = input()
n = int(n)
solved = 0
qs = []

for i in range(n):
    q = input()
    qs.append(q)
    if("1 1" in q or "1 0 1" in q ):
        solved = solved + 1
    # print(q)

print(solved)
