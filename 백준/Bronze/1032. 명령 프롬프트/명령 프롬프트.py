def cmd(files):
    rec=[]
    for i in files:
        if(len(files)==1):
                return i
        else:
            if len(rec)==0:
                rec= [s for s in i]
            else:
                for j in range(len(rec)):
                    if i[j]==rec[j]:
                        pass
                    else:
                        rec[j]='?'
    return ''.join(rec)

c = int(input())
files = [input() for _ in range(c)]
print(cmd(files))