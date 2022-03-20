#201802_支點切割
N, K = map(int, input().split())
a = list(map(int, input().split()))

def findValue(a, K, L, R, level, ldp, rdp):
    if R - L < 2 or level >= K:
        return 0

    if ldp is None:
        ldp = []
        delta = 0
        for i in range(L, R+1):
            if i == L:
                ldp.append(0)
            else:
                delta += a[i-1]
                ldp.append(ldp[i-1-L] + delta)
    
    if rdp is None:
        rdp = []
        delta = 0
        for i in range(R, L-1, -1):
            if i == R:
                rdp.append(0)
            else:
                delta += a[i+1]
                rdp.append(rdp[R-i-1] + delta)

    length = len(rdp)
    L_original = R - length + 1

    for i in range(L+1, R):
        if i == L + 1:
            mini = abs(rdp[length-i-1+L_original] - ldp[i-L])
            idx = i
        else:
            temp = abs(rdp[length-i-1+L_original] - ldp[i-L])
            if temp < mini:
                mini = temp
                idx = i

    return a[idx] + findValue(a, K, L, idx - 1, level + 1, ldp, None) + findValue(a, K, idx + 1, R, level + 1, None, rdp)

print(findValue(a, K, 0, N - 1, 0, None, None))
