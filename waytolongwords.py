n = input()
n = int(n)
words = []


def converttoabbr(a):
    print(a[0])
    b = a[::-1]
    print(b[0])
    new = a[0] + str(len(a) - 2) + b[0]
    return new


for i in range(n):
    t = input()
    words.append(t)
    # print(words[i])

new_words = []

for i in words:
    if(len(i) > 10):
        i = converttoabbr(i)
        new_words.append(i)
    else:
        new_words.append(i)
    # print("\n")
print(new_words)


# c = input()
# convertoabbr(c)
