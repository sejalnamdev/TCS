n = int(input())
s = []
for i in range(n):
    s.append(int(input()))

if n < 2:
    print(None)

else:

    res = float('-inf')
    

    for i in range(n-1):
        s[i], s[i+1] = s[i+1], s[i]
        power = 0
        for j in range(n):
            power += s[j]*j
        res = max(res,power)
        s[i], s[i+1] = s[i+1], s[i]


print(res)
