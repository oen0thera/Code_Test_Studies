'''
Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.
'''
class Calculating: #Used Calculating class from previous calculator project

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

    def evaluate(self, string):
        tokenlist = splitTokens(string)
        postfix = infixToPostfix(tokenlist)
        val = postfixEval(postfix)
        return val


def splitTokens(expr): #spliting formula to float and operator
        tokenlist = []
        sp = 0
        switch = False
        i=0
        while i<len(expr):
            if i==0 and expr[i]=='-':
                switch=True
            elif expr[i] in '0123456789.':
                pass
            else:
                print(expr[i],expr[sp])
                if switch==True:
                    switch=False
                    tokenlist.append(expr[:i])
                    tokenlist.append(expr[i])
                    sp=i+1
                elif switch==False:
                    print('switch 0')
                    tokenlist.append(expr[sp:i])
                    tokenlist.append(expr[i])
                    sp = i + 1
            i+=1
        tokenlist.append(expr[sp:len(expr)])

        remover = []
        for i in range(0, len(tokenlist)):
            if tokenlist[i] == '':
                remover.append(i)
            elif tokenlist[i] in '+-/*()':
                pass
            else:
                tokenlist[i] = float(tokenlist[i])
        remover.reverse()
        for r in remover:
            del tokenlist[r]
        print(tokenlist)
        return tokenlist


def infixToPostfix(tokenlist): #changing infix formula to postfix formula for stack process
        prec = {
            '*': 3,
            '/': 3,
            '+': 2,
            '-': 2,
            '(': 1,
        }

        opStack = Calculating()
        postfixList = []
        if len(tokenlist) == 1 and type(tokenlist[0]) is float:
            return tokenlist
        for token in tokenlist:
            if type(token) is float:
                postfixList.append(token)
            if token == '(':
                opStack.push(token)
            if token == ')':
                while not opStack.isEmpty():
                    tide = opStack.pop()
                    if tide != '(':
                        postfixList.append(tide)
                    if tide == '(':
                        break
            else:
                if token in prec:
                    if prec[token] >= 2 and opStack.isEmpty() == False:
                        peek = opStack.peek()
                        if prec[peek] == 3 and prec[peek] == prec[token]:
                            opStack.push(token)
                        elif prec[peek] < prec[token]:
                            opStack.push(token)
                        elif prec[peek] >= prec[token]:
                            while not opStack.isEmpty():
                                tide = opStack.pop()
                                if tide != '(':
                                    postfixList.append(tide)

                                if tide == '(':
                                    break
                            opStack.push(token)
                    if prec[token] >= 2 and opStack.isEmpty() == True:
                        opStack.push(token)
        while not opStack.isEmpty():
            tide = opStack.pop()
            if tide != '(':
                postfixList.append(tide)
        return postfixList


def postfixEval(postfixList): #evaluate the formula by using Stack which has postfix formula
    valStack = Calculating()
    skipper = False
    if len(postfixList) == 1 and type(postfixList[0]) is float:
        return postfixList[0]
    for token in range(0, len(postfixList)):
        if type(postfixList[token]) is float:
            valStack.push(postfixList[token])
        elif postfixList[token] == '*':
            if valStack.size() >= 2:
                if token != len(postfixList) - 1:
                    if postfixList[token + 1] != '/':
                        number2 = valStack.pop()
                        number1 = valStack.pop()
                        result = number1 * number2
                        valStack.push(result)


                    else:
                        number3 = valStack.pop()
                        number2 = valStack.pop()
                        number1 = valStack.pop()
                        result = number1 * number3 / number2
                        valStack.push(result)

                        skipper = True
                else:
                    number2 = valStack.pop()
                    number1 = valStack.pop()
                    result = number1 * number2
                    valStack.push(result)

        elif postfixList[token] == '/':
            if valStack.size() >= 2 and skipper == False:
                number2 = valStack.pop()
                number1 = valStack.pop()
                result = number1 / number2
                valStack.push(result)

            else:
                skipper = False
        elif postfixList[token] == '+':
            if valStack.size() >= 2:
                number2 = valStack.pop()
                number1 = valStack.pop()
                print(number1, number2)
                result = number1 + number2
                valStack.push(result)
                print(result)

        elif postfixList[token] == '-':
            if valStack.size() >= 2:
                number2 = valStack.pop()
                number1 = valStack.pop()
                result = number1 - number2
                valStack.push(result)
                print(result)

    return valStack.pop()

#234*+3/63/-3*8+
print(Calculating().evaluate("-1+21"))
