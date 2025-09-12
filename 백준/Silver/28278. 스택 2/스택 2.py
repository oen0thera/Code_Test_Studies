import sys
input = sys.stdin.readline

class Stack:
  def __init__(self):
    self.stack_que=[]
  
  def exec(self):
    exec_lines = int(input())
    for _ in range(exec_lines):
      val = list(map(int,input().split()))
      if val[0] == 1: # push()
        self.stack_que.append(val[1])
      elif val[0] == 2: # pop()
        print( self.stack_que.pop() if len(self.stack_que)>0 else -1)
      elif val[0] == 3: # size()
        print(len(self.stack_que))
      elif val[0] == 4: # isEmpty()
        print( 0 if len(self.stack_que)>0 else 1)
      elif val[0] == 5: # peek
        print(self.stack_que[-1] if len(self.stack_que)>0 else -1)
      else:
        return

  def print(self):
    print(self.stack_que)
  
stack = Stack()
stack.exec()