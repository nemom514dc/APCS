#102902_最大和
s = 0
a = []
maxi = []
result = []
r, c = map(int, input().split())
for i in range(r):
    a.append(list(map(int, input().split())))

for i in range(r):
    m = max(a[i])
    maxi.append(m)
    s += m
for i in maxi:
    if s % i == 0:
        result.append(i)
print(s)
if result == []:
    print(-1)
else:
    print(' '.join(list(map(str, result))))