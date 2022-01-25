from decimal import *
getcontext().prec = 100
count=1
confirming=0
process=0
#경우의 수: 0.33333(같은수 반복)/0.16666(소숫점 첫째자리 다른수, 그이후 반복),0.142857...(구간반복),0.125(나누어 떨어짐)

def Solution(n):
  count=1
  confirming=0
  process=0
  Result=[]
  Final_num=0
  while count<=n:
    if process==0:
      process+=1
      count+=1
      print(Decimal(1)/Decimal(count))
      number=Decimal(1)/Decimal(count)
      Data=[i for i in str(number)]
      Data.remove(Data[0])
      Data.remove(Data[0])
      while Data[0]=='0':
        Data.remove(Data[0])
      print(Data)
      if Data[0] in Data[1:]:# 소숫점 이후 0이 아닌 첫번째 숫자가 그 뒤에 반복되는경우
          k=Data[1:].index(Data[0])
          print(Data[1:].index(Data[0]))
          print(Data[0])
          print('k:{}'.format(k))
          if Data[k+1]!=Data[k+2] and k!=0:
            Rod=Data[0:k+1]
            plust=0
            for i in Rod:
              if i in Data[k+2:]:
                plust+=1
                print(plust)
            if plust==len(Rod):
              new=Data[k+2:].index(Data[0])
              Rod=Data[0:new+k+2]
              print(Rod)
              print('같은 구간 반복')
              if len(Rod)>len(Result):
                Result=Rod[:]
                Final_num=count

          if Data[k]==Data[k+1] and k==0:
            for j in Data:
              if j!=Data[0]:
                confirming+=1
                print(confirming)
                break
            if confirming==0:
              print(Data[0])  #0.33333(같은 수 반복)
              print('같은 수 반복')
            confirming=0
      if Data[0] not in Data[1:]: # 소숫점 이후 0이 아닌 첫번째 숫자가 그 뒤에 반복되지 않을 경우
          if 1/count==Decimal(1)/Decimal(count) and count%5!=0:
            print(Decimal(1)/Decimal(count)) #0.125(나누어떨어지는 경우)
            print('나누어떨어짐')
          if count%5==0:
            print(Decimal(1)/Decimal(count)) #0.125(나누어떨어지는 경우)
            print('나누어떨어짐')
          if 1/count!=Decimal(1)/Decimal(count) and count%5!=0:
            if Data[1] in Data[2:]: # 소숫점 이후 0이 아닌 두번째 숫자가 그 뒤에 반복되는경우
              m=Data[2:].index(Data[1])
              if Data[1:m-1] in Data[m:] and Data[m]!=Data[m+1] and m!=0:
                print(Data[0],Data[1:m-1]) #0.1329329329(첫번째 숫자 이후 구간반복)
                print('첫번째 숫자 이후 구간반복')
              if Data[m+1]==Data[m+2] and m==0:
                for p in Data[1:len(Data)-1]:
                  if p!=Data[1]:
                    confirming+=1
                    break
                if confirming==0:
                  print(Data[0],Data[1])#0.16666 (첫번째 숫자이후 같은 수 반복)
                  print('첫번째 숫자이후 같은 수 반복')
                confirming=0
      process=0
  print(Result)
  print(Final_num)

Solution(100)
