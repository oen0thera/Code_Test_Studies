from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


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
                if switch==True:
                    switch=False
                    tokenlist.append(expr[:i])
                    tokenlist.append(expr[i])
                    sp=i+1
                elif switch==False:
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
                result = number1 + number2
                valStack.push(result)

        elif postfixList[token] == '-':
            if valStack.size() >= 2:
                number2 = valStack.pop()
                number1 = valStack.pop()
                result = number1 - number2
                valStack.push(result)

    return valStack.pop()


class Button(QToolButton):

    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size




class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton=[] #making empty list of digitButton
        i=0 # initializing 'numbers' of digitButton
        while i<10: #through 0~9
            self.digitButton.append(Button(str(i))) #append Buttons to self.digitButton
            i+=1 #add 1 to i for while loop

        # . and = Buttons
        self.decButton = Button('.')
        self.eqButton = Button('=')

        # Operator Buttons
        self.mulButton = Button('*')
        self.divButton = Button('/')
        self.addButton = Button('+')
        self.subButton = Button('-')

        # Parentheses Buttons
        self.lparButton = Button('(')
        self.rparButton = Button(')')

        # Clear Button
        self.clearButton = Button('C')

        # Connection
        # Digit
        for dig in range(0,10): #connecting digitButtons to Button_pressed function
            self.digitButton[dig].clicked.connect(self.Button_pressed)
        # . and = Buttons
        self.decButton.clicked.connect(self.Button_pressed)
        self.eqButton.clicked.connect(self.Button_pressed)
        # Operator Buttons
        self.mulButton.clicked.connect(self.Button_pressed)
        self.divButton.clicked.connect(self.Button_pressed)
        self.addButton.clicked.connect(self.Button_pressed)
        self.subButton.clicked.connect(self.Button_pressed)
        # Parentheses Buttons
        self.lparButton.clicked.connect(self.Button_pressed)
        self.rparButton.clicked.connect(self.Button_pressed)
        # Clear Button
        self.clearButton.clicked.connect(self.Button_pressed)



        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        num=1 #numbers to add
        row=2 #row number of Grid(numLayout)
        col=0 #column number of Grid(numLayout)
        numLayout.addWidget(self.digitButton[0], 3, 0) #adding 0 separately since it doesn't fit in loop algorithm
        while num<10: #through 1~9
            numLayout.addWidget(self.digitButton[num], row, col) #add digitButton[num] for current column and row number
            if col==2: #if column reaches to 2
                row-=1 #substitute 1 from row
                col=0 #initialize column to 0
            else:
                col+=1 #if column didn't reach to 2, add 1 to column
            num+=1 #add 1 for the while loop

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)

        opLayout.addWidget(self.clearButton, 3, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")
    def Button_pressed(self):
        sender = self.sender() #call the pressed button
        if sender.text() in '0123456789': #if pressed button is digit
            if self.display.text()=='0': #if the display is 0
                self.display.setText(sender.text()) #initialize the display into pressed digitbutton
            else: #if the display is not 0
                self.display.insert(sender.text()) #insert the pressed button's digitnumber to display
        elif sender.text() in '+-*/().': #if pressed button is operator
            self.display.insert(sender.text()) #insert the preseed button's operator to display
        elif sender.text()=='C': #if pressed button is C
            self.display.clear() #clear the display
            self.display.setText('0') #initialize the display into '0'
        elif sender.text()=='=':
            Calc=Calculating() #create Calculating() class as Calc
            result = str(Calc.evaluate(self.display.text())) #evaluate the formula in display, change to string and name it as result
            self.display.clear() #clear the display
            self.display.setText(result) #initialize the display to evaluation result



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
