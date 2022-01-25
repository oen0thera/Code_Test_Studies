from collections import Counter
import sys
import matplotlib.pyplot as pyplot


file = open("f_num.txt")

num_friends = sorted(int(line.split()[1]) for line in file)
n = len(num_friends)

print("중심경향성")
#mean
mean = sum(num_friends) / len(num_friends)
print(f"mean: {mean}")

#median
median = num_friends[n//2]
if n%2==0:
        median = (median + num_friends[n//2 -1])/2
print(f"median: {median}")

#mode
count = Counter(num_friends)
mode = [c for c in count if c == max(count.values())]
print(f"mode: {mode}")

#max, min
print(f"min: {min(num_friends)}")
print(f"max: {max(num_friends)}")

#quantile
q10 = num_friends[int(0.25*n)]
q25 = num_friends[int(0.5*n)]
q90 = num_friends[int(0.75*n)]
print(f"quantile: {q10},{q25},{q90}")

print("\n\n")

print("산포도")
maxmin_range = max(num_friends) - min(num_friends)
var= sum((x-mean)**2 for x in num_friends) / len(num_friends)
sd = var ** 0.5
print(f"variance: {var}")
print(f"interquartile range: {q90-q10}")
print(f"standard_deviation: {sd}")

print("\n\n")

print("히스토그램")
hist = Counter(int(line.split()[1])// 10*10 for line in file)

pyplot.figure(figsize=(10,5))
pyplot.bar([x+5 for x in hist.keys()],hist.values(),width=10,color='blue',edgecolor="black")
pyplot.xlabel("# friends")
pyplot.ylabel("# peoples")
pyplot.title("Histogram of Friend Counts")
pyplot.savefig('test.png')
pyplot.show()
