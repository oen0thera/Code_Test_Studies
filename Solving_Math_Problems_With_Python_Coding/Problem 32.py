#1부터 n까지의 각 숫자를 한 번씩만 써서 만들 수 있는 수를 팬디지털(pandigital)이라고 합니다.
#예를 들면 15234는 1부터 5의 숫자가 한 번씩만 쓰였으므로 1 ~ 5 팬디지털입니다.

#7254라는 수는 그런 면에서 특이한데, 39 × 186 = 7254 라는 곱셈식을 만들 때 이것이 1 ~ 9 팬디지털이 되기 때문입니다.

#이런 식으로 a × b = c 가 1 ~ 9 팬디지털이 되는 모든 c의 합은 얼마입니까?

#(참고: 어떤 c는 두 개 이상의 (a, b)쌍에 대응될 수도 있는데, 이런 경우는 하나로 칩니다)


Result=[]
def Solution():
    a=1
    b=1
    confirm=['1','2','3','4','5','6','7','8','9']
    Why=[]
    next_set=0
    Total_break=False
    while a<9999:
      if next_set==0:
        next_set+=1
        ListA=[i for i in str(a)]
        ListB=[i for i in str(b)]

        for i in ListA:
          if Total_break==True:
                break
          if i in ListB:
            Total_break=True
            b+=1
            Total_break=False
            next_set=0
            print(a,b)
          if i not in ListB:
            if i==ListA[-1]:
              for n in ListB:
                if n in ListA:
                  Total_break=True
                  b+=1
                  Total_break=False
                  next_set=0
                  print(a,b)
                else:
                  if n==ListB[-1]:
                    ListC=[i for i in str(a*b)]
                    print(a,b)
                    for j in ListC:
                      if j==ListC[-1]:
                        New=ListA+ListB+ListC
                        New.sort()
                        if New==confirm and a*b not in Result:
                          next_set+=1
                          print(ListC)
                          Why.append('{}x{}={}'.format(a,b,a*b))
                          Why.append(New)
                          Result.append(a*b)
                          print(a,b)
                          Total_break=True
                          b+=1
                          Total_break=False
                          next_set=0
                          New=[]
                          break
                        else:
                          Total_break=True
                          b+=1
                          Total_break=False
                          print(a,b)
                          next_set=0
                          New=[]
      if len(ListA)==1 and b>9999:
        b=1
        a+=1
        print(a,b)
        next_set=0
      if len(ListA)==2 and b>999:
        b=1
        a+=1
        print(a,b)
        next_set=0
      if len(ListA)==3 and b>99:
        b=1
        a+=1
        print(a,b)
        next_set=0
      if len(ListA)==4 and b>9:
        b=1
        a+=1
        print(a,b)
        next_set=0
    print(Result)
    print(Why)
    sum=0
    for m in Result:
      sum=sum+m
    print('Result is {}'.format(sum))
Solution()
