s = input()
# s = int(s, base=36)
sorted_s = []
for i in range(len(s)):
    if(i % 2 == 0):
        sorted_s.append(int(s[i]))
        # print(s[i])

sorted_s = sorted(sorted_s)

new_s = ""
for i in range(len(sorted_s)):
    if(i == len(sorted_s)-1):
        new_s = new_s + str(sorted_s[i])
    else:
        new_s = new_s + str(sorted_s[i]) + "+"

print(new_s)
