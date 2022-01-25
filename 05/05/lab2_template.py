from collections import Counter
def solution(lst):
    c = Counter(lst)
    new= [x for x, y in c.items() if y == c.most_common()[0][1]]
    if len(new)==len(lst):
        return []
    return new
print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]
