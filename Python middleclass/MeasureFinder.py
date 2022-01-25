def is_prime(n:int) -> bool:
  if n<2:
    return False
  if n in (2,3):
    return True
  if n%2 == 0 or n%3 == 0:
    return False
  if n<9:
    return True
  k,l = 5, n**0.5
  while k<=l:
    if n%k == 0 or n%(k+2) == 0:
      return False
    k+=6
  return True

def Measure(number):
  result=[]

  if number%2==0 and 2 not in result and number//2 not in result:
    result.append(2)
    result.append(int(number/2))
  if number%3==0 and 3 not in result and number//3 not in result:
    result.append(3)
    result.append(int(number/3))
  if number%5==0 and 5 not in result and number//5 not in result:
    result.append(5)
    result.append(int(number/5))
  if number%7==0 and 7 not in result and number//7 not in result:
    result.append(7)
    result.append(int(number/7))
  if number//number**0.5==number**0.5:
    result.append(int(number**0.5))
  for i in result:
    if i>=10:
      ender = Measure(i)
      for i in ender:
        if i not in result:
          result.append(i)
    if i//i**0.5==i**0.5 and i!=1:
      ender = Measure(i)
      for i in ender:
        if i not in result:
          result.append(i)
  if 1 not in result and number not in result and is_prime(number)==True:
    result.append(1)
    result.append(number)
  if 1 not in result and number not in result and is_prime(number)==False:
    result.append(1)
    for i in range(1,number,2):
      if is_prime(i):
        if number%i==0 and i not in result:
          result.append(i)
    result.append(number)
  return sorted(result)

print(Measure(573))
