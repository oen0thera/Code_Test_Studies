N, M = map(int, input().split())
arr = list(map(int,input().split()))
prefix_sum = [0]*(len(arr)+1) #0으로 초기화
result = []
for k in range(1,len(arr)+1): #1번째 인덱스에 arr의0번째값(누적합 0번째) + arr의 0번째 값
    prefix_sum[k] = prefix_sum[k-1] + arr[k-1] #k번째 인덱스에 k-1번째 값까지의 누적합 + arr의 k-1번째값
for _ in range(M):
  i,j = map(int,input().split())
  prefix = prefix_sum[j] - prefix_sum[i-1] #i~j 구간의 누적합 =  1~j까지의 누적합 - 1~i-1까지의 누적합
  result.append(prefix)
for res in result:
  print(res)