str1 = input()
str2 = input()
str1 = int(str1, base=36)
str2 = int(str2, base=36)

if(str1 > str2):
    print(1)
elif(str1 == str2):
    print(0)
else:
    print(-1)

# print(str1)
# print(str2)
