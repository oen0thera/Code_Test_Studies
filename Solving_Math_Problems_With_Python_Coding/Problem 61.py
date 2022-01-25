def header(target:int):
  strtarget = str(target)
  listtarget= [i for i in strtarget]
  sublist = listtarget[0:2]
  head = int("".join(sublist))
  return head

def tailer(target:int):
  strtarget = str(target)
  listtarget= [i for i in strtarget]
  sublist = listtarget[2:4]
  tail = int("".join(sublist))
  return tail

def counting(number:int, result: list, counter:list, four:list,five:list, six:list, seven:list, eight:list):
  four_list=[]
  four_counter=[]
  five_list=[]
  five_counter=[]
  six_list=[]
  six_counter=[]
  seven_list=[]
  seven_counter=[]
  eight_list=[]
  eight_counter=[]

  if 4 not in counter:
    for i in four:
      if header(i) == number:
        four_list.append(i)
        four_counter.append(4)

  if 5 not in counter:
    for i in five:
      if header(i) == number:
        five_list.append(i)
        five_counter.append(5)

  if 6 not in counter:
    for i in six:
      if header(i) == number:
        six_list.append(i)
        six_counter.append(6)
  if 7 not in counter:
    for i in seven:
      if header(i)==number:
        seven_list.append(i)
        seven_counter.append(7)
  if 8 not in counter:
    for i in eight:
      if header(i)==number:
        eight_list.append(i)
        eight_counter.append(8)
  entry = four_list+five_list+six_list+seven_list+eight_list
  thres = four_counter+five_counter+six_counter+seven_counter+eight_counter
  return entry, thres


def third_party():
  newlist=[]
  for number in range(1000,9999):
    for i in range(1,999):
      if number== i*(i+1)/2:
        newlist.append(number)
  return newlist

def forth_party():
  newlist=[]
  for number in range(1000,9999):
    for i in range(1,999):
      if number== i*i:
        newlist.append(number)
  return newlist

def fifth_party():
  newlist=[]
  for number in range(1000,9999):
    for i in range(1,999):
      if number == i*(3*i-1)/2:
        newlist.append(number)
  return newlist

def sixth_party():
  newlist=[]
  for number in range(1000,9999):
    for i in range(1,999):
      if number == i*(2*i-1):
        newlist.append(number)
  return newlist

def seventh_party():
  newlist=[]
  for number in range(1000,9999):
    for i in range(1,999):
      if number == i*(5*i-3)/2:
        newlist.append(number)
  return newlist
def eighth_party():
  newlist=[]
  for number in range(1000,9999):
    for i in range(1,999):
      if number == i*(3*i-2):
        newlist.append(number)
  return newlist

thirdparty = third_party()
forthparty = forth_party()
fifthparty = fifth_party()
sixthparty = sixth_party()
seventhparty = seventh_party()
eighthparty = eighth_party()
counter=[3]
final=[]
for i in thirdparty:
  print(i)
  entry=[]
  thres=[]
  result=[i]
  thirdtail=0
  thirdhead = header(i)
  thirdtail = tailer(i)
  entry, thres = counting(thirdtail,result,counter,forthparty,fifthparty,sixthparty,seventhparty,eighthparty)
  for j in entry:
    enttail=tailer(j)
    oper=[]
    ande=[]
    ande.append(thres[entry.index(j)])
    oper,ande = counting(enttail,result,ande,forthparty,fifthparty,sixthparty,seventhparty,eighthparty)
    for k in oper:
      opertail=tailer(k)
      rose=[]
      yolk=[]
      yolk.append(ande[oper.index(k)])
      rose,yolk = counting(opertail,result,yolk,forthparty,fifthparty,sixthparty,seventhparty,eighthparty)
      for l in rose:
        rosetail=tailer(l)
        goat=[]
        tide=[]
        tide.append(yolk[rose.index(l)])
        goat,tide = counting(rosetail,result,tide,forthparty,fifthparty,sixthparty,seventhparty,eighthparty)
        for m in goat:
          goattail=tailer(m)
          toad=[]
          hubo=[]
          hubo.append(tide[goat.index(m)])
          toad,hubo = counting(goattail,result,hubo,forthparty,fifthparty,sixthparty,seventhparty,eighthparty)
          for n in toad:

            if tailer(n)==thirdhead :
              counter=[3]
              counter.append(thres[entry.index(j)])
              counter.append(ande[oper.index(k)])
              counter.append(yolk[rose.index(l)])
              counter.append(tide[goat.index(m)])
              counter.append(hubo[toad.index(n)])
              if sorted(counter)==[3,4,5,6,7,8]:
                print('result:',i,j,k,l,m,n)
                answer=i+j+k+l+m+n
                print('answer is :',answer)


  result=[]
  counter=[3]
