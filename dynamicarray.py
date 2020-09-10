n, q = input().split()

n = int(n)
q = int(q)
# print(n, q)

queries = []

for i in range(q):
    queries.append(input().split())

for i in range(len(queries)):
    for j in range(3):
        queries[i][j] = int(queries[i][j])

# print(queries)

lastAnswer = 0
answers = []
seqList = []
for i in range(n):
    seqList.append([])
for i in range(len(queries)):
    if (queries[i][0] == 1):
        x = queries[i][1]
        index = (x ^ lastAnswer) % 2
        seqList[index].append(queries[i][2])
    elif (queries[i][0] == 2):
        x = queries[i][1]
        index = (x ^ lastAnswer) % 2
        elem_index = queries[i][2] % len(seqList[index])
        lastAnswer = seqList[index][elem_index]
        answers.append(lastAnswer)
        print(lastAnswer)
