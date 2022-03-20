#102804_物品堆疊

import functools

while True:
    try:
        n = int(input())
        W = list(map(int, input().split()))
        F = list(map(int, input().split()))

        obj = [[int(w), int(f)] for w, f in zip(W, F)]

        obj.sort(key=functools.cmp_to_key(lambda a, b: a[0] * b[1] - b[0] * a[1]))

        energy = 0
        accumulation = 0

        for i in range(n-1):
            accumulation += obj[i][0]
            energy += accumulation * obj[i+1][1]
        print(energy)

    except:
        break
