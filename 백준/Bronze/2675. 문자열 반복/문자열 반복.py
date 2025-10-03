for _ in range(int(input())):
  R, S = input().split()
  T = ""
  for s in S:
    T+=s*int(R)
  print(T)