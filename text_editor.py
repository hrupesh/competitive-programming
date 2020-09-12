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
        stack.append(S+i[1])
        S += i[1]
        # print("After Appending: ", S, stack)
    elif(i[0] == 2):
        d = int(i[1])
        S = S[:-d]
        stack.append(S[:-d])
        # print("After deleting: ", S, stack)
    elif(i[0] == 3):
        k = int(i[1])
        # print(S)
        print(S[k-1])
    else:
        S = stack.pop(len(stack)-2)
        # print("Undoing :", S, stack)


# print(S, stack)
