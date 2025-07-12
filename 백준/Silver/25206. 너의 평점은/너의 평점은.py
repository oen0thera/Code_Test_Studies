import sys
count=0
grade=0
grade_set = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}

#sys.stdin = open('input.txt')
readline = sys.stdin.readlines()
for line in readline:
    a,b,c = map(str,line.split())
    if c!='P':
      count+=float(b)
      grade+=grade_set[c]*float(b)

if(grade>0):
  print(grade/count)
else:
  print(grade)