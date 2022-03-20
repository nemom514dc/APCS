#102802_交錯字串
k = int(input())
s = str(input())
result = 0

a = [0] * len(s)
for i in range(len(s)):
    if s[i].isupper():
        a[i] = 1
b = []
count = 1
for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        b.append(count)
        count = 1
    else:
        count += 1
b.append(count)

ans = []
count = 0

for i in range(len(b)):
    if b[i] == k:
        count += 1
    else:
        if ((i - count - 1) >= 0) and (b[i - count -1] > k):
            count += 1
        if (b[i] > k):
            count += 1
        ans.append(count)
        count = 0
if count > 0 and ((len(b) - count - 1) >= 0) and b[len(b) - count - 1] > k:
    count += 1
ans.append(count)

print(max(ans) * k)