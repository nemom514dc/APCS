#子集合的和
n, P = map(int, input().split())
A = list(map(int, input().split()))
dp = [[-1 for _ in range(P+1)] for _ in range(n+1)]
def knapsack(n, P, A):
    if dp[n][P] != -1:
        return dp[n][P]
    if n == 0 or P == 0:
        return 0
    if A[n-1] > P:
        return knapsack(n-1, P, A)
    dp[n][P] = max(knapsack(n-1, P, A), knapsack(n-1, P-A[n-1], A) + A[n-1])
    return dp[n][P]

print(knapsack(n, P, A))