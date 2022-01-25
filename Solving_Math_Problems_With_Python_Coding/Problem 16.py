#1부터 5까지의 수를 영어로 쓰면 one, two, three, four, five 이고,
#각 단어의 길이를 더하면 3 + 3 + 5 + 4 + 4 = 19 이므로 사용된 글자는 모두 19개입니다.

#1부터 1,000까지 영어로 썼을 때는 모두 몇 개의 글자를 사용해야 할까요?

#참고: 빈 칸이나 하이픈('-')은 셈에서 제외하며, 단어 사이의 and 는 셈에 넣습니다.
#  예를 들어 342를 영어로 쓰면 three hundred and forty-two 가 되어서 23 글자,
#  115 = one hundred and fifteen 의 경우에는 20 글자가 됩니다.

What_Number_is_Missing=[]

def Categorize(Processer,i):
    if int(Processer[i])==0:
        Results=0
    if int(Processer[i])==1:
        Results=3
    if int(Processer[i])==2:
        Results=3
    if int(Processer[i])==3:
        Results=5
    if int(Processer[i])==4:
        Results=4
    if int(Processer[i])==5:
        Results=4
    if int(Processer[i])==6:
        Results=3
    if int(Processer[i])==7:
        Results=5
    if int(Processer[i])==8:
        Results=5
    if int(Processer[i])==9:
        Results=4
    return Results
def Categorize2(Processer,i):
    if int(Processer[i])==0:
        if int(Processer[i+1])==1:
            Results=3
        if int(Processer[i+1])==2:
            Results=3
        if int(Processer[i+1])==3:
            Results=5
        if int(Processer[i+1])==4:
            Results=4
        if int(Processer[i+1])==5:
            Results=4
        if int(Processer[i+1])==6:
            Results=3
        if int(Processer[i+1])==7:
            Results=5
        if int(Processer[i+1])==8:
            Results=5
        if int(Processer[i+1])==9:
            Results=4
    if int(Processer[i])==1:
        if int(Processer[i+1])==0:
            Results=3
        if int(Processer[i+1])==1:
            Results=6
        if int(Processer[i+1])==2:
            Results=6
        if int(Processer[i+1])==3:
            Results=8
        if int(Processer[i+1])==4:
            Results=8
        if int(Processer[i+1])==5:
            Results=7
        if int(Processer[i+1])==6:
            Results=7
        if int(Processer[i+1])==7:
            Results=9
        if int(Processer[i+1])==8:
            Results=8
        if int(Processer[i+1])==9:
            Results=8
    if int(Processer[i])==2:
        if int(Processer[i+1])==0:
            Results=0
        if int(Processer[i+1])==1:
            Results=3
        if int(Processer[i+1])==2:
            Results=3
        if int(Processer[i+1])==3:
            Results=5
        if int(Processer[i+1])==4:
            Results=4
        if int(Processer[i+1])==5:
            Results=4
        if int(Processer[i+1])==6:
            Results=3
        if int(Processer[i+1])==7:
            Results=5
        if int(Processer[i+1])==8:
            Results=5
        if int(Processer[i+1])==9:
            Results=4
        Results+=6
    if int(Processer[i])==3:
        if int(Processer[i+1])==0:
            Results=0
        if int(Processer[i+1])==1:
            Results=3
        if int(Processer[i+1])==2:
            Results=3
        if int(Processer[i+1])==3:
            Results=5
        if int(Processer[i+1])==4:
            Results=4
        if int(Processer[i+1])==5:
            Results=4
        if int(Processer[i+1])==6:
            Results=3
        if int(Processer[i+1])==7:
            Results=5
        if int(Processer[i+1])==8:
            Results=5
        if int(Processer[i+1])==9:
            Results=4
        Results+=6
    if int(Processer[i])==4:
        if int(Processer[i+1])==0:
            Results=0
        if int(Processer[i+1])==1:
            Results=3
        if int(Processer[i+1])==2:
            Results=3
        if int(Processer[i+1])==3:
            Results=5
        if int(Processer[i+1])==4:
            Results=4
        if int(Processer[i+1])==5:
            Results=4
        if int(Processer[i+1])==6:
            Results=3
        if int(Processer[i+1])==7:
            Results=5
        if int(Processer[i+1])==8:
            Results=5
        if int(Processer[i+1])==9:
            Results=4
        Results+=5
    if int(Processer[i])==5:
        if int(Processer[i+1])==0:
            Results=0
        if int(Processer[i+1])==1:
            Results=3
        if int(Processer[i+1])==2:
            Results=3
        if int(Processer[i+1])==3:
            Results=5
        if int(Processer[i+1])==4:
            Results=4
        if int(Processer[i+1])==5:
            Results=4
        if int(Processer[i+1])==6:
            Results=3
        if int(Processer[i+1])==7:
            Results=5
        if int(Processer[i+1])==8:
            Results=5
        if int(Processer[i+1])==9:
            Results=4
        Results+=5
    if int(Processer[i])==6:
        if int(Processer[i+1])==0:
            Results=0
        if int(Processer[i+1])==1:
            Results=3
        if int(Processer[i+1])==2:
            Results=3
        if int(Processer[i+1])==3:
            Results=5
        if int(Processer[i+1])==4:
            Results=4
        if int(Processer[i+1])==5:
            Results=4
        if int(Processer[i+1])==6:
            Results=3
        if int(Processer[i+1])==7:
            Results=5
        if int(Processer[i+1])==8:
            Results=5
        if int(Processer[i+1])==9:
            Results=4
        Results+=5
    if int(Processer[i])==7:
        if int(Processer[i+1])==0:
            Results=0
        if int(Processer[i+1])==1:
            Results=3
        if int(Processer[i+1])==2:
            Results=3
        if int(Processer[i+1])==3:
            Results=5
        if int(Processer[i+1])==4:
            Results=4
        if int(Processer[i+1])==5:
            Results=4
        if int(Processer[i+1])==6:
            Results=3
        if int(Processer[i+1])==7:
            Results=5
        if int(Processer[i+1])==8:
            Results=5
        if int(Processer[i+1])==9:
            Results=4
        Results+=7
    if int(Processer[i])==8:
        if int(Processer[i+1])==0:
            Results=0
        if int(Processer[i+1])==1:
            Results=3
        if int(Processer[i+1])==2:
            Results=3
        if int(Processer[i+1])==3:
            Results=5
        if int(Processer[i+1])==4:
            Results=4
        if int(Processer[i+1])==5:
            Results=4
        if int(Processer[i+1])==6:
            Results=3
        if int(Processer[i+1])==7:
            Results=5
        if int(Processer[i+1])==8:
            Results=5
        if int(Processer[i+1])==9:
            Results=4
        Results+=6
    if int(Processer[i])==9:
        if int(Processer[i+1])==0:
            Results=0
        if int(Processer[i+1])==1:
            Results=3
        if int(Processer[i+1])==2:
            Results=3
        if int(Processer[i+1])==3:
            Results=5
        if int(Processer[i+1])==4:
            Results=4
        if int(Processer[i+1])==5:
            Results=4
        if int(Processer[i+1])==6:
            Results=3
        if int(Processer[i+1])==7:
            Results=5
        if int(Processer[i+1])==8:
            Results=5
        if int(Processer[i+1])==9:
            Results=4
        Results+=6
    return Results
