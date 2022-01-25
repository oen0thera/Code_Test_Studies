'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:
rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''
'''
RGB
00~09:10
0A~0F:6
10~19:10
1A~1F:6
20~29:10
2A~2F:6
30~39:10
3A~3F:6
40~49:10
4A~4F:6
50~59:10
5A~5F:6
60~69:10
6A~6F:6
70~79:10
7A~7F:6
80~89:10
8A~8F:6
90~99:10
9A~9F:6 -160
A0~A9:10
AA~AF:6
B0~B9:10
BA~BF:6
C0~C9:10
CA~CF
D0~D9
DA~DF
E0~E9
EA~EF
F0~F9
FA~FF -96
'''

count=-1
RGB_Dict={}
Alpha_list=['A','B','C','D','E','F']
for i in range(0,10):
  for j in range(0,10):
    count+=1
    RGB_Dict[count]=str(i)+str(j)
  for k in Alpha_list:
    count+=1
    RGB_Dict[count]=str(i)+k
for i in Alpha_list:
  for j in range(0,10):
    count+=1
    RGB_Dict[count]=str(i)+str(j)
  for k in Alpha_list:
    count+=1
    RGB_Dict[count]=str(i)+k

def rgb(r, g, b):
    #your code here :)
    red=finder(r)
    green=finder(g)
    blue=finder(b)

    total_RGB=red+green+blue

    return total_RGB

def finder(color):
  return_RGB=0
  if color>255:
    return_RGB=RGB_Dict[255]
  elif color<0:
    return_RGB=RGB_Dict[0]
  else:
    return_RGB=RGB_Dict[color]
  return return_RGB

rgb(-20,275,125)
