'''
Common denominators

You will have a list of rationals in the form

{ {numer_1, denom_1} , ... {numer_n, denom_n} }
or
[ [numer_1, denom_1] , ... [numer_n, denom_n] ]
or
[ (numer_1, denom_1) , ... (numer_n, denom_n) ]
where all numbers are positive ints. You have to produce a result in the form:

(N_1, D) ... (N_n, D)
or
[ [N_1, D] ... [N_n, D] ]
or
[ (N_1', D) , ... (N_n, D) ]
or
{{N_1, D} ... {N_n, D}}
or
"(N_1, D) ... (N_n, D)"
depending on the language (See Example tests) in which D is as small as possible and

N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
Example:
convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]
Note:
Due to the fact that the first translations were written long ago - more than 6 years - these first translations have only irreducible fractions.

Newer translations have some reducible fractions. To be on the safe side it is better to do a bit more work by simplifying fractions even if they don't have to be.

Note for Bash:
input is a string, e.g "2,4,2,6,2,8" output is then "6 12 4 12 3 12"
'''
import math
import functools

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
  if number==1:
    return [1]
  if number%2==0 and 2 not in result and int(number//2) not in result:
    result.append(2)
    result.append(int(number/2))
  if number%3==0 and 3 not in result and int(number//3) not in result:
    result.append(3)
    result.append(int(number/3))
  if number%5==0 and 5 not in result and int(number//5) not in result:
    result.append(5)
    result.append(int(number/5))
  if number%7==0 and 7 not in result and int(number//7) not in result:
    result.append(7)
    result.append(int(number/7))
  if number//number**0.5==number**0.5 and int(number**(0.5)) not in result:
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
  return sorted(list(set(result)))

def abbreviation(tiny:int,Big:int):
  t=Measure(tiny)
  new_t=tiny
  new_T=Big
  for i in t:
    if i!=1 and Big%i==0:
      new_t=new_t//i
      new_T=new_T//i
      tiny,Big = abbreviation(new_t,new_T)
      break
  return tiny,Big

def Factorization(number:int, result:list):
  for i in range(1,number+1):
    if is_prime(i) and number%i==0 :
      result.append(i)
      number=number//i
      result = Factorization(number,result)
      break
  return result

def LCM(List:list):
  new_list=[]
  for i in List:
    for j in i:
      if [j,i.count(j)] not in new_list:
        new_list.append([j,i.count(j)])
  remover=[]
  for i in new_list:
    for j in new_list:
      if i[0]==j[0] and i[1]<j[1] and i not in remover:
        remover.append(i)
  for r in remover:
    new_list.remove(r)
  res=1
  for r in new_list:
    res=res*(r[0]**r[1])
  return res
def convert_fracts(lst):
  Merge=[]
  Factor=[]
  Final=[]
  for i in lst:
    converted = list(abbreviation(i[0],i[1]))
    Merge.append(converted[1])
  for i in Merge:
    result=[]
    result = Factorization(i,result)
    if result not in Factor:
      Factor.append(result)
  Least = LCM(Factor)
  for i in lst:
    prev=i[0]*Least//i[1]
    Final.append([prev,Least])
  return Final
print(convert_fracts([[1, 100], [3, 1000], [1, 2500], [1, 20000]]))


#Better Sol.
def convertFracts(lst):
    lcm = lambda a, b : abs(a*b) // math.gcd(a, b)
    tmp_list = list(map(lambda x : x[1] ,list(lst)))
    lcm_num = functools.reduce(lcm,tmp_list)
    return list(map(lambda x : [x[0] * lcm_num // x[1], lcm_num] , list(lst)))

print(convertFracts([[1, 100], [3, 1000], [1, 2500], [1, 20000]]))
