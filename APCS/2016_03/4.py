#030504_血緣關係
while True:
    try:
        n = int(input())
        ans = 0
        child = [list() for _ in range(n)]
        child_count = [0 for _ in range(n)]
        other = [False for _ in range(n)]
        for i in range(n - 1):
            a, b = map(int, input().split())
            child[a].append(b)
            child_count[a] += 1
            other[b] = True
        anscestor = 0
        for i in range(n):
            if other[i] == False:
                anscestor = i
                break
        depth_record = [-1 for _ in range(n)]
        def depth(node):
            global ans
            global depth_record
            if depth_record[node] != -1:
                return depth_record[node]
            else:
                if child_count[node] == 0:
                    depth_record[node] = 0
                    return depth_record[node]
                elif child_count[node] == 1:
                    depth_record[node] = depth(child[node][0]) + 1
                    return depth_record[node]
                else:
                    m1 = 0
                    m2 = 0
                    for i in range(child_count[node]):
                        t = depth(child[node][i])
                        if t > m1:
                            m2 = m1
                            m1 = t
                        elif t > m2:
                            m2 = t
                    ans = max(m1 + m2 + 2, ans)
                    depth_record[node] = m1 + 1
                    return depth_record[node]
        ancestor_depth = depth(anscestor)
        ans = max(ancestor_depth, ans)
        print(ans)
    except:
        break
