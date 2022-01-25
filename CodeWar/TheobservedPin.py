'''
Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we are counting on you!

For C# user: Do not use Mono. Mono is too slower when run your code.

ALGORITHMS
'''
import copy

def get_pins(observed):
  '''TODO: This is your job, detective!'''
  number_list=[i for i in observed]
  predicted_number=[]
  recorder=[]
  result=[]
  for i in number_list:
    print(i)
    predicted_number.append(predicter(i))
  return digit_maker(predicted_number[0],predicted_number,recorder,0,result)

def predicter(number:str):
  i=int(number)
  if i==1:
    return['1','2','4']
  elif i==2:
    return['1','2','3','5']
  elif i==3:
    return['2','3','6']
  elif i==4:
    return['1','4','5','7']
  elif i==5:
    return['2','4','5','6','8']
  elif i==6:
    return['3','5','6','9']
  elif i==7:
    return['4','7','8']
  elif i==8:
    return['5','7','8','9','0']
  elif i==9:
    return['6','8','9']
  else:
    return ['8','0']

def digit_maker(target:list,total:list,recorder:list,current_num:int,result:list):
  for i in target:
    if len(total)==1:
      return total[0]
    if len(recorder)==0 and len(total)>1:
      recorder.append(i)
      current_num+=1
      print('r:',recorder)
      digit_maker(total[current_num],total,recorder,current_num,result)
      recorder=[]
      current_num=0
    elif len(recorder)>0 and len(total)>1 and len(recorder)<len(total)-1:
      copied=copy.deepcopy(recorder)
      copied.append(i)
      current_num+=1
      print('c:',copied,'current_num:',current_num)
      digit_maker(total[current_num],total,copied,current_num,result)
      current_num-=1
    elif len(recorder)==len(total)-1 and len(total)>1:
      copied=copy.deepcopy(recorder)
      copied.append(i)
      print('c:',copied,'current_num:',current_num)

      result.append(''.join(copied))
      copied=recorder
  return result

print(get_pins('9173'))
