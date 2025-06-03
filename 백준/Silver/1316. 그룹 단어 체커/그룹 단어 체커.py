count=0
for case in range(int(input())):
  word_set = list()
  word = input()
  for i in range(len(word)):
    if word[i] not in word_set:
      word_set.append(word[i])
      if i==len(word)-1:
        count+=1
    else:
      if word[i] == word_set.pop():
        word_set.append(word[i])
        if i==len(word)-1:
          count+=1
        continue
      break

print(count)