#030402_小群體
#50
n = int(input())
a = list(map(int, input().split()))
"""
n = 10
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [4, 7, 2, 9, 6, 0, 8, 1, 5, 3]
"""

d = []
result = 0
for i in range(n):
    if i not in d:
        result += 1
        p = i
        f = a[i]
        d.append(i)
        while True:
            if f == i:
                break
            else:
                d.append(f)
                p = f
                f = a[p]
print(result)