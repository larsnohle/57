#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui


class FiveChallengeFour(QtGui.QWidget):
    
    def __init__(self):
        super(FiveChallengeFour, self).__init__()

        self.firstNumberLabel = None
        self.secondNumberLabel = None
        self.firstNumberTextEdit = None
        self.secondNumberTextEdit = None
        self.additionEquationLabel = None
        self.subtractionEquationLabel = None
        self.multiplicationEquationLabel = None
        self.divisionEquationLabel = None

        self.initUI()
        
    def initUI(self):        
        # Create widgets.
        self.firstNumberLabel = QtGui.QLabel('What is the first number?')
        self.secondNumberLabel = QtGui.QLabel('What is the second number?')
        self.firstNumberTextEdit = QtGui.QLineEdit()
        self.secondNumberTextEdit = QtGui.QLineEdit()
        self.additionEquationLabel = QtGui.QLabel(self.createAdditionTextToOutput(None, None))
        self.subtractionEquationLabel = QtGui.QLabel(self.createSubtractionTextToOutput(None, None))
        self.multiplicationEquationLabel = QtGui.QLabel(self.createMultiplicationTextToOutput(None, None))
        self.divisionEquationLabel = QtGui.QLabel(self.createDivisionTextToOutput(None, None))

        # Set up layout to contain the widgets.
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # Add widgets to the layout.
        grid.addWidget(self.firstNumberLabel, 1, 0)
        grid.addWidget(self.firstNumberTextEdit, 1, 1)
        grid.addWidget(self.secondNumberLabel, 2, 0)
        grid.addWidget(self.secondNumberTextEdit, 2, 1)
        grid.addWidget(self.additionEquationLabel, 3, 0, 1, 2)
        grid.addWidget(self.subtractionEquationLabel, 4, 0, 1, 2)
        grid.addWidget(self.multiplicationEquationLabel, 5, 0, 1, 2)
        grid.addWidget(self.divisionEquationLabel, 6, 0, 1, 2)

        # Create layout to take care of extra vertical space.
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addStretch(1)

        # A set layout of this widget.
        self.setLayout(vbox) 

        # Connect signals to slots.
        self.firstNumberTextEdit.textChanged.connect(self.oneOfTheNumberInputTextsChanged)
        self.secondNumberTextEdit.textChanged.connect(self.oneOfTheNumberInputTextsChanged)

        # Position on screen and show.
        self.resize(400, 100)
        self.center()
        self.show()
 
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())       
        
    def oneOfTheNumberInputTextsChanged(self):
        (firstNumber, secondNumber) = self.getNumbers()
        if firstNumber != None and secondNumber != None:
            self.additionEquationLabel.setText(self.createAdditionTextToOutput(firstNumber, secondNumber))
            self.subtractionEquationLabel.setText(self.createSubtractionTextToOutput(firstNumber, secondNumber))
            self.multiplicationEquationLabel.setText(self.createMultiplicationTextToOutput(firstNumber, secondNumber))
            self.divisionEquationLabel.setText(self.createDivisionTextToOutput(firstNumber, secondNumber))
        else:
            self.clearTextEdits()

    def getNumbers(self):
        firstNumberAsString = self.firstNumberTextEdit.text()
        secondNumberAsString = self.secondNumberTextEdit.text()        
        firstNumber = self.parseAsInteger(firstNumberAsString)
        secondNumber = self.parseAsInteger(secondNumberAsString)
        return (firstNumber, secondNumber)

    def parseAsInteger(self, numberAsString):
        i = None
        try:
            i = int(numberAsString)
        except ValueError:
            pass # We just return None if we could not parse the string as an int.

        return i

    def createAdditionTextToOutput(self, firstNumber, secondNumber):
        return self.createTextToOutput(firstNumber, secondNumber, "+", lambda x, y: x + y)

    def createSubtractionTextToOutput(self, firstNumber, secondNumber):
        return self.createTextToOutput(firstNumber, secondNumber, "-", lambda x, y: x - y)

    def createMultiplicationTextToOutput(self, firstNumber, secondNumber):
        return self.createTextToOutput(firstNumber, secondNumber, "*", lambda x, y: x * y)

    def createDivisionTextToOutput(self, firstNumber, secondNumber):
        return self.createTextToOutput(firstNumber, secondNumber, "/", lambda x, y: x / y)

    def createTextToOutput(self, firstNumber, secondNumber, operator, resultMaker):
        if firstNumber != None and secondNumber != None:
            result = resultMaker(firstNumber, secondNumber)
            return str(firstNumber) + operator + str(secondNumber) + " = " + str(result)
        else:
            return ""

    def clearTextEdits(self):
        self.additionEquationLabel.setText("")
        self.subtractionEquationLabel.setText("")
        self.multiplicationEquationLabel.setText("")
        self.divisionEquationLabel.setText("")

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = FiveChallengeFour()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