def Solution(Number_range):
    Number=1
    Processer=[]
    Results=0
    Count=0
    Str_Counter=[]
    while Number<=Number_range:
        Processer=[i for i in str(Number)]
        print(Processer)
        print(int(Processer[0]))
        if len(Processer)==1:
            Results=Categorize(Processer,0)
            Str_Counter.append(Results)
            What_Number_is_Missing.append(Number)
        if len(Processer)==2:
            Results=Categorize2(Processer,0)
            Str_Counter.append(Results)
            What_Number_is_Missing.append(Number)
        if len(Processer)==3:
            Results=Categorize(Processer,0)
            Count+=Results
            Count+=7
            print('Processing three numbers')
            if int(Processer[1])==0 and int(Processer[2])==0:
                Str_Counter.append(Count)
                print(Count)
                What_Number_is_Missing.append(Number)
            elif int(Processer[1])>=0 and int(Processer[2])!=0:
                Results=Categorize2(Processer,1)
                Count+=Results
                Count+=3
                Str_Counter.append(Count)
                print(Count)
                What_Number_is_Missing.append(Number)
            elif int(Processer[1])>0 and int(Processer[2])==0:
                Results=Categorize2(Processer,1)
                Count+=Results
                Count+=3
                Str_Counter.append(Count)
                print(Count)
                What_Number_is_Missing.append(Number)
            Count=0
        if len(Processer)==4:
            Str_Counter.append(11)
            What_Number_is_Missing.append(Number)
        Number+=1
        print(Results)
        print(Str_Counter)
        print(Number)
        Final=0
        for i in Str_Counter:
            Final+=i

        print('Final Sum = {}'.format(Final))
        print(len(Str_Counter))
        print(What_Number_is_Missing)
Solution(1000)
