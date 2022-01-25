def path_finder(area):
  Matrix=[list(i) for i in area.split('\n')]
  col=0
  row=0
  Closed=[]
  Opened=[]
  Result=[]
  for i in Matrix:
    print(i)
  naver = neighbor(5,4,Matrix)
  print(naver)
  print()
  Result=A_star(Closed,Opened,Result,col,row,Matrix)
  print(sum(Result))
def A_star(Closed,Opened,G_sum,row,col,Matrix):
  if col==len(Matrix)-1 and row==len(Matrix)-1:
    Closed.append([Matrix[col][row],(row,col)])
    print(Closed)
    print('G_sum:',G_sum)
    return G_sum
  print('r:',row,'c:',col)
  current_pos=[Matrix[col][row],(row,col)]
  Closed.append([Matrix[col][row],(row,col)])
  Naver=neighbor(row,col,Matrix)
  G_List=[]
  F_List=[]
  for i in Naver:
    if i not in Opened and i not in Closed:
      Opened.append(i)
  for i in Opened:
    G=G_distance([Matrix[col][row],(row,col)],i)
    G_List.append(G)
  for g in range(0,len(G_List)):
    F=F_distance(G_List[g],Opened[g][1][0],Opened[g][1][1],Matrix)
    F_List.append(F)
  print('Opened:',Opened,'F:',F_List)
  count=F_List[0]
  count_pos=0
  for f in range(0,len(F_List)):
    print(F_List[f],'f_pos:',f,'curr_row:',row,'curr_col:',col,'f_row:',Opened[f][1][0],'f_col:',Opened[f][1][1],'count_pos:',count_pos,'row:',Opened[count_pos][1][0],'col:',Opened[count_pos][1][1])
    if F_List[f]<=count and Opened[f]!=current_pos and Opened[f] not in Closed:
      count_pos=f
      count=F_List[f]
      print('count_pos:',count_pos,'row:',Opened[count_pos][1][0],'col:',Opened[count_pos][1][1])

  print(Opened[count_pos],G_List[count_pos],count)
  print('Closed:',Closed)
  G_sum.append(G_List[count_pos])
  G_sum=A_star(Closed,Opened,G_sum,Opened[count_pos][1][0],Opened[count_pos][1][1],Matrix)
  return G_sum
def neighbor(row,col,Matrix):
  neighbor=[]
  if row==0 and col==0:
    neighbor.append([Matrix[col][row+1],(row+1,col)])
    neighbor.append([Matrix[col+1][row],(row,col+1)])
    return neighbor
  elif row==0 and col<len(Matrix)-1:
    neighbor.append([Matrix[col-1][row],(row,col-1)])
    neighbor.append([Matrix[col][row+1],(row+1,col)])
    neighbor.append([Matrix[col+1][row],(row,col+1)])
    return neighbor
  elif row<len(Matrix)-1 and col==0:
    neighbor.append([Matrix[col][row-1],(row-1,col)])
    neighbor.append([Matrix[col][row+1],(row+1,col)])
    neighbor.append([Matrix[col+1][row],(row,col+1)])
    return neighbor
  elif row<len(Matrix)-1 and col<len(Matrix)-1:
    neighbor.append([Matrix[col-1][row],(row,col-1)])
    neighbor.append([Matrix[col][row-1],(row-1,col)])
    neighbor.append([Matrix[col][row+1],(row+1,col)])
    neighbor.append([Matrix[col+1][row],(row,col+1)])
    return neighbor
  elif row==len(Matrix)-1 and col<len(Matrix)-1:
    if col>0:
      neighbor.append([Matrix[col-1][row],(row,col-1)])
    neighbor.append([Matrix[col+1][row],(row,col+1)])
    neighbor.append([Matrix[col][row-1],(row-1,col)])
    return neighbor
  elif col==len(Matrix)-1 and row<len(Matrix)-1:
    if row>0:
      neighbor.append([Matrix[col][row-1],(row-1,col)])
    neighbor.append([Matrix[col][row+1],(row+1,col)])
    neighbor.append([Matrix[col-1][row],(row,col-1)])
    return neighbor
  else:
    return neighbor

def F_distance(G_distance,row,col,Matrix):
  print('(',row,col,') -> (',len(Matrix)-1,len(Matrix)-1,')',G_distance+(len(Matrix)-1-row)+(len(Matrix)-1-col))
  return G_distance+(len(Matrix)-1-row)+(len(Matrix)-1-col)

def G_distance(current_pos,object_pos):
  print(current_pos[0],'-',object_pos[0], '=',abs(int(current_pos[0])-int(object_pos[0])))
  return abs(int(current_pos[0])-int(object_pos[0]))
