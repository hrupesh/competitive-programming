n = input()
n = int(n)
statements = []
x = 0

for i in range(n):
    s = input()
    statements.append(s)

for stmt in statements:
    switch(stmt):
        case("X++" or "++X"):
            x = x + 1
        case("X--" or "--X"):
            x = x - 1


print(statements)
