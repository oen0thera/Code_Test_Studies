'''
온라인 뱅킹에서 흔히 쓰이는 보안 기법 중에는, 비밀번호에 포함된 숫자를 랜덤하게 세 개 입력하도록 하는 것이 있습니다.
예를 들어 531278이라는 비밀번호에 대해서 2번째, 3번째, 5번째 숫자를 입력하도록 하는 식입니다. 이 때 올바른 입력은 317이 됩니다.

첨부한 텍스트 파일 keylog.txt에는 로그인에 성공한 어떤 사용자의 입력 기록이 50건 담겨져 있습니다. (비밀번호의 길이는 알 수 없습니다)

3개의 숫자는 항상 앞쪽부터 순서대로 요청된다고 할 때, 위의 접속 기록에서 알아낼 수 있는 가장 짧은 길이의 비밀번호는 무엇입니까?
'''

numbers='''319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716'''
numbers_list=[str(i) for i in numbers.split('\n')]
print(numbers_list)

keylog=[]
ex_key=[]
for i in numbers_list:
  ex_key=[j for j in str(i)]
  print(ex_key)
  start=0
  middle=0
  end=0

  if ex_key[0] not in keylog and ex_key[1] not in keylog and ex_key[2] not in keylog: # X X X
    keylog.append(ex_key[0])
    keylog.append(ex_key[1])
    keylog.append(ex_key[2])
    print(keylog)
  elif ex_key[0] in keylog and ex_key[1] not in keylog and ex_key[2] not in keylog: # O X X
    print('ket')
    start=keylog.index(ex_key[0])
    keylog.insert(start+1,ex_key[2])
    keylog.insert(start+1,ex_key[1])
    print(keylog)
  elif ex_key[0] in keylog and ex_key[1] in keylog and ex_key[2] not in keylog: # O O X
    if keylog.index(ex_key[0])<keylog.index(ex_key[1]):
      middle=keylog.index(ex_key[1])
      keylog.insert(middle+1,ex_key[2])
    elif keylog.index(ex_key[0])>keylog.index(ex_key[1]):
      start=keylog.index(ex_key[0])
      middle=keylog.index(ex_key[1])
      keylog.remove(ex_key[0])
      keylog.insert(middle,ex_key[0])
      keylog.remove(ex_key[1])
      keylog.insert(start,ex_key[1])

    print(keylog)
  elif ex_key[0] in keylog and ex_key[1] not in keylog and ex_key[2] in keylog: # O X O
    if keylog.index(ex_key[0])<keylog.index(ex_key[2]):
      end=keylog.index(ex_key[2])
      keylog.insert(end-1,ex_key[1])
    elif keylog.index(ex_key[0])>keylog.index(ex_key[2]):
      start=keylog.index(ex_key[0])
      end=keylog.index(ex_key[2])
      keylog.remove(ex_key[0])
      keylog.insert(end,ex_key[0])
      keylog.remove(ex_key[2])
      keylog.insert(start,ex_key[2])

    print(keylog)
  elif ex_key[0] not in keylog and ex_key[1] not in keylog and ex_key[2] in keylog: # X X O
    end=keylog.index(ex_key[2])
    keylog.insert(end-1,ex_key[1])
    keylog.insert(end-1,ex_key[0])
    print(keylog)
  elif ex_key[0] not in keylog and ex_key[1] in keylog and ex_key[2] in keylog: # X O O
    middle = keylog.index(ex_key[1])
    end = keylog.index(ex_key[2])
    if middle<end:
      keylog.insert(middle-1,ex_key[0])
    elif middle>end:
      keylog.remove(ex_key[1])
      keylog.insert(end,ex_key[1])
      keylog.remove(ex-key[2])
      keylog.insert(middle,ex_key[2])

    print(keylog)
  elif ex_key[0] not in keylog and ex_key[1] in keylog and ex_key[2] not in keylog:
    middle=keylog.index(ex_key[1])
    keylog.insert(middle+1,ex_key[2])
    keylog.insert(middle,ex_key[0])
  elif ex_key[0] in keylog and ex_key[1] in keylog and ex_key[2] in keylog:
    start=keylog.index(ex_key[0])
    middle=keylog.index(ex_key[1])
    end=keylog.index(ex_key[2])

    if start<middle and middle<end:
      pass
    elif start>middle:
      start=keylog.index(ex_key[0])
      middle=keylog.index(ex_key[1])
      keylog.remove(ex_key[0])
      keylog.insert(middle,ex_key[0])
      keylog.remove(ex_key[1])
      keylog.insert(start,ex_key[1])

      print(start)
      print(middle)
    elif start>end:
      start=keylog.index(ex_key[0])
      end=keylog.index(ex_key[2])
      keylog.remove(ex_key[0])
      keylog.insert(end,ex_key[0])
      keylog.remove(ex_key[2])
      keylog.insert(start,ex_key[2])

      print(start)
      print(end)
    elif middle>end:
      middle=keylog.index(ex_key[1])
      end=keylog.index(ex_key[2])
      keylog.remove(ex_key[1])
      keylog.insert(end,ex_key[1])
      keylog.remove(ex_key[2])
      keylog.insert(middle,ex_key[2])

      print(middle)
      print(end)
  print(keylog)



print(''.join(keylog))
