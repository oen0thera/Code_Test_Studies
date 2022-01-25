#세 변의 길이가 모두 자연수 {a, b, c}인 직각삼각형의 둘레를 p 로 둘 때, p = 120 을 만족하는 직각삼각형은 아래와 같이 세 개가 있습니다.

#{20, 48, 52}, {24, 45, 51}, {30, 40, 50}
#1000 이하의 둘레 p에 대해서, 직각삼각형이 가장 많이 만들어지는 p의 값은 얼마입니까?
List=[(a+b+int((a**2+b**2)**(0.5))) for a in range(1,1000) for b in range(1,1000) if a**2+b**2==(int((a**2+b**2)**(0.5)))**2 and a<=b and a+b+int((a**2+b**2)**(0.5))<=1000]
ops=0
Result=0
for i in List:
  if List.count(i)>ops:
    ops=List.count(i)
    Result=i

print(Result)
