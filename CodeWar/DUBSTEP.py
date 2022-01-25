# My Solution
def song_decoder(song):
    Song_list=[i for i in song]
    Pos_Recorder=[]
    RepeatedSets=set()
    for i in range(0,len(Song_list)):
      if Song_list.count(Song_list[i])>=2:
        Pos_Recorder.append(i)
    Confirmer=[]
    for i in Pos_Recorder:
      for j in range(0,len(Song_list)):
        if Song_list[j]==Song_list[i]:
          for k in range(i,j+1):
            if song.count(song[i:k])>=2 and song[i:k]!='' and len(song[i:k])==3 and ''.join(song[i:k])=='WUB':
              new_str=song.replace(song[i:k],' ')
              spliter=new_str.split()
              removeblank=' '.join(spliter)
              RepeatedSets.add(removeblank)
    RepeatedList = list(RepeatedSets)
    if RepeatedList:
      count=len(RepeatedList[0])
    else:
      new_str=song.replace("WUB",'')
      return new_str
    pos=0
    for i in range(0,len(RepeatedList)):
      if len(RepeatedList[i])<count:
        count=len(RepeatedList[i])
        pos=i

    return RepeatedList[pos]

#Far more Better solution(...)
def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())
