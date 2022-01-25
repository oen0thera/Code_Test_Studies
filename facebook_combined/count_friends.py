import sys
from collections import Counter
file = open('facebook_combined.txt')


cnt_friends = sorted(Counter(int(x) for line in file for x in line.split()).items())
#튜플화

for nid, cnt in cnt_friends:
    print(f"{nid}\t{cnt}")
