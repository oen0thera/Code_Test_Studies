
Count = 0
sum=0
for b in range(0,201,200):
    for c in range(0,201-b,100):
        for d in range(0,201-c-b,50):
            for e in range(0,201-d-c-b,20):
                for f in range(0,201-e-d-c-b,10):
                    for g in range(0,201-f-e-d-c-b,5):
                        for h in range(0,201-g-f-e-d-c-b,2):
                            for i in range(0,201-h-g-f-e-d-c-b,1):
                                Final=[b,c,d,e,f,g,h,i]
                                for a in Final:
                                    sum=sum+a
                                if sum==200:
                                    print(b,c,d,e,f,g,h,i)
                                    Count+=1
                                    sum=0
                                if sum!=200:
                                    sum=0
print(Count)

#another Solution
#동적 계획법이라는데... 모르겠다...
def get_number_ways(num):
    UNITS = [1, 2, 5, 10, 20, 50, 100, 200]
    U = len(UNITS)
    ans = 0
    num *= 100 # 1 pound = 100 pence
               # '달과 6펜스'가 생각남. ㅇㅈ?

    cache = [[0] * (num + 1) for _ in range(U+1)]
    for u in range(U+1):
        cache[u][0] = 1

    UNITS = [0] + UNITS

    for u in range(1, U+1)1:
        for n in range(num+1):
            if UNITS[u] > n:
                break

            cache[u][n] = cache[u-1][n] + (cache[u][n-UNITS[u]] if n - UNITS[u] >= 0 else 0)

    return cache


if __name__ == '__main__':
    print(get_number_ways(2)))

#another Solution2
def f(x):
	coins=[1,2,5,10,20,50,100,200]
	dp=[0 for i in range(x+1)]
	dp[0]=1
	for coin in coins:
		for cost in range(1,x+1):
			if cost-coin>=0:
				dp[cost]+=dp[cost-coin]
				print(dp)
				print(cost-coin)
	return dp[-1]

print(f(200))
#식이 너무 아름답다 ㄹㅇ...
