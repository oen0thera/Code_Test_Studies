#양의 정수 n에 대하여, 다음과 같은 계산 과정을 반복하기로 합니다.
#n → n / 2 (n이 짝수일 때)
#n → 3 n + 1 (n이 홀수일 때)
#13에 대하여 위의 규칙을 적용해보면 아래처럼 10번의 과정을 통해 1이 됩니다.
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#아직 증명은 되지 않았지만, 이런 과정을 거치면 어떤 수로 시작해도 마지막에는 1로 끝나리라 생각됩니다.
#(역주: 이것은 콜라츠 추측 Collatz Conjecture이라고 하며, 이런 수들을 우박수 hailstone sequence라 부르기도 합니다)

#그러면, 백만(1,000,000) 이하의 수로 시작했을 때 1까지 도달하는데 가장 긴 과정을 거치는 수는 얼마입니까?

#참고: 계산 과정에는 백만을 넘어가는 수가 나와도 괜찮습니다.

def Solution(n):
    num=n
    count=0
    record=0
    recorded_num=0
    switch=0
    while n>1:
        if switch==0:
            while num!=1:
                if num%2==0 and num!=1:
                    num=num//2
                    count+=1

                elif num%2==1 and num!=1:
                    num=(num*3)+1
                    count+=1


                if count>=record:
                    print('Recorded Process:{}'.format(record))
                    record=count
                    recorded_num=n

            if num==1:
                n-=1
                print('New Number!!! : {}'.format(n))
                num=n
                count=0


    print('The highest process number is {}'.format(recorded_num))
    print('Counts of Process is {}'.format(record))

#Solution(1000000)


#Other Solution
#앞선 숫자의 결과를 딕셔너리에 저장, 이후 다른 숫자 계산과정에 계산해놓은 숫자가 나오면
#재활용하는 방식
# !!! == 훨씬 더 시간이 절약된다
dictionary=dict()
for n in range(1,1000001):
    num=n
    cnt_now=0
    while True:
        if n==1:
            cnt_now+=1
            break
        if n in dictionary:
            cnt_now=cnt_now+dictionary[n]
            break
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        cnt_now+=1
    dictionary[num]=cnt_now

print(max(dictionary,key=dictionary.get))
