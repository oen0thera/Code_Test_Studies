import random
List=[0,1,2,3,4,5,6,7,8,9]
Count=0
Operand=0
Set=0
Appender=0
mul=1
Result=[]
for i in range(1,10):
    mul=mul*i

while Count<1000000:
    if Set==0 and Operand==0:
        Operand+=1
        Appender=List[0]
        List.remove(Appender)
        Count+=mul
    if Count<1000000 and Operand==1:
        List.append(Appender)
        Operand-=1
print(List)
