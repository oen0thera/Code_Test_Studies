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


def splitTokens(expr):
    tokenlist = []
    val = 0
    valProcessing = False
    for c in expr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokenlist.append(val)
                val = 0
            valProcessing = False
            tokenlist.append(c)
    if valProcessing:
        tokenlist.append(val)
    return tokenlist


def infixToPostfix(tokenlist):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for token in tokenlist:
        if type(token) is int:
            postfixList.append(token)
        if token == '(':
            opStack.push(token)
        if token == ')':
            while not opStack.isEmpty():
                tide=opStack.pop()
                if tide!='(':
                    postfixList.append(tide)
                if tide=='(':
                    break
        else:
            if token in prec:
                if prec[token]>=2 and opStack.isEmpty()==False:
                    peek=opStack.peek()
                    if prec[peek]<prec[token]:
                        opStack.push(token)
                    elif prec[peek]>=prec[token]:
                        while not opStack.isEmpty():
                            tide=opStack.pop()
                            if tide !='(':
                                postfixList.append(tide)
                                print(postfixList)
                            if tide =='(':
                                break
                if prec[token]>=2 and opStack.isEmpty()==True:
                    opStack.push(token)
    while not opStack.isEmpty():
            tide=opStack.pop()
            if tide !='(':
                postfixList.append(tide)
    return postfixList


def postfixEval(postfixList):
    valStack=ArrayStack()
    for token in postfixList:
        if type(token) is int:
            valStack.push(token)
        elif token == '*':
            if valStack.size()>=2:
                number2=valStack.pop()
                number1=valStack.pop()
                result=number1*number2
                valStack.push(result)
        elif token == '/':
            if valStack.size()>=2:
                number2=valStack.pop()
                number1=valStack.pop()
                result=number1/number2
                valStack.push(result)
        elif token == '+':
            if valStack.size()>=2:
                number2=valStack.pop()
                number1=valStack.pop()
                result=number1+number2
                valStack.push(result)
        elif token == '-':
            if valStack.size()>=2:
                number2=valStack.pop()
                number1=valStack.pop()
                result=number1-number2
                valStack.push(result)
    return valStack.pop()

def solution(expr):
    tokenlist = splitTokens(expr)
    postfix = infixToPostfix(tokenlist)
    val = postfixEval(postfix)
    print(val)
    return val


solution('2 + 3 * 4 / 3 - 6 / 3 * 3 + 8')
