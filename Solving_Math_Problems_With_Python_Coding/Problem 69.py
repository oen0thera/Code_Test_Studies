number=5
comb_list=[]
zero_list=[]

for i in range(2,number+1):
    zero_list=[]
    for _ in range(i):
        zero_list.append(0)
    comb_list.append(zero_list)

print(comb_list)
