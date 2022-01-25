def Solution(n):
    mul=1
    for i in range(1,n+1):
        mul=mul*i

    List=[m for m in str(mul)]
    Final=0
    for j in List:
        Final=Final+int(j)

    print(Final)

Solution(100)
