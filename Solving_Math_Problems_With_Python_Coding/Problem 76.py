def getWays(n):
  ways = [1] + [0] * n
  for i in range(1, n):
    for j in range(i, n+1):
      ways[j] += ways[j-i]
      print(ways)
  return ways[n]

print(getWays(100))
