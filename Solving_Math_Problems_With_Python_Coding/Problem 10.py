#n = 1000000
#lst = primeNum(n)

#Solution 2
n=3
setOfprimeNumbers=[2]
result=2

while setOfprimeNumbers[-1]<=2000000:
    for i in setOfprimeNumbers:
        if n%i == 0:
            break
        if i==setOfprimeNumbers[-1]:
            setOfprimeNumbers.append(n)
            print(setOfprimeNumbers[-1])
            result+=setOfprimeNumbers[-1]
            print('sum:{}'.format(result))
    n+=2

print('last prime number is', setOfprimeNumbers[-1])
print(result)
