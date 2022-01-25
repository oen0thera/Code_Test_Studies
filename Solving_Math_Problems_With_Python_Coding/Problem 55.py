'''
47이란 수를 골라서 뒤집은 다음 다시 원래 수에 더하면, 47 + 74 = 121 과 같이 대칭수(palindrome)가 됩니다.
물론 모든 수가 이토록 쉽게 대칭수를 만들어내지는 않습니다. 예를 들어 349의 경우,

349 + 943 = 1292
1292 + 2921 = 4213
4213 + 3124 = 7337

위에서 보는 것처럼 3번의 반복과정을 거쳐야 대칭수가 됩니다.

196과 같은 몇몇 수는 이와 같은 과정을 아무리 반복해도 대칭수가 되지 않을 것이라고 추측되는데, 이런 수를 라이크렐 수 (Lychrel number) 라고 부릅니다. 아직 증명되지는 않았지만, 문제 풀이를 위해서 일단 라이크렐 수가 존재한다고 가정하겠습니다.

또한 1만 이하의 수는, 50번 미만의 반복으로 대칭수가 되든지 라이크렐 수든지 둘 중 하나라고 합니다.
1만을 넘어서면 10677에 이르렀을 때 비로소 53번의 반복으로 4668731596684224866951378664 라는 28자리의 대칭수가 만들어집니다.

그러면 1만 이하에는 몇 개의 라이크렐 수가 존재합니까?
'''
def isPalindrome(inputs):
  input_list=[i for i in str(inputs)]
  count=0
  for i in range(0,(len(input_list)//2)):
    if input_list[i]==input_list[len(input_list)-(i+1)]:
      count+=1
  if count==len(input_list)//2 and len(input_list)>1:
    return True
  if count==len(input_list)//2 and len(input_list)<=1:
    return False

  if count!=len(input_list)//2:
    return False

from copy import copy
number=0
Palindrome_list=[]
Not_Palindrome=[]
while number<10000:
  number+=1
  Reversal=reversed([i for i in str(number)])
  Reversal_number=int(''.join(Reversal))
  if isPalindrome(number+Reversal_number):
    if number not in Palindrome_list:
      Palindrome_list.append(number)
  if not isPalindrome(number+Reversal_number):
    count=1
    New_number=copy(number)
    New_Reversal_number=copy(Reversal_number)
    More=New_number+New_Reversal_number
    next=0
    while count<50:
      if next==0:
        next+=1
        New_number=copy(More)
        New_Reversal=reversed([i for i in str(New_number)])
        New_Reversal_number=int(''.join(New_Reversal))
        More=New_number+New_Reversal_number
        if isPalindrome(More):
          if number not in Palindrome_list:
            Palindrome_list.append(number)
            break
        if not isPalindrome(More):
          count+=1
          next=0
    if count==50:
      Not_Palindrome.append(number)
print('Total counts of Lychrell Number lower than 10000 is {}'.format(10000-len(Palindrome_list)))
print('Lycrell Numbers List:{}'.format(Not_Palindrome))
