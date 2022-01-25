#1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317 입니다.

#1^1 + 2^2 + 3^3 + ... + 1000^1000 의 마지막 10자리 수는 무엇입니까?

#내가 한 풀이
#List=[i**i for i in range(1,1001)]
#Result=[i for i in str(sum(List))]
#print(sum(List))
#print(int(''.join(Result[-10:])))

#더 줄이기
List=[i**i for i in range(1,1001)]
print(str(sum(List))[-10:])
