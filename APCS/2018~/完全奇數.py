#完全奇數
try:
    result = []
    while True:    
        N = input()
        m = [1 for _ in range(len(N))]
        n = [9 for _ in range(len(N))]
        for i in range(len(N)):
            t = int(N[i])
            if t % 2 == 1:
                m[i] = t
                n[i] = t
            else:
                if t != 0:
                    m[i] = t + 1
                    n[i] = t - 1
                else:
                    m[i] = t + 1
                    index = i - 1
                    while index > 0 and int(N[index]) == 1:
                        n[index] = 9
                        index -= 1
                    n[index] -= 2
                    if n[index] < 0:
                        n[index] = 0
                break
        _M = int(''.join([str(i) for i in m]))
        _N = int(''.join([str(i) for i in n]))
        result.append(min(_M - int(N), int(N) - _N))
except EOFError:
    print('\n'.join(list(map(str, result))))