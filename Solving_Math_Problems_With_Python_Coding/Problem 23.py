#자신을 제외한 약수(진약수)를 모두 더하면 자기 자신이 되는 수를 완전수라고 합니다.
#예를 들어 28은 1 + 2 + 4 + 7 + 14 = 28 이므로 완전수입니다.
#또, 진약수의 합이 자신보다 작으면 부족수, 자신보다 클 때는 과잉수라고 합니다.

#12는 1 + 2 + 3 + 4 + 6 = 16 > 12 로서 과잉수 중에서는 가장 작습니다.
#따라서 과잉수 두 개의 합으로 나타낼 수 있는 수 중 가장 작은 수는 24 (= 12 + 12) 입니다.

#해석학적인 방법을 사용하면, 28123을 넘는 모든 정수는 두 과잉수의 합으로 표현 가능함을 보일 수가 있습니다.
#두 과잉수의 합으로 나타낼 수 없는 가장 큰 수는 실제로는 이 한계값보다 작지만, 해석학적인 방법으로는 더 이상 이 한계값을 낮출 수 없다고 합니다.

#그렇다면, 과잉수 두 개의 합으로 나타낼 수 없는 모든 양의 정수의 합은 얼마입니까?

'''
약수 찾기 시스템 사용
'''
Result = Solution(28123)
print(Result)
Over_number=[]
for i in range(0,len(Result)):
    if i+1<Result[i][0]:
        Over_number.append(i+1)

print(Over_number)

List = []
Less_than_28123=[i for i in range(1,28124)]
print(Less_than_28123)
for a in Over_number:
    for b in Over_number:
        if a+b<=28123 and a+b in Less_than_28123:
          Less_than_28123.remove(a+b)
          print(len(Less_than_28123))

print(Less_than_28123)

sum=0
for i in List:
  sum=sum+i
  print(sum)

print(sum)

#자세한 내용은 colab.research Untitled 17번 참조
