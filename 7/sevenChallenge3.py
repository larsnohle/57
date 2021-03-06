#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui


class SevenChallengeThree(QtGui.QWidget):
    
    def __init__(self):
        super(SevenChallengeThree, self).__init__()
        
        # Constants
        self.lengthInMeterMessage = "Length in meter"
        self.lengthInFeetMessage = "Length in feet"
        self.widthInMeterMessage = "Width in meter"
        self.widthInFeetMessage = "Width in feet"
        self.feetToMeterConversionFactor = 0.09290304

        # Instance variables.
        self.meterRadioButton = None
        self.feetRadioButton  = None

        self.unitLabel = None
        self.lengthLabel = None
        self.widthLabel = None
        self.lengthTextEdit = None
        self.widthTextEdit = None

        self.firstOutputLabel = None
        self.secondOutputLabel = None
        self.thirdOutputLabel = None
        self.fourthOutputLabel = None

        # Setup the GUI.
        self.initUI()
        
    def initUI(self):        
        # Create widgets.
        self.unitLabel = QtGui.QLabel("Unit")
        self.lengthLabel = QtGui.QLabel(self.lengthInMeterMessage)
        self.widthLabel = QtGui.QLabel(self.widthInMeterMessage)

        self.meterRadioButton  = QtGui.QRadioButton(self.tr("Meter"), self)
        self.feetRadioButton  = QtGui.QRadioButton(self.tr("Feet"), self)

        self.meterRadioButton.setChecked(True)

        buttonGroup =QtGui.QButtonGroup()
        buttonGroup.addButton(self.meterRadioButton)
        buttonGroup.addButton(self.feetRadioButton)

        self.lengthTextEdit = QtGui.QLineEdit()
        self.widthTextEdit = QtGui.QLineEdit()
        self.firstOutputLabel = QtGui.QLabel(self.createFirstOutputLine(None, None))
        self.secondOutputLabel = QtGui.QLabel()
        self.thirdOutputLabel = QtGui.QLabel(self.createThirdOutputLine(None, None))
        self.fourthOutputLabel = QtGui.QLabel(self.createFourthOutputLine(None, None))

        # Layout for the widgets.
        radioButtonHBox = QtGui.QHBoxLayout()
        radioButtonHBox.addWidget(self.meterRadioButton)
        radioButtonHBox.addWidget(self.feetRadioButton)
        radioButtonHBox.addStretch(1)

        # Set up layout to contain the widgets.
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # Add widgets to the layout.
        grid.addWidget(self.unitLabel, 1, 0)
        grid.addLayout(radioButtonHBox, 1, 1)
        grid.addWidget(self.lengthLabel, 2, 0)
        grid.addWidget(self.lengthTextEdit, 2, 1)
        grid.addWidget(self.widthLabel, 3, 0)
        grid.addWidget(self.widthTextEdit, 3, 1)
        grid.addWidget(self.firstOutputLabel, 4, 0, 1, 2)
        grid.addWidget(self.secondOutputLabel, 5, 0, 1, 2)
        grid.addWidget(self.thirdOutputLabel, 6, 0, 1, 2)
        grid.addWidget(self.fourthOutputLabel, 7, 0, 1, 2)

        # Create layout to take care of extra vertical space.
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addStretch(1)

        # A set layout of this widget.
        self.setLayout(vbox) 

        # Connect signals to slots.
        self.lengthTextEdit.textChanged.connect(self.oneOfTheNumberInputTextsChanged)
        self.widthTextEdit.textChanged.connect(self.oneOfTheNumberInputTextsChanged)
        self.meterRadioButton.toggled.connect(self.unitButtonToggled)
        self.feetRadioButton.toggled.connect(self.unitButtonToggled)

        # Position on screen and show.
        self.resize(400, 100)
        self.center()
        self.show()
 
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())       
        
    def unitButtonToggled(self, checked):
        if checked == True and self.meterRadioButton.isChecked():
            self.lengthLabel.setText(self.lengthInMeterMessage)
            self.widthLabel.setText(self.widthInMeterMessage)
            self.updateOutputFields()
        elif checked == True and self.feetRadioButton.isChecked():
            self.lengthLabel.setText(self.lengthInFeetMessage)
            self.widthLabel.setText(self.widthInFeetMessage)
            self.updateOutputFields()

    def oneOfTheNumberInputTextsChanged(self):
        self.updateOutputFields()

    def updateOutputFields(self):
        (firstNumber, secondNumber) = self.getNumbers()
        if firstNumber != None and secondNumber != None:
            self.firstOutputLabel.setText(self.createFirstOutputLine(firstNumber, secondNumber))
            self.secondOutputLabel.setText(self.createSecondOutputLine())
            self.thirdOutputLabel.setText(self.createThirdOutputLine(firstNumber, secondNumber))
            self.fourthOutputLabel.setText(self.createFourthOutputLine(firstNumber, secondNumber))
        else:
            self.clearTextEdits()

    def getNumbers(self):
        firstNumberAsString = self.lengthTextEdit.text()
        secondNumberAsString = self.widthTextEdit.text()        
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

    def createFirstOutputLine(self, length, width):
        if length != None and width != None:
            unit = self.getSelectedUnit()
            return "You entered dimensions of %d %s by %d %s." % (length, unit, width, unit)

    def createSecondOutputLine(self):
        return "The area is"

    def createThirdOutputLine(self, length, width):
        if length != None and width != None:
            return "%.2f square meters" % self.getSelectedAreaInMeters(length, width)

    def createFourthOutputLine(self, length, width):
        if length != None and width != None:
            return "%.2f square feet" % self.getSelectedAreaInFeet(length, width)

    def getSelectedUnit(self):
        if self.meterRadioButton.isChecked():
            return "meter"
        elif self.feetRadioButton.isChecked():
            return "feet"

    def createTextToOutput(self, firstNumber, secondNumber, operator, resultMaker):
        if firstNumber != None and secondNumber != None:
            result = resultMaker(firstNumber, secondNumber)
            return str(firstNumber) + operator + str(secondNumber) + " = " + str(result)
        else:
            return ""

    def clearTextEdits(self):
        self.firstOutputLabel.setText("")
        self.secondOutputLabel.setText("")
        self.thirdOutputLabel.setText("")
        self.fourthOutputLabel.setText("")

    def getSelectedAreaInMeters(self, length, width):
        if length != None and width != None:
            if self.meterRadioButton.isChecked():
                return length * width
            else:
                return length * width * self.feetToMeterConversionFactor

    def getSelectedAreaInFeet(self, length, width):
        if length != None and width != None:
            if self.meterRadioButton.isChecked():
                return length * width / self.feetToMeterConversionFactor
            else:
                return length * width

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = SevenChallengeThree()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
