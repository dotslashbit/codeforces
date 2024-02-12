s = input()
ans = ""
for i in range(len(s)):
    if int(s[i]) == 9 and i == 0:
        ans += s[i]
    elif int(s[i]) >= 5:
        ans += str(9 - int(s[i]))
    else:
        ans += s[i]
print(ans)

