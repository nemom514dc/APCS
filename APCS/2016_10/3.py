#102903_定時K彈
'''
a = list(range(1, n + 1))
for i in range(k):
    p = m % n - 1
    result = p + 1
    a.extend(a)
    a = [a[x] for x in range(result, p + n)]
    n = len(a)
print(a[result % n])
'''
n, m, k = map(int, input().split())
answer = 0
for i in range(n - k + 1, n + 1):
    answer = (answer + m) % i
print(answer + 1)