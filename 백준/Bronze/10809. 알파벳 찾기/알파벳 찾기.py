alpha = [i for i in range(97,123)]
S = [ord(i) for i in input()]
result = [S.index(i) if i in S else -1 for i in alpha]
print(' '.join(str(i) for i in result))