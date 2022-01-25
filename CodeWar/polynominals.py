'''
When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):

All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
"cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab" #알파벳순 정렬, 짧은 순서대로 정렬
                                                                    #계산가능한경우 계산



All monomials appears in order of increasing number of variables, e.g.:
"-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
"a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

There is no leading + sign if the first coefficient is positive, e.g.:
"-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials, so you won't find something like `-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.

Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english alphabet.

Good Work :)
'''

'''
# First Sol
def simplify(poly):
  Oper = {'+':0,'-':1}
  Result=[]
  charset=set()
  List=[]
  st=0
  if poly[0]!='-':
    poly='+'+poly
  for ch in range(1,len(poly)):
      if poly[ch] in Oper:
        new_str=poly[st+1:ch]
        number,alpha = separator(new_str)
        if ch>0 and poly[st]=='-':
          number.insert(0,'-')
        if number==[] or number==['-']:
          number.append('1')
        if ''.join(alpha) not in charset:
          Result.append([int(''.join(number)),''.join(alpha)])
          charset.add(''.join(alpha))
        else:
          for i in Result:
            if i[1]==''.join(alpha):
              i[0]=i[0]+int(''.join(number))
        st=ch
      if ch==len(poly)-1:
        new_str=poly[st+1:ch+1]
        number,alpha = separator(new_str)
        if ch>0 and poly[st]=='-':
          number.insert(0,'-')
        if number==[] or number==['-']:
          number.append('1')
        if ''.join(alpha) not in charset:
          Result.append([int(''.join(number)),''.join(alpha)])
          charset.add(''.join(alpha))
        else:
          for i in Result:
            if i[1]==''.join(alpha):
              i[0]=i[0]+int(''.join(number))


  Result=Sorter(Result)
  Final=joiner(Result)

  return ''.join(Final)

def separator(new_str):
  alpha=[]
  number=[]
  for i in new_str:
    if i in 'abcdefghijklmnopqrstuvwxyz':
      alpha.append(i)
    else:
      number.append(i)
  alpha.sort()

  return number,alpha

def Sorter(Result):
  done=False
  done2=False
  length_List=[]
  alpha_Dict={}
  dict_c=0
  for i in Result:
    length_List.append(len(i[1]))
  for i in 'abcdefghijklmnopqrstuvwxyz':
    if len(str(dict_c))==1:
      appender='0'+str(dict_c)
    else:
      appender=str(dict_c)
    alpha_Dict[i]=appender
    dict_c+=1
  sp=0

  while done==False:
    for i in range(0,len(length_List)-1):
      if sp==len(length_List)-1:
        done=True
        break
      if length_List[i]<=length_List[i+1]:
        sp+=1
      else:
        temp=length_List[i+1]
        result_temp=Result[i+1]
        del length_List[i+1]
        del Result[i+1]
        length_List.insert(sp,temp)
        Result.insert(sp,result_temp)
        sp=0
        break

  sp=0
  alpha_List=[]
  for i in Result:
    new_num=''
    for j in i[1]:
      new_num+=str(alpha_Dict[j])
    alpha_List.append(new_num)

  #[1, 1, 2, 2, 2, 3]
  #['0', '2', '13', '34', '12', '012']

  sp=0
  while done2==False:
    for i in range(0,len(length_List)-1):
      if sp==len(length_List)-2:
        done2=True
        break

      if length_List[i]==length_List[i+1]:
        if length_List[i]<=length_List[i+1] and int(alpha_List[i])<int(alpha_List[i+1]):
          sp=i
        else:
          sp=i
          temp=alpha_List[i+1]
          temp2=length_List[i+1]
          result_temp=Result[i+1]
          del length_List[i+1]
          del alpha_List[i+1]
          del Result[i+1]
          length_List.insert(sp,temp2)
          alpha_List.insert(sp,temp)
          Result.insert(sp,result_temp)
          sp=0
          break
  print(length_List,alpha_List,Result)
  return Result

def joiner(Result):
  Final=[]
  for i in range(0,len(Result)):
    if i==0 and Result[i][0]==1:
      Final.append(Result[i][1])
    elif i==0 and Result[i][0]>1:
      Final.append(Result[i][0])
      Final.append(Result[i][1])
    elif Result[i][0]==-1:
      Final.append('-')
      Final.append(Result[i][1])
    elif Result[i][0]>1:
      Final.append('+')
      Final.append(str(Result[i][0]))
      Final.append(Result[i][1])
    elif i>0 and Result[i][0]==1:
      Final.append('+')
      Final.append(Result[i][1])
    elif i>0 and Result[i][0]==-1:
      Final.append('-')
      Final.append(Result[i][1])
    elif Result[i][0]<0:
      Final.append(str(Result[i][0]))
      Final.append(Result[i][1])

  return Final
print(simplify("xzy+zby"))
'''
def simplify(poly):
  #SecondSol
  Total=[]
  alpha=[]
  oper=[]
  Res=[]
  if poly[0]=='+':
    pass
  elif poly[0]!='-':
    poly='+'+poly
  for i in poly:
    if len(oper)!=0 and i in 'abcdefghijklmnopqrstuvwxyz':
      Total.append(oper)
      oper=[]
    if len(alpha)!=0 and i not in 'abcdefghijklmnopqrstuvwxyz':
      Total.append(sorted(alpha))
      alpha=[]
    if i not in 'abcdefghijklmnopqrstuvwxyz':
      oper.append(i)
    elif i in 'abcdefghijklmnopqrstuvwxyz' :
      alpha.append(i)
  if len(alpha)!=0:
    Total.append(sorted(alpha))
  print(Total)


  for i in range(0,len(Total)):
    if Total[i]==['+']:
      Total[i]=['+1']
      onechar=[Total[i][0],''.join(Total[i+1])]
      Res.append(onechar)
    elif Total[i]==['-']:
      Total[i]=['-1']
      onechar=[Total[i][0],''.join(Total[i+1])]
      Res.append(onechar)
    elif Total[i][0]=='+' or Total[i][0]=='-':
      Total[i]=[''.join(Total[i])]
      onechar=[Total[i][0],''.join(Total[i+1])]
      Res.append(onechar)

  print(Res)

  a_dict={}
  count=0

  for a in 'abcdefghijklmnopqrstuvwxyz':
    if count<10:
      code='0'+str(count)
      a_dict[a]=code
    else:
      a_dict[a]=str(count)
    count+=1
  print(a_dict)

  codeset=set()
  Removelist=[]

  for i in Res:
    codelist=''
    for j in i[1]:
      codelist+=a_dict[j]
    if codelist not in codeset:
      i.insert(0,codelist)
      codeset.add(codelist)
      print(codeset)
    else:
      for k in Res:
        if k[0]==codelist:
          print('k:',k,'i:',i)
          new_num=int(k[1])+int(i[0])
          print(new_num)
          if new_num>0:
            k[1]='+'+str(new_num)
          else:
            k[1]=str(new_num)
          Removelist.append(i)
          print(Removelist)
  for i in Removelist:
    Res.remove(i)
    print(Res)
  print(Res)
  Final=[]
  count=2
  while len(Final)<len(Res):
    same_length=[]
    for i in Res:
      if len(i[0])==count:
        same_length.append(i)
    same_length.sort()
    print(same_length)
    Final=Final+same_length
    print(Final)
    count+=2

  Result=''
  for last in Final:
    if last[1]=='+1':
      Result=Result+'+'+last[2]
    elif last[1]=='-1':
      Result=Result+'-'+last[2]
    elif last[1]=='0':
      pass
    else:
      Result=Result+last[1]+last[2]
  if Result[0]=='+':
    Result=Result[1:]

  return Result

print(simplify("xzy+zby"))

'''''
#BetterSol
def simplify(poly):
    # I'm feeling verbose today

    # get 3 parts (even if non-existent) of each term: (+/-, coefficient, variables)
    import re
    matches = re.findall(r'([+\-]?)(\d*)([a-z]+)', poly)

    # get the int equivalent of coefficient (including sign) and the sorted variables (for later comparison)
    expanded = [[int(i[0] + (i[1] if i[1] != "" else "1")), ''.join(sorted(i[2]))] for i in matches]

    # get the unique variables from above list. Sort them first by length, then alphabetically
    variables = sorted(list(set(i[1] for i in expanded)), key=lambda x: (len(x), x))

    # get the sum of coefficients (located in expanded) for each variable
    coefficients = {v:sum(i[0] for i in expanded if i[1] == v) for v in variables}

    # clean-up: join them with + signs, remove '1' coefficients, and change '+-' to '-'
    return '+'.join(str(coefficients[v]) + v for v in variables if coefficients[v] != 0).replace('1','').replace('+-','-')

'''''
