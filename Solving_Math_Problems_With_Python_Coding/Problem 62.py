'''세제곱수인 41063625 (=3453) 로 순열을 만들어보면, 그 중에서 56623104 (=3843)와 66430125 (=4053)가 또 세제곱수입니다.
실제 41063625은, 자릿수로 만든 순열 중에서 3개가 세제곱수인 가장 작은 수입니다.

그러면 자릿수로 만든 순열 중에서 5개가 세제곱수인 가장 작은 수는 무엇입니까?

'''
for n in range(300,100000):
  operand=[]
  target=list(sorted([i for i in str(n**3)]))
  operand.append(n)
  for k in range(0,100000):
    if k!=n and list(sorted([i for i in str(k**3)]))==target:
      operand.append(k)
  if len(operand)==5:
    print(operand)
    break
