#수 1406357289은 0 ~ 9 팬디지털인데, 부분열에 관련된 재미있는 성질을 가지고 있습니다.

#d1을 첫째 자릿수, d2를 둘째 자릿수...라고 했을 때, 다음과 같은 사실을 발견할 수 있습니다.

#d2 d3 d4 = 406 → 2로 나누어 떨어짐
#d3 d4 d5 = 063 → 3으로 나누어 떨어짐
#d4 d5 d6 = 635 → 5로 나누어 떨어짐
#d5 d6 d7 = 357 → 7로 나누어 떨어짐
#d6 d7 d8 = 572 → 11로 나누어 떨어짐
#d7 d8 d9 = 728 → 13으로 나누어 떨어짐
#d8 d9 d10 = 289 → 17로 나누어 떨어짐
#위와 같은 성질을 갖는 0 ~ 9 팬디지털을 모두 찾아서 그 합을 구하면 얼마입니까?


from itertools import permutations
Numbers=['0','1','2','3','4','5','6','7','8','9']
Result=[]
pandigit=[list(i) for i in permutations(Numbers) if i[0]!='0']
for i in pandigit:
  if int(''.join(i[1:4]))%2==0:
    if int(''.join(i[2:5]))%3==0:
      if int(''.join(i[3:6]))%5==0:
        if int(''.join(i[4:7]))%7==0:
          if int(''.join(i[5:8]))%11==0:
            if int(''.join(i[6:9]))%13==0:
              if int(''.join(i[7:10]))%17==0:
                  print(i)
                  Result.append(int(''.join(i)))

print(Result)
print(sum(Result))
