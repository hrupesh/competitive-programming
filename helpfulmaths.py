s = input()
# s = int(s, base=36)
sorted_s = []
for i in range(len(s)):
    if(i % 2 == 0):
        sorted_s.append(int(s[i]))
        print(s[i])

sorted_s = sorted(sorted_s)
print(sorted_s)
