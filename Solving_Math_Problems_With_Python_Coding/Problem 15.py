#2^15 = 32768 의 각 자릿수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.
#2^1000의 각 자릿수를 모두 더하면 얼마입니까?


Number=2**1000
List=[i for i in str(Number)]
result=0
for i in List:
    result=result+int(i)
print(List)
print(result)
