res = []
a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
st = []

st.append(a[0])

res.append(-1)
st[0] = a[i]
for i in range(1,len(st)):
    while st and a[i]>= st.top():
        st.pop()

    if not st:
        res[i] = -1

    else:
        res[i] = st[-1]

        st.push(a[i])

print(res)




