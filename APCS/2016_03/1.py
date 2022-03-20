#030501_成績指標
if __name__ == '__main__':
    n = input()
    arr = list(map(int, input().split()))
    
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
 
    mini = 101
    maxi = -1
    
    for i in range(len(arr)):
        if arr[i] >= 60:
            if arr[i] < mini:
                mini = arr[i]
        else:
            if arr[i] > maxi:
                maxi = arr[i]
    
    print(' '.join(list(map(str, arr))))
    if maxi == -1:
        print("best case")
    else:
        print(maxi)
    if mini == 101:
        print("worst case")
    else:
        print(mini)