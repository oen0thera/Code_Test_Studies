import sys
file = open("fb_data.txt")

ids = [] #노드아이디
X = []
Y = []
for line in file:
    a,b,c = (int(x) for x in line.split())
    ids.append(a)
    X.append(b)
    Y.append(c)

mean_x = sum(X)/len(X)
mean_y = sum(Y)/len(Y)
std_x = (sum((x-mean_x)**2 for x in X)/len(X)) ** 0.5
std_y = (sum((y-mean_y)**2 for y in Y)/len(Y)) ** 0.5
cov = sum((x-mean_x)*(y-mean_y) for x,y in zip(X,Y))/len(X)
corr = cov/(std_x*std_y)

print("corr:",corr)
