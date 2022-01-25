#분수 49/98에는 재미있는 성질이 있습니다. 수학을 잘 모르는 사람이 분모와 분자에서 9를 각각 지워서 간단히 하려고 49/98 = 4/8 처럼 계산해도 올바른 결과가 됩니다.

#이에 비해 30/50 = 3/5 같은 경우는 다소 진부한 예라고 볼 수 있습니다.

#위와 같은 성질을 가지면서 '진부하지 않은' 분수는, 값이 1보다 작고 분자와 분모가 2자리 정수인 경우 모두 4개가 있습니다.

#이 4개의 분수를 곱해서 약분했을 때 분모는 얼마입니까?
offspring=[]
parent=[]
Result=[]
son=1
anc=1
count=0
for i in range(1,100):
  for j in range(1,100):
    if i<j:
      count=0
      offspring=[a for a in str(i)]
      parent=[b for b in str(j)]
      for a in offspring:
        if a in parent and a!='0':
          count+=1
          offspring.remove(a)
          parent.remove(a)
      if offspring and parent:
        New_offspring=''.join(offspring)
        New_parent=''.join(parent)

        if int(New_offspring)>0 and int(New_parent)>0:
          if int(New_offspring)/int(New_parent)==i/j and count>0 :
            Result.append('{}/{} = {}/{}'.format(int(New_offspring),int(New_parent),i,j))
            son=son*i
            anc=anc*j
            print(son)
            print(anc)
          New_offspring=''
          New_parent=''
          count=0

print(Result)
print(anc/son)
