n = input()
n = int(n)
words = []

for i in range(n):
    t = input()
    words.append(t)
    # print(words[i])

for i in words:
    if(len(i) > 10):
        print(i)
    # print("\n")
# print(words)
