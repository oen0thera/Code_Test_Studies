def Solution():
    List=list(filter(lambda i: i%2!=0,range(1,10000)))
    count=0
    if count<100:
        for i in range(0,len(List)-1):
            for j in List:
                if j!=List[i] and j%List[i]==0 and List[i]!=1:
                    List.remove(j)
                    print(List[-1])
                    print('len(List):{}'.format(len(List)))
                    print(i)
                    print(List[i])
                    print(j)
                else:
                    count+=1

    print(List)

Solution()
