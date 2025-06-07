for case in range(int(input())):
  str_input = input()
  def isPalindrome(sp,ep,count,str_input):
    if str_input[sp]==str_input[ep]:
      if(sp>=ep): 
        print(1,count+1)
        return
      return isPalindrome(sp+1,ep-1,count+1,str_input)
    else:
      print(0,count+1)
      return
  isPalindrome(0,len(str_input)-1,0,str_input)

