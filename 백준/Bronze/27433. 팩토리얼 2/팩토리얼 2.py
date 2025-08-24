num = int(input())

def fact(num):
  if num==0: return 1
  if num==1: return 1
  return fact(num-1)*num

print(fact(num))