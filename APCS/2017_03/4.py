#030404_基地台

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

dis = a[-1] - a[0]
l = 0
r = dis // k + 1

def coverable(d):
    coverage = a[0] + d
    count = 1
    for i in range(1, n):
        while (a[i] > coverage):
            coverage = a[i] + d
            count += 1
    return count <= k

mini = r - l
while (l < r):
    mid = (l + r) // 2
    if (coverable(mid)):
        mini = mid
        r = mid
    else:
        l = mid + 1

print(mini)