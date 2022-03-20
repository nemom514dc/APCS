#201802_階梯數字
N = input()
a = []
for i in range(len(N)):
    a.append(int(N[i]))
a.reverse()
maxn = len(a) - 1

global dp
dp = [[[-1 for k in range(2)] for j in range(10)] for i in range(len(a))]

def findNum(pos, now, lim):
    if dp[pos][now][lim] != -1:
        return dp[pos][now][lim]
    if pos == 0:
        dp[pos][now][lim] = 1
        return dp[pos][now][lim]
    if lim == 1:
        res = 0
        for i in range(now, a[pos-1]):
            res += findNum(pos-1, i, 0)
        if a[pos-1] >= now:
            res += findNum(pos-1, a[pos-1], 1)
    else:
        res = 0
        for i in range(now, 10):
            res += findNum(pos-1, i, 0)

    dp[pos][now][lim] = res
    return dp[pos][now][lim]

ans = 0
for i in range(a[maxn]):
    ans += findNum(maxn, i, 0)
ans += findNum(maxn, a[maxn], 1)

print(ans - 1)