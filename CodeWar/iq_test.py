'''
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
'''

def iq_test(numbers):
    #your code here
    List=numbers.split()
    odd=[]
    even=[]
    for i in List:
      if int(i)%2==0:
        even.append(int(i))
      else:
        odd.append(int(i))
    if len(even)>1:
      pos=List.index(str(odd[0]))+1
    elif len(odd)>1:
      pos=List.index(str(even[0]))+1
    return pos

iq_test("1 2 2")
