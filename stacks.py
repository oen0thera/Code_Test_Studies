class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

# 수식이 문자열로 주어져 있을 때 (몇자리수인지 모르는 상태)
# 각각을 피연산자인 수와 연산자인 기호로 분리해서 리스트로 만드는 작업
# exprStr -> 중위표현 수식
def splitTokens(expStr):
    tokens = []
    val = 0 # 각 자리 숫자를 담은 변수
    valProcessing = False # 변수프로세스 false로 초기화
    for c in expStr:
        if c == ' ': # 빈칸이 들어 있으면 패스
            continue
        if c in '0123456789': # 숫자를 10진수로 변환하는 과정
            val = val * 10 + int(c)
            valProcessing = True # 숫자를 만났음으로 True로 변환
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False # 10진수가 아님으로 False로 다시 변환
            tokens.append(c)
    if valProcessing: # 변수프로세스 확인 후 변수처리
        tokens.append(val)
    return tokens

def infixToPostfix(s): # 중위표현 수식 -> 후위표현 수식 변경 작업
    re = ''
    stack = []
    for c in s:
        if type(c) is int: # 수식이 숫자이면 바로 re에 담음
            re += str(c)
        elif c not in '()+-*/': # 수식이 연산자가 아니면 re에 담음
            re += c
        elif c == "(": # 수식이 '('이면 stack에 넣음
            stack.append(c)
        elif stack and c == ")": # stack이 있고, ')'라면, stack 마지막이 '('아닐때까지 stack에서 꺼내서 re에 담음
            while stack[-1] != "(":
                re += stack.pop()
            stack.pop()
        elif stack and prec.get(c) <= prec.get(stack[-1]): # stack에 값이 있고, prec에 수식이 stack마지막 값보다 같거나 작다면
            re += stack.pop() # stack에서 꺼내서 re에 담은
            stack.append(c) # stack에 수식을 넣음
            if len(stack) == 2: # stack의 길이가 2라면, stack의 첫번째 값을 re에 담음
                re += stack.pop(0)
        else:
            stack.append(c) # 위에 해당하지 않은 수식은 stack에 담음

    while stack: # stack에 남아있는 수식을 re에 담음
        re += stack.pop()

    return re


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)

    return postfix

print(solution('2 + 3 * 4 / 3 - 6 / 3 * 3 + 8'))
