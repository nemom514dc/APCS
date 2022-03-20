#030401_秘密差
#7:20
x = input()
a = 0
b = 0
for i in range(len(x)):
    if int(i) % 2 == 0:
        b += int(x[i])
    else:
        a += int(x[i])
print(abs(a - b))