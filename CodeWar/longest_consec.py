'''
You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Examples:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

Note
consecutive strings : follow one after another without an interruption
'''
def longest_consec(strarr, k):
    # your code
  if k<=0 or len(strarr)<k or len(strarr)==0:
    return ""

  str_list=[]
  for i in range(0,len(strarr)):
    if len(strarr[i:i+k])==k:
      new_str = ''.join(strarr[i:i+k])
      if new_str not in str_list:
        str_list.append(new_str)
  Length=[]
  for i in str_list:
    Length.append(len(i))
  max_Length=max(Length)
  return str_list[Length.index(max_Length)]

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"],2)
