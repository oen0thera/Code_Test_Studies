#수 1부터 시작해서 우측으로부터 시계방향으로 감아 5×5 행렬을 만들면 아래와 같이 됩니다.

#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13

#여기서 대각선 상의 수를 모두 더한 값은 101 입니다.

#같은 방식으로 1001×1001 행렬을 만들었을 때, 대각선 상의 수를 더하면 얼마가 됩니까?

import numpy as np

map=np.zeros((9,9))


print(map)
def Solution(map):
  count=1
  record=1
  Recorder=1
  process=0
  print((map.shape[0]+1)//2)
  while map[0][map.shape[1]-1]==0:
    if map[(map.shape[0]-1)//2][(map.shape[1]-1)//2]==0:
      map[(map.shape[0]-1)//2][(map.shape[1]-1)//2]=1
      middle=map[(map.shape[0]-1)//2][(map.shape[1]-1)//2]
    if map[(map.shape[0]-1)//2][(map.shape[1]-1)//2]!=0:
        if process==0:
          a=(map.shape[0]-1)//2 # (a,b) = (2,2)
          b=(map.shape[1]-1)//2
          if map[a-count][b+count]==0:
            record+=count
            map[a][b+count]=record
            record+=count
            map[a+count][b+count]=record
            Recorder+=record
            record+=count
            map[a+count][b]=record
            record+=count
            map[a+count][b-count]=record
            Recorder+=record
            record+=count
            map[a][b-count]=record
            record+=count
            map[a-count][b-count]=record
            Recorder+=record
            record+=count
            map[a-count][b]=record
            record+=count
            map[a-count][b+count]=record
            Recorder+=record
          if map[a-count][b+count]!=0:
            process+=1
            count+=1
            process-=1

    print(map)
    print(Recorder)

Solution(map)
