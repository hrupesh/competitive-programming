s = input()
# s = int(s, base=36)
sorted = []
for i in range(len(s)):
    if(i % 2 == 0):
        sorted.append(s[i])
        print(s[i])
# print(len(s))
