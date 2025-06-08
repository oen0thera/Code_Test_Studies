N,M = map(int,input().split())

def multi_comb(comb=[]):
  for i in range(N):
    if len(comb)<M:
      comb.append(i+1)
      multi_comb(comb)
      comb.pop();
    else:
      print(' '.join(str(i) for i in comb))
      return

multi_comb()