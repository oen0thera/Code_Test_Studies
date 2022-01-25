'''
아래와 같이 마방진과 유사한 성질을 가진 도형이 있습니다. 1부터 6까지의 수가 한 번씩만 사용되었고, 선을 따라 합을 구하면 항상 9가 됩니다.


바깥으로 뻗친 가지 중에서 가장 수가 낮은 것부터 시작해서 직선들을 시계방향으로 돌아가며 나열하면, 도형의 모양을 수로 나타낼 수 있습니다. 위 그림의 예를 들면 4,3,2; 6,2,1; 5,1,3 과 같이 됩니다.

위 도형으로는 네 가지 다른 합계를 가지도록 배열할 수 있는데, 다음과 같은 여덟 개의 풀이가 존재합니다.

합계	풀이
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
하나의 풀이에 대해서 각 수를 모두 이어붙이면 9자리의 수를 만들 수 있고, 그 중에서 가장 큰 것은 432621513이 됩니다.

이제 아래와 같은 도형에다 마방진의 성질을 가지도록 1부터 10까지의 수를 채우고, 같은 방식으로 풀이 수를 이어붙이면 16자리 또는 17자리의 수가 만들어집니다. 이 때, 16자리 수 중에서 가장 큰 것은 무엇입니까?
'''
def Solution(number:int, first:int, second:int, third:int, innerone:int, innertwo:int, innerthree:int,recorder:list,final:list):
  if first==0:
    for i in range(1,7):
      if second==0:
        for j in range(1,7):
          if third==0:
            for k in range(1,7):
              if i+j+k==number and first==0 and i!=j and j!=k and i!=k:
                first=i
                innertwo=j
                innerthree=k
                recorder=[]
                recorder.append(i)
                recorder.append(j)
                recorder.append(k)
                result=Solution(number,first,second,third,innerone,innertwo,innerthree,recorder,final)
                if result[2]==0:
                  first=0
                  innertwo=0
                  innerthree=0
                  recorder=[]
  else: #Solution(9,4,0,0,0,2,3) #5,3,1
    for j in range(1,7):
      if second==0 and third==0:
        for k in range(1,7):
          if j+innerthree+k==number and j not in recorder and k not in recorder and j!=k and j!=innerthree and k!=innerthree:
            second=j
            innerone=k
            recorder.append(j)
            recorder.append(k)
            Solution(number,first,second,third,innerone,innertwo,innerthree,recorder,final)
            if third==0:
              recorder.remove(second)
              recorder.remove(innerone)
              second=0
              innerone=0

      if second!=0 and third==0: #Solution(9,4,5,0,1,2,3)
        for l in range(1,7):
          if l+innerone+innertwo==number and l not in recorder and l!=innerone and l!=innertwo:
            third=l
            confirmed=0
            confirmer=[number, first,innertwo, innerthree, second,innerthree,innerone, third, innerone,innertwo]
            for i in final:
              if i[1:4]==confirmer[4:7]:
                confirmed+=1
              if i[1:4]==confirmer[7:10]:
                confirmed+=1

            if confirmed==0:
              print(number, first,innertwo, innerthree, second,innerthree,innerone, third, innerone,innertwo)
              final.append([number,first,innertwo,innerthree,second,innerthree,innerone,third,innerone,innertwo])

  return [number, first, second, third, innerone, innertwo, innerthree]

def Solution2(number:int, first:int, second:int, third:int, four:int, five:int, innerone:int, innertwo:int, innerthree:int, innerfour:int, innerfive:int,recorder:list,final:list):
  if first==0:
    for i in range(1,11):
      if second==0:
        for j in range(1,11):
          if third==0:
            for k in range(1,11):
              if i+j+k==number and first==0 and i!=j and j!=k and i!=k:
                first=i
                innertwo=j
                innerthree=k
                recorder=[]
                recorder.append(i)
                recorder.append(j)
                recorder.append(k)
                result=Solution2(number,first,second,third,four,five,innerone,innertwo,innerthree,innerfour,innerfive,recorder,final)
                if result[2]==0:
                  first=0
                  innertwo=0
                  innerthree=0
                  recorder=[]

  else: #Solution(9,4,0,0,0,2,3) #5,3,1
    for j in range(1,11):
      if second==0 and third==0 and four==0 and five==0:
        for k in range(1,11):
          if j+innerthree+k==number and j not in recorder and k not in recorder and j!=k and j!=innerthree and k!=innerthree:
            second=j
            innerfour=k
            recorder.append(j)
            recorder.append(k)
            Solution2(number,first,second,third,four,five,innerone,innertwo,innerthree,innerfour,innerfive,recorder,final)
            if third==0:
              recorder.remove(second)
              recorder.remove(innerfour)
              second=0
              innerfour=0
      else:
          for k in range(1,11):
            if second!=0 and third==0 and four==0 and five==0:
              for l in range(1,11):
                if k+innerfour+l==number and k not in recorder and l not in recorder and k!=l and k!=innerfour and l!=innerfour:
                  third=k
                  innerfive=l
                  recorder.append(k)
                  recorder.append(l)
                  Solution2(number,first,second,third,four,five,innerone,innertwo,innerthree,innerfour,innerfive,recorder,final)
                  if four==0:
                    recorder.remove(third)
                    recorder.remove(innerfive)
                    third=0
                    innerfive=0
            else:
              if third!=0:
                for j in range(1,11):
                  if four==0 and five==0:
                    for k in range(1,11):
                      if j+innerfive+k==number and j not in recorder and k not in recorder and j!=k and j!=innerfive and k!=innerfive:
                        four=j
                        innerone=k
                        recorder.append(j)
                        recorder.append(k)
                        Solution2(number,first,second,third,four,five,innerone,innertwo,innerthree,innerfour,innerfive,recorder,final)
                        if five==0:
                          recorder.remove(four)
                          recorder.remove(innerone)
                          four=0
                          innerone=0

                  if four!=0 and five==0: #Solution(9,4,5,0,1,2,3)
                    for l in range(1,11):
                      if l+innerone+innertwo==number and l not in recorder and l!=innerone and l!=innertwo:
                        five=l
                        confirmed=0
                        confirmer=[number, first,innertwo, innerthree, second,innerthree,innerfour,third,innerfour,innerfive,four,innerfive,innerone, five, innerone,innertwo]
                        for i in final:
                          if i[1:4]==confirmer[1:4]:
                            confirmed+=1
                          if i[1:4]==confirmer[4:7]:
                            confirmed+=1
                          if i[1:4]==confirmer[7:10]:
                            confirmed+=1
                          if i[1:4]==confirmer[10:13]:
                            confirmed+=1
                          if i[1:4]==confirmer[13:16]:
                            confirmed+=1

                        if confirmed==0:
                          print(number, first,innertwo, innerthree, second,innerthree,innerfour,third,innerfour,innerfive,four,innerfive,innerone, five, innerone,innertwo)
                          print(len(final))
                          final.append([number, first,innertwo, innerthree, second,innerthree,innerfour,third,innerfour,innerfive,four,innerfive,innerone, five, innerone,innertwo])


  return [number, first, second, third,four,five, innerone, innertwo, innerthree,innerfour,innerfive]
recorder=[]
final=[]
for i in range(14,20):
  print(i)
  Solution2(i,0,0,0,0,0,0,0,0,0,0,recorder,final)
print(recorder)
print(final)
