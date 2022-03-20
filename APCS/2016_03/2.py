#030502_矩陣轉換
def spin(arr, r, c):
    result = [[arr[i][j] for i in range(r)] for j in range(c - 1, -1, -1)]
    return result

def turn(arr, r, c):
    for i in range(c):
        for j in range(r // 2):
            arr[j][i], arr[r - j - 1][i] = arr[r - j - 1][i], arr[j][i]
    return arr

R, C, M = map(int, input().split())
a = [[]*C]*R
for i in range(R):
    a[i] = list(map(int, input().split()))
m = list(map(int, input().split()))

for i in range(len(m) - 1, -1, -1):
    if m[i] == 0:
        a = spin(a, len(a), len(a[0]))
    else:
        a = turn(a, len(a), len(a[0]))

print(len(a), len(a[0]))
for i in range(len(a)):
    print(' '.join(list(map(str, a[i]))))