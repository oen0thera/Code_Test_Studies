'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''

def solution(string,markers):
    #your code here
    List=[]
    remover=[]
    new_string=string
    for _ in range(0,len(markers)):
      for i in markers:
        if i in string:
          if new_string=='':
            List=string.split(i)
            for i in range(0,len(List)):
              List[i]=blank_(List[i])

            for i in range(1,len(List)):
              if '\n' in List[i]:
                pos=List[i].index('\n')
                List[i]=List[i][pos:]
              else:
                remover.append(i)
            if remover:
              remover.sort()
              for i in range(len(remover)-1,-1,-1):
                del List[remover[i]]
            new_string=''.join(List)
            string=new_string
            remover=[]
          else:

            List=new_string.split(i)
            for i in range(0,len(List)):
              List[i]=blank_(List[i])

            for i in range(1,len(List)):
              if '\n' in List[i]:
                pos=List[i].index('\n')
                List[i]=List[i][pos:]
              else:
                remover.append(i)
            if remover:
              remover.sort()
              for i in range(len(remover)-1,-1,-1):
                del List[remover[i]]
            new_string=''.join(List)
            string=new_string
            remover=[]

    return new_string

def blank_(string):
  new_string=string
  if len(string)==0:
    return string
  if string[0]==' ':
    new_string = string[1:]
  if string[len(string)-1]==' ':
    new_string = string[:len(string)-1]

  return new_string
solution("apples, pears # and bananas\ngrapes\nbananas !#apples", ["#", "!"])

'''Better solution
def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)
'''
