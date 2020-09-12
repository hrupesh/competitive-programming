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

stack = [""]

for i in q:
    if(i[0] == 1):
        S += i[1]
        stack.append(i[1])
    elif(i[0] == 2):
        d = int(i[1])
        S = S[:-d]
        # stack.append(S[:-d])
    elif(i[0] == 3):
        k = int(i[1])
        if(len(S) > k-1):
            print(S[k-1])
    else:
        print("Before pushing:",S,stack)
        S = stack.pop()
        print("In else:",S,stack)


# print(S, stack)
