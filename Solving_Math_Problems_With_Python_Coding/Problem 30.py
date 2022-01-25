#각 자리의 숫자를 4제곱해서 더했을 때 자기 자신이 되는 수는 놀랍게도 단 세 개밖에 없습니다.

#1634 = 14 + 64 + 34 + 44
#8208 = 84 + 24 + 04 + 84
#9474 = 94 + 44 + 74 + 44
#(1 = 14의 경우는 엄밀히 말해 합이 아니므로 제외합니다)

#위의 세 수를 모두 더하면 1634 + 8208 + 9474 = 19316 입니다.

#그렇다면, 각 자리 숫자를 5제곱해서 더했을 때 자기 자신이 되는 수들의 합은 얼마입니까?

def Solution():
    n=10
    sum=0
    process=0
    count=0
    Result=[]
    while process==0:
        if count==0:
            List=[i for i in str(n)]
            for i in List:
                sum+=int(i)**5
            sum_length=[t for t in str(sum)]
            if sum==n:
                count+=1
                Result.append(n)
                n+=1
                print(n)
                sum=0
                count-=1
            if sum!=n:
                count+=1
                n+=1
                print(n)
                sum=0
                count-=1
            if n>1000000:
                process+=1
                print(n)
    print(Result)


Solution()
