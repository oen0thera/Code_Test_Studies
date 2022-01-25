import copy

class Matrix:
  def __init__(self,*lst):
    self.data = list(lst)
    self.size = len(self.data)

  def __repr__(self):
    return f"Matrix({self.data})"

  def __add__(self,other):
    assert self.size==other.size, "두 매트릭스를 더하려면 크기가 같아야합니다."
    newlst=copy.deepcopy(self.data)
    temp=Matrix(*newlst)
    for vector in range(0,len(temp.data)):
      assert len(self.data[vector])==len(other.data[vector]), "두 매트릭스를 더하려면 크기가 같아야합니다."
      for number in range(0,len(temp.data[vector])):
        temp.data[vector][number]=temp.data[vector][number]+other.data[vector][number]
    return f"Matrix({temp.data})"

  def __sub__(self,other):
    assert self.size==other.size, "두 매트릭스를 빼려면 크기가 같아야합니다."
    newlst=copy.deepcopy(self.data)
    temp=Matrix(*newlst)
    for vector in range(0,len(temp.data)):
      assert len(self.data[vector])==len(other.data[vector]), "두 매트릭스를 빼려면 크기가 같아야합니다."
      for number in range(0,len(temp.data[vector])):
        temp.data[vector][number]=temp.data[vector][number]-other.data[vector][number]
    return f"Matrix({temp.data})"

  def __mul__(self,other):
    newlst=copy.deepcopy(self.data)
    temp=Matrix(*newlst)
    if type(other)==int:
      for vector in range(0,len(temp.data)):
        for number in range(0,len(temp.data[vector])):
          temp.data[vector][number]=temp.data[vector][number]*other
      return f"Matrix({temp.data})"
    elif type(other)==Matrix:
      newlst=copy.deepcopy(self.data)
      temp=Matrix(*newlst)
      templst=[]
      assert temp.size<=other.size, f"{temp}의 행은 {other}의 행보다 작거나 같아야합니다."
      for vector in range(0,len(temp.data)):
        assert len(temp.data[vector])==other.size, f"{temp}의 열과 {other}의 행이 맞지 않습니다.({len(temp.data[vector])} =/= {other.size})"
        tempitem=[]
        for count in range(0,len(other.data[vector])):
          item=0
          for number in range(0,len(temp.data[vector])):
            item+=temp.data[vector][number]*other.data[number][count]
          tempitem.append(item)
        templst.append(tempitem)
      return f"Matrix({templst})"

  def __rmul__(self,other):
    newlst=copy.deepcopy(self.data)
    temp=Matrix(*newlst)
    for vector in range(0,len(temp.data)):
      for number in range(0,len(temp.data[vector])):
        temp.data[vector][number]=temp.data[vector][number]*other
    return f"Matrix({temp.data})"

a=Matrix([1,2,3],[4,5,6])
b=Matrix([2,4,5],[1,2,3])
c=Matrix([1,2,3,4],[4,5,6,7])
d=Matrix([1,2],[3,4],[5,6],[7,8])
e=Matrix([5,10],[7,8])
f=Matrix([2,2],[4,4])
g=Matrix([0])
h=Matrix([1],[2],[3],[4])
i=Matrix([1,2,3,4])
m3=Matrix([1,2,1],[0,1,0],[2,3,4])
m2=Matrix([2,5],[6,7],[1,8])

print('a+b:',a+b)
print('a-b:',a-b)
print('3*a:',3*a)
print('b*4:',b*4)
print('c*d:',c*d)
print('e*f:',e*f)
print('e+f:',e+f)
print('e-f:',e-f)
print('e*0:',e*0)
print('0*e:',0*e)
print('-2*e:',-2*e)
print('m3*m2:',m3*m2)
print('c-a:',c-a)
print('a:',a)
print('b:',b)
print('c:',c)
print('d:',d)
print('e:',e)
print('f:',f)
print('g:',g)
print('m3:',m3)
print('m2:',m2)
