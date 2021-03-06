#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import math
from PyQt4 import QtGui


class ThirteenChallengeThree(QtGui.QWidget):
    
    def __init__(self):
        super(ThirteenChallengeThree, self).__init__()
        
        # Constants
        self.principalAmountMessage = "Principal amount"
        self.rateMessage = "Rate"
        self.numberOfYearsMessage = "Number of years"
        self.numberOfCompoundsPerYearMessage = "Number of componds per year"

        # Instance variables.
        self.principalAmountLabel = None
        self.rateLabel = None
        self.numberOfYearsLabel = None
        self.numberOfCompondsPerYearLabel = None
        self.firstOutputLabel = None

        self.principalAmountEdit = None
        self.rateEdit = None
        self.numberOfYearsEdit = None
        self.numberOfCompondsPerYearEdit = None

        # Setup the GUI.
        self.initUI()
        
    def initUI(self):        
        # Create widgets.
        self.principalAmountLabel = QtGui.QLabel(self.principalAmountMessage)
        self.rateLabel = QtGui.QLabel(self.rateMessage)
        self.numberOfYearsLabel = QtGui.QLabel(self.numberOfYearsMessage)
        self.numberOfCompondsPerYearLabel = QtGui.QLabel(self.numberOfCompoundsPerYearMessage)
        self.firstOutputLabel = QtGui.QLabel("")

        self.principalAmountEdit = QtGui.QLineEdit()
        self.rateEdit = QtGui.QLineEdit()
        self.numberOfYearsEdit = QtGui.QLineEdit()
        self.numberOfCompondsPerYearEdit = QtGui.QLineEdit()

        # Set up layout to contain the widgets.
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # Add widgets to the layout.
        grid.addWidget(self.principalAmountLabel, 1, 0)
        grid.addWidget(self.principalAmountEdit, 1, 1)
        grid.addWidget(self.rateLabel, 2, 0)
        grid.addWidget(self.rateEdit, 2, 1)
        grid.addWidget(self.numberOfYearsLabel, 3, 0)
        grid.addWidget(self.numberOfYearsEdit, 3, 1)
        grid.addWidget(self.numberOfCompondsPerYearLabel, 4, 0)
        grid.addWidget(self.numberOfCompondsPerYearEdit, 4, 1)
        grid.addWidget(self.firstOutputLabel, 5, 0, 1, 2)

        # Create layout to take care of extra vertical space.
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addStretch(1)

        # A set layout of this widget.
        self.setLayout(vbox) 

        # Connect signals to slots.
        self.principalAmountEdit.textChanged.connect(self.oneOfTheNumberInputTextsChanged)
        self.rateEdit.textChanged.connect(self.oneOfTheNumberInputTextsChanged)
        self.numberOfYearsEdit.textChanged.connect(self.oneOfTheNumberInputTextsChanged)
        self.numberOfCompondsPerYearEdit.textChanged.connect(self.oneOfTheNumberInputTextsChanged)

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
        (principalAmount, rate, numberOfYears, numberOfCompondsPerYear) = self.getNumbers()
        if principalAmount != None and rate != None and numberOfYears != None and numberOfCompondsPerYear != None:
            self.firstOutputLabel.setText(self.createFirstOutputLine(principalAmount, rate, numberOfYears, numberOfCompondsPerYear))
        else:
            self.clearTextEdits()

    def getNumbers(self):
        principalAmountAsString = self.principalAmountEdit.text()
        rateAsString = self.rateEdit.text()        
        numberOfYearsAsString = self.numberOfYearsEdit.text()        
        numberOfCompondsPerYearString = self.numberOfCompondsPerYearEdit.text()

        principalAmount = self.parseAsInteger(principalAmountAsString)
        rate = self.parseAsFloat(rateAsString)
        numberOfYears = self.parseAsInteger(numberOfYearsAsString)
        numberOfCompondsPerYear = self.parseAsInteger(numberOfCompondsPerYearString)

        return (principalAmount, rate, numberOfYears, numberOfCompondsPerYear)

    def parseAsInteger(self, numberAsString):
        i = None
        try:
            i = int(numberAsString)
        except ValueError:
            pass # We just return None if we could not parse the string as an int.

        return i

    def parseAsFloat(self, numberAsString):
        i = None
        try:
            i = float(numberAsString)
        except ValueError:
            pass # We just return None if we could not parse the string as an int.

        return i

    def createFirstOutputLine(self, principalAmount, rateInPercent, numberOfYears, numberOfCompondsPerYear):
        rate = rateInPercent / 100
        finalAmount = principalAmount * (1 + rate / numberOfCompondsPerYear) ** (numberOfYears * numberOfCompondsPerYear)
        numberOfWholeDollars = math.trunc(finalAmount)
        numberOfPennies = math.ceil((finalAmount - numberOfWholeDollars) * 100)    
        adjustedAmount = numberOfWholeDollars + numberOfPennies / 100

        return "After %d years at %s percent, the investment will be worth $%.2f." % (numberOfYears, str(rateInPercent), adjustedAmount)

    def createSecondOutputLine(self):
        return "The area is"

    def clearTextEdits(self):
        self.firstOutputLabel.setText("")

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = ThirteenChallengeThree()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
