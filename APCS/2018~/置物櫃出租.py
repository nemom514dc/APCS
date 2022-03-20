#置物櫃出租
n, M, S = map(int, input().split())
f = list(map(int, input().split()))

dp = {}
def knapsack(n, P, A):
    if (n, P) in dp:
        return dp[(n, P)]
    if n == 0 or P == 0:
        return 0
    if A[n-1] > P:
        return knapsack(n-1, P, A)
    dp[(n, P)] = max(knapsack(n-1, P, A), knapsack(n-1, P-A[n-1], A) + A[n-1])
    return dp[(n, P)]

total_sum = 0
for i in f:
    total_sum += i
print(total_sum - knapsack(n, M - S, f))