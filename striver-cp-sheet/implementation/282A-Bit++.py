n = int(input())
x = 0
while n:
    s = input()
    if s == "++X" or s == "X++":
        x += 1
    else:
        x -= 1
    n -= 1
print(x)
