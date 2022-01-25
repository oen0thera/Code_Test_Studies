a=()
b=(1)
c=(11,12,13,14)
d=(100,101,'a','b','c')
e=(100,101,('a','b','c'))
print('d-',d[1])
print('d-',d[-1])
print('e-',list(e[-1][1]))
print('d-',e[2:])

t=('foo','bar','baz','qux')

(x1,x2,x3,x4) = t
print( type(x1), type(x2), type(x3), type(x4))
print(x1,x2,x3,x4)

t2 = 1, 2, 3
t3 = 4,

x1,x2,x3 = t2
x4,x5,x6 = 4, 5, 6

print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)
