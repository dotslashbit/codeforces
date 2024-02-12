mat = []
posX, posY = -1,-1
for i in range(5):
    row = input().split(" ")
    mat.append(row)
for i in range(5):
    for j in range(5):
        if mat[i][j] == "1":
            posX = i
            posY = j
print(abs(2-posX) + abs(2-posY))

