'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''

def scramble(s1, s2):
    # your code here
    s2_list=[]
    for i in s2:
      if i not in s2_list and s1.count(i)>=s2.count(i):
        s2_list.append(i)
      elif i in s2_list:
        continue
      else:
        return False
    return True
scramble('cedewaraaossoqqyt', 'codewars')
