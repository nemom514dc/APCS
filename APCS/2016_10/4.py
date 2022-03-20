#102904_棒球遊戲
n = []
a = []
p = []
s = 0
d = 0

for i in range(9):
    n = list(map(str, input().split()))
    a.append(n[1:])
b = int(input())
"""
a = [["1B", "1B"], ["1B", "2B"], ["SO", "HR"], ["FO", "FO"], ["1B", "1B"], ["GO", "GO"], ["1B"],["SO"], ["3B"]]
b = 6
"""

i = 0
j = 0
while True:
    if i == 9:
        i = 0
        j += 1
    if a[i][j] == "1B":
        p.insert(0, 1)
        for x in range(1, len(p)):
            if p[x] + 1 >= 4:
                s += 1
                p[x] = 0
            else:
                p[x] += 1

    elif a[i][j] == "2B":
        p.insert(0, 2)
        for x in range(1, len(p)):
            if p[x] + 2 >= 4:
                s += 1
                p[x] = 0
            else:
                p[x] += 2

    elif a[i][j] == "3B":
        p.insert(0, 3)
        for x in range(1, len(p)):
            if p[x] + 3 >= 4:
                s += 1
                p[x] = 0
            else:
                p[x] += 3

    elif a[i][j] == "HR":
        s += len(p) + 1
        p = []

    elif a[i][j] == "SO" or a[i][j] == "FO" or a[i][j] == "GO":
        d += 1
        if d >= b:
            break
        elif d % 3 == 0:
            p = []
    while 0 in p:
        p.remove(0)
    i += 1
print(s)