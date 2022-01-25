'''
There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
'''

def recoverSecret(triplets):
  'triplets is a list of triplets from the secrent string. Return the string.'
  Interpret_lists=[]
  for i in triplets:
    print(i)
    if len(Interpret_lists)==0:
      Interpret_lists+=i
    else:
      pos=[]
      letters=[]
      for j in i:
        if j in Interpret_lists:
          pos.append(Interpret_lists.index(j))
          letters.append(j)
      if len(pos)==0:
        Interpret_lists+=i
      elif len(pos)==1:
        if i.index(letters[0])==0:
          Interpret_lists.insert(pos[0]+1,i[2])
          Interpret_lists.insert(pos[0]+1,i[1])

        elif i.index(letters[0])==1:
          Interpret_lists.insert(pos[0],i[0])
          Interpret_lists.insert(pos[0]+1,i[2])
        elif i.index(letters[0])==2:
          Interpret_lists.insert(pos[0],i[1])
          Interpret_lists.insert(pos[0],i[0])

      elif len(pos)==2:
        if i.index(letters[0])==0 and i.index(letters[1])==1:
            Interpret_lists.insert(pos[1]+1,i[2])

        elif i.index(letters[0])==1 and i.index(letters[1])==2:
            Interpret_lists.insert(pos[0],i[0])

        elif i.index(letters[0])==0 and i.index(letters[1])==2:
            Interpret_lists.insert(pos[1],i[1])

      elif len(pos)==3:
        if not pos[0]<pos[1]<pos[2]:
            if pos[0]>pos[1]:
              temp=Interpret_lists[pos[0]]
              del Interpret_lists[pos[0]]
              Interpret_lists.insert(pos[1],temp)
              pos[0]=pos[1]
              pos[1]=pos[1]+1

            if pos[0]>pos[2]:
              temp=Interpret_lists[pos[0]]
              del Interpret_lists[pos[0]]
              Interpret_lists.insert(pos[2],temp)
              pos[0]=pos[2]
              pos[2]=pos[2]+1

            if pos[1]>pos[2]:
              temp=Interpret_lists[pos[1]]
              del Interpret_lists[pos[1]]
              Interpret_lists.insert(pos[2],temp)
              pos[1]=pos[2]
              pos[2]=pos[2]+1
  for i in triplets:
    if not Interpret_lists.index(i[0])<Interpret_lists.index(i[1])<Interpret_lists.index(i[2]):
      if Interpret_lists.index(i[0])>Interpret_lists.index(i[1]):
        swap(Interpret_lists,Interpret_lists.index(i[0]),Interpret_lists.index(i[1]))
      if Interpret_lists.index(i[1])>Interpret_lists.index(i[2]):
        swap(Interpret_lists,Interpret_lists.index(i[0]),Interpret_lists.index(i[1]))
      if Interpret_lists.index(i[0])>Interpret_lists.index(i[2]):
        swap(Interpret_lists,Interpret_lists.index(i[0]),Interpret_lists.index(i[1]))

  return ''.join(Interpret_lists)

def swap(List:list,a:int,b:int):
  temp=List[a]
  List[a]=List[b]
  List[b]=temp

'''
better solve
def recoverSecret(triplets):
  r = list(set([i for l in triplets for i in l]))
  for l in triplets:
    fix(r, l[1], l[2])
    fix(r, l[0], l[1])
  return ''.join(r)

def fix(l, a, b):
   """let l.index(a) < l.index(b)"""
   if l.index(a) > l.index(b):
       l.remove(a)
       l.insert(l.index(b), a)
'''
