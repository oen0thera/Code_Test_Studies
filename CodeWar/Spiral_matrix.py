'''
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
'''
import sys
sys.setrecursionlimit(10**7)

def spiralize(size):
    # Make a snake
    Matrix=[[0 for i in range(0,size)] for j in range(0,size)]
    startpoint=Matrix[0][0]
    currentRow=0
    currentCol=0
    Matrix=drawer(Matrix,startpoint,currentRow,currentCol,'right')

    print('printing result')
    for i in Matrix:
      print(i)
    return Matrix

def showMatrix(Matrix):
  for i in Matrix:
    print(i)

def drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection):
  if currentdirection=='stop':
    return
  if currentdirection=='right':
    if currentRow<len(Matrix[0])-1 and Matrix[currentCol+1][currentRow-1]==1 and Matrix[currentCol+1][currentRow]==1:
      currentdirection='stop'
      drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)
    if currentRow<len(Matrix[0])-1 and Matrix[currentCol][currentRow+1]==0 and currentdirection!='stop':
      if currentRow<=len(Matrix[0])-3 and Matrix[currentCol][currentRow+2]==1:
        Matrix[currentCol][currentRow]=1
        currentdirection='down'
        currentCol+=1
        currentpoint=Matrix[currentCol][currentRow]
        drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)
        currentdirection='stop'

      if currentdirection!='stop':

        Matrix[currentCol][currentRow]=1
        currentRow+=1
        currentpoint=Matrix[currentCol][currentRow]
        drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)
        currentdirection='stop'

    elif currentRow==len(Matrix[0])-1:
      if currentdirection!='stop':

        Matrix[currentCol][currentRow]=1
        currentdirection='down'
        currentCol+=1
        currentpoint=Matrix[currentCol][currentRow]
        drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)
        currentdirection='stop'

  if currentdirection=='down':

    if currentCol<len(Matrix[0])-1 and Matrix[currentCol+1][currentRow]==0 and currentdirection!='stop':
      if currentCol<=len(Matrix[0])-3 and Matrix[currentCol+2][currentRow]==1:
        Matrix[currentCol][currentRow]=1
        currentdirection='left'
        currentRow-=1
        currentpoint=Matrix[currentCol][currentRow]
        drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)
        currentdirection='stop'

      if currentdirection!='stop':
        Matrix[currentCol][currentRow]=1
        currentCol+=1
        currentpoint=Matrix[currentCol][currentRow]
        drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)
        currentdirection='stop'

    elif currentCol==len(Matrix[0])-1:
      if currentdirection!='stop':

        Matrix[currentCol][currentRow]=1
        currentdirection='left'
        currentRow-=1
        currentpoint=Matrix[currentCol][currentRow]
        drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)
        currentdirection='stop'

  if currentdirection=='left':
    if currentRow<len(Matrix[0])-1 and Matrix[currentCol-1][currentRow+1]==1 and Matrix[currentCol-1][currentRow]==1:
      currentdirection='stop'
      drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)

    if currentRow>0 and Matrix[currentCol][currentRow-1]==0 and currentdirection!='stop':

      if currentRow>=2 and Matrix[currentCol][currentRow-2]==1:
        Matrix[currentCol][currentRow]=1
        currentdirection='up'
        currentCol-=1
        currentpoint=Matrix[currentCol][currentRow]
        drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)
        currentdirection='stop'

      if currentdirection!='stop':
        Matrix[currentCol][currentRow]=1
        currentRow-=1
        currentpoint=Matrix[currentCol][currentRow]
        drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)
        currentdirection='stop'

    elif currentRow==0:
      if currentdirection!='stop':

        Matrix[currentCol][currentRow]=1
        currentdirection='up'
        currentCol-=1
        currentpoint=Matrix[currentCol][currentRow]
        drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)
        currentdirection='stop'

  if currentdirection=='up':
    if currentCol>0 and Matrix[currentCol-1][currentRow]==0 and currentdirection!='stop':
      if currentCol>=2 and Matrix[currentCol-2][currentRow]==1:
        Matrix[currentCol][currentRow]=1
        currentdirection='right'
        currentRow+=1
        currentpoint=Matrix[currentCol][currentRow]
        drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)
        currentdirection='stop'

      if currentdirection!='stop':
        Matrix[currentCol][currentRow]=1
        currentCol-=1
        currentpoint=Matrix[currentCol][currentRow]
        drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)
        currentdirection='stop'

    elif currentCol==0:
      if currentdirection!='stop':
        Matrix[currentCol][currentRow]=1
        currentdirection='right'
        currentRow+=1
        currentpoint=Matrix[currentCol][currentRow]
        drawer(Matrix,currentpoint,currentRow,currentCol,currentdirection)
        currentdirection='stop'


  return Matrix
spiralize(39)
