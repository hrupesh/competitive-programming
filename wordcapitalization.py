w = input()
new_w = ""
for i in range(len(w)):
    if(i == 0):
        new_w = new_w + w[i].upper()
    else:
        new_w = new_w + w[i]

print(new_w)
