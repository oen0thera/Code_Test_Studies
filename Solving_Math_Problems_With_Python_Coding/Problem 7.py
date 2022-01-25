#소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
#이 때 10,001번째의 소수를 구하세요.


# 포기한 문제! = > 보충하기...
def primeNum(n : int)-> [int]:
    pList = [False, False] + [True]*(n-1)
    cnt = 0
    for i in range(2, n+1) :
        if pList[i]:
            cnt += 1
            m = i + i
            while m <= n:
                pList[m] = False
                m +=i
            if cnt == 10001:
                print(i, cnt)

    return [x for (x,y) in enumerate(pList) if y]



#n = 1000000
#lst = primeNum(n)

#Solution 2
#n=3
#setOfprimeNumbers=[2]

#while len(setOfprimeNumbers)<10001:
#    for i in setOfprimeNumbers:
#        if n%i == 0:
#            break
#        if i==setOfprimeNumbers[-1]:
#            setOfprimeNumbers.append(n)
#    n+=1

#print('10001st prime number is', setOfprimeNumbers[-1])


#Solution3
list7 = []
i = 1
breaker=False

while True:
    i = i+1

    for j in range(2,(i+1)):

        if (i%j==0) & (i>j):
            break
        elif j==i:
            list7.append(i)


        if len(list7)==10001:
            breaker=True

    if breaker==True:
        print(list7[-1])
        break
