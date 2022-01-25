#1487, 4817, 8147은 3330씩 늘어나는 등차수열입니다. 이 수열에는 특이한 점이 두 가지 있습니다.

#세 수는 모두 소수입니다.
#세 수는 각각 다른 수의 자릿수를 바꿔서 만들 수 있는 순열(permutation)입니다.
#1자리, 2자리, 3자리의 소수 중에서는 위와 같은 성질을 갖는 수열이 존재하지 않습니다. 하지만 4자리라면 위엣것 말고도 또 다른 수열이 존재합니다.

#그 수열의 세 항을 이었을 때 만들어지는 12자리 수는 무엇입니까?
from itertools import permutations
Notprime=[i for i in range(1,10000) for j in range(1,int(i**(0.5)+1)) if i%j==0 and j!=i and j!=1]
New=set(Notprime)
PrimeNum=[i for i in range(1,10000) if i not in New]

List=[ str(i) for i in range(1000,10000)]
Result=set()
for i in List:
  Tide=[j for j in i]
  Goat=[int(''.join(list(n))) for n in permutations(Tide) if list(n)[0]!='0']
  New=list(set(Goat))
  New.sort()
  print(New)
  for j in New:
    for k in New:
      for l in New:
        if j>k>l and j-k==k-l and j in PrimeNum and k in PrimeNum and l in PrimeNum:
          Result.add('{},{},{}'.format(str(l),str(k),str(j)))
print(Result)
for p in list(Result):
  if '1487' not in p:
    target=list(p)
    for i in target:
      if ',' in target:
        target.remove(',')
    print(''.join(target))
