'''
Given a number of points on a plane, your task is to find two points with the smallest distance between them in linearithmic O(n log n) time.

Example
  1  2  3  4  5  6  7  8  9
1
2    . A
3                . D
4                   . F
5             . C
6
7                . E
8    . B
9                   . G
For the plane above, the input will be:

(
  (2,2), # A
  (2,8), # B
  (5,5), # C
  (6,3), # D
  (6,7), # E
  (7,4), # F
  (7,9)  # G
)
=> closest pair is: ((6,3),(7,4)) or ((7,4),(6,3))
(both answers are valid. You can return a list of tuples too)
The two points that are closest to each other are D and F.
Expected answer should be an array with both points in any order.

Goal
The goal is to come up with a function that can find two closest points for any arbitrary array of points, in a linearithmic time.
'''
def closest_pair(points):
  result = divideandconquer(points)
  return (result[0],result[1])
def distance(a,b):
  print(a,b,':',(a[0]-b[0])**2+(a[1]-b[1])**2)
  return [a,b,(a[0]-b[0])**2+(a[1]-b[1])**2]

def divideandconquer(points):
  points=sorted(list(points),key=lambda x: x[0])
  if len(points)==2:
    return distance(points[0],points[1])
  elif len(points)==3:
    one=distance(points[0],points[1])
    two=distance(points[0],points[2])
    three=distance(points[1],points[2])
    if min(one[2],two[2],three[2])==one[2]:
      return one
    elif min(one[2],two[2],three[2])==two[2]:
      return two
    else:
      return three
  else:
    mid=len(points)//2
    new=min([divideandconquer(points[:mid]),divideandconquer(points[mid:])],key=lambda n: n[2])
    temp=[]
    for i in range(len(points)):
      if (points[i][0]-points[mid][0])**2<=new[2]:
        temp.append(points[i])
    if len(temp)>=2:
      temp.sort(key= lambda x: x[1])
      for i in range(len(temp)-1):
        for j in range(i+1,len(temp)):
          if temp[i]==temp[j]:
            new= [temp[i],temp[j],0]

          if (temp[i][1] - temp[j][1])**2>new[2]:
            break
          else:
            new=min(new,distance(temp[i],temp[j]),key=lambda n: n[2])


  return new

closest_pair(points=((2, 2), # A
            (2.2, 8), # B
            (5, 5), # C
            (6, 3), # D
            (6.5, 7), # E
            (7, 4), # F
            (7, 9)  # G
        ))
