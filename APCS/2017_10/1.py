#102801_邏輯運算子
#23:07
a, b, c = map(int, input().split())
result = [0, 0, 0]
p = [0, 0, 0]
arr = ["AND", "OR", "XOR"]
if a == b and a == 0:
    result = [0, 0, 0]
elif a == 0 or b == 0:
    result = [0, 1, 1]
else:
    result = [1, 1, 0]
for i in range(len(result)):
    if result[i] == c:
        p[i] = 1
if p == [0, 0, 0]:
    print("IMPOSSIBLE")
else:
    for i in range(len(p)):
        if p[i] == 1:
            print(arr[i])