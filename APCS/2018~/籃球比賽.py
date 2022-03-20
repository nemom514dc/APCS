#籃球比賽
a = []
for i in range(4):
    temp = list(map(int, input().split()))
    a.append(sum(temp))
print(str(a[0]) + ":" + str(a[1]))
print(str(a[2]) + ":" + str(a[3]))
if a[0] > a[1] and a[2] > a[3]:
    print("Win")
elif a[0] < a[1] and a[2] < a[3]:
    print("Lose")
else:
    print("Tie")