#어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 합니다.
#예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.
#600851475143의 소인수 중에서 가장 큰 수를 구하세요.
def Shortest():
    a=1683
    b=3
    c=[]

    while a>b:
        if a%b==0:
            a=a/b
        b+=2
        print(b)

    print(b)

def OtherSolution():
    #project euler

    #oo3

    fac_list=[1]
    fac=3

    num=600851475143

    while num!=1:
        if num%fac==0:
            if fac>fac_list[-1]:
                fac_list.append(fac)
                print(fac_list)
                print(fac)
            num=num/fac
        else:
            fac+=1
            print(fac)

    print(fac_list)



OtherSolution()
