#피보나치(Fibonacci) 수열의 각 항은 바로 앞의 항 두 개를 더한 것입니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#4백만 이하의 짝수 값을 갖는 모든 피보나치 항을 더하면 얼마가 됩니까?

def Solution():
    a=0
    b=1
    c=1
    L=[1,2]
    result=0
    while a<=4000000:
        if c>b:
            a=a+b
            b=a
            L.append(a)
        if b>c:
            a=a+c
            c=a
            L.append(a)
        else:
            a=b+c
            b=a
    for i in L:
        if i%2==0:
            result+=i
    print(a)
    print(L)
    print(result)

Solution()

#Other Solution
'''
def Fibonacci(n):
    sum=0
    new_num = 0
    num1 = 1
    num2 = 2
    while new_num<n:
        new_num=num1+num2
        num1=num2
        num2=new_num
        if new_num % 2 ==0:
            sum += new_num
    return sum+2


print(Fibonacci(4000000))
'''
