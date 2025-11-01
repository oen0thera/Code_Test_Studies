while True:
  F,S = map(int,input().split())
  if F==0 and S==0: break
  if F%S==0:
    print('multiple')
  elif S%F==0:
    print('factor')
  else:
    print('neither')