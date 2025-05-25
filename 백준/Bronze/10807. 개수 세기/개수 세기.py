arr_length = int(input())
arr = list(map(int,input().split()))
num = int(input())
count = 0
for i in range(arr_length):
    if arr[i]==num:
        count+=1

print(count)