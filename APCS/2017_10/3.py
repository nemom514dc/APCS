#102803_樹狀圖分析

while True:
    try:
        n = int(input())
        parent = [-1 for _ in range(n+1)]
        height = [-1 for _ in range(n+1)]
        height[0] = 0
        child_count = [0 for _ in range(n+1)]

        for i in range(1, n+1):
            temp = [x for x in list(map(int, input().split()))]
            child_count[i] = temp.pop(0)
            for child in temp:
                parent[child] = i

        leaf = []
        for i in range(1, n+1):
            if parent[i] == -1:
                root = i
            if child_count[i] == 0:
                leaf.append(i)
                height[i] = 0

        while leaf:
            node = leaf.pop(0)
            height[parent[node]] = max(height[parent[node]], height[node] + 1)
            child_count[parent[node]] -= 1
            if child_count[parent[node]] == 0 and parent[parent[node]] != -1:
                leaf.append(parent[node])
        
        print(root)
        print(sum(height))

    except:
        break
