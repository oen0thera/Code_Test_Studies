def to_camel_case(text):
    #your code here
    List=[i for i in text]
    for _ in List:
      if '_' in List:
        for i in List:
          if i=='_':
            pos = List.index(i)
            List[pos+1]=List[pos+1].upper()
            List.remove(i)

      elif '-' in List:
        for i in List:
          if i=='-':
            pos = List.index(i)
            List[pos+1]=List[pos+1].upper()
            List.remove(i)
    return ''.join(List)
to_camel_case('')
