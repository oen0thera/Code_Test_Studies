#세 자연수 a, b, c 가 피타고라스 정리 a2 + b2 = c2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
#예를 들면 32 + 42 = 9 + 16 = 25 = 52이므로 3, 4, 5는 피타고라스 수입니다.
#a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?

def Solution():
    List=[i for i in range(1,1000)]
    for a in List:
        for b in List:
            if a<b:
                c=(a**2)+(b**2)

                if c**(0.5)-int(c**(0.5))!=0:
                    pass
                elif c**(0.5)-int(c**(0.5))==0:
                    if a+b+(c**(0.5))==1000:
                        print(a*b*(c**0.5))
                        print(a,b,(c**0.5))

Solution()
