n = input("Enter Number: ")
k = input("Enter no of times number: ")
i = 0
for i in range(k):
    if(n % 10 == 0):
        n = n/10
    else:
        # print("In else")
        n = n - 1
    # print(n)

print(n)

# n = input("Enter Number : ")
# n = n[::-1]
# print(n)
