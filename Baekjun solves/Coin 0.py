
pos='''10 4790
1
5
10
50
100
500
1000
5000
10000
50000'''
Prime=pos.split('''\n''')
print(Prime)
Nums_and_Price=Prime[0].split(' ')
print(Nums_and_Price)
Prime.remove(Prime[0])
Prime.reverse()
print(Prime)
New=[int(i) for i in Prime]
print(New)
Price=int(Nums_and_Price[1])
count=0
for i in New:
  if i<=Price:
    count+=Price//i
    print(Price//i,i)
    Price=Price%i

    print(Price)
  if Price==0:
    break

print(count)
print(Price)
