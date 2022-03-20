#反序數量
n = int(input())
A = list(map(int, input().split()))

def InvPCount(A):
    mini = A[0]
    maxi = A[0]
    for i in A:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
    if mini == maxi:
        return 0
    mid = (maxi + mini) / 2
    a = []
    b = []
    result = 0
    for i in range(len(A)):
        if A[i] <= mid:
            a.append(A[i])
            result += len(b)
        elif A[i] > mid:
            b.append(A[i])
    return InvPCount(a) + InvPCount(b) + result

print(InvPCount(A))