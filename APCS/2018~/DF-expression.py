#DF-expression
s = input()
n = int(input())
global idx
idx = -1

def count_ones(l):
    global idx
    idx += 1
    if s[idx] == '0':
        return 0
    if s[idx] == '1':
        return l * l
    return count_ones(l//2) + count_ones(l//2) + count_ones(l//2) + count_ones(l//2)

print(count_ones(n))