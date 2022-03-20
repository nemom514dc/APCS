#030403_數字龍捲風
#53
a = []
n = int(input())
s = int(input())
for i in range(n):
    a.append(list(map(int, input().split())))
"""
n = 5
s = 0
a = [[3, 4, 2, 1, 4], [4, 2, 3, 8, 9], [2, 1, 9, 5, 6], [4, 2, 3, 7, 8], [1, 2, 6, 4, 3]]
"""

t = 2
d = []
r = n // 2
c = n // 2
result = [a[r][c]]
for i in range(1, n):
    if i == n - 1:
        t = 3
    for j in range(t):
        for k in range(i):
            d.append(s)
        if s == 3:
            s = 0
        else:
            s += 1
for i in d:
    if i == 0:
        c = c - 1
    elif i == 1:
        r = r - 1
    elif i == 2:
        c = c + 1
    elif i == 3:
        r = r + 1
    result.append(a[r][c])
print(''.join(list(map(str, result))))