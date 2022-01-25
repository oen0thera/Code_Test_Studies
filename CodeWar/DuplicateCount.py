def duplicate_count(text):
    # Your code goes here
    Recorder=[]
    Text_List=[i for i in text.upper()]
    count=0
    for i in Text_List:
      if i not in Recorder and Text_List.count(i)>=2:
        count+=1
        Recorder.append(i)
    return count
