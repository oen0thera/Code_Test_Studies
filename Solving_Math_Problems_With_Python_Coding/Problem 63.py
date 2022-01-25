'''
다섯 자리 수인 16807은 75으로 5제곱수입니다. 또, 아홉 자리 수인 134217728은 89으로 9제곱수입니다.

n자리 수면서 n제곱수도 되는 양의 정수는 모두 몇 개나 있습니까?
'''

count=0
for i in range(1,10000):
  for j in range(1,100):
    List=[k for k in str(i**j)]
    if len(List)==j:
      print('{}^{}'.format(i,j))
      count+=1
print(count)
