#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui


class TwoChallengeTwo(QtGui.QWidget):
    
    def __init__(self):
        super(TwoChallengeTwo, self).__init__()

        self.inputTextEdit = None
        self.letterCounterLabel = None

        self.initUI()
        
    def createTextToOutput(self, inputtedText):
        numberOfLetters = len(inputtedText)
        return inputtedText + " has " + str(numberOfLetters) + " characters."

    def initUI(self):        
        # Create widgets.
        inputTextLabel = QtGui.QLabel('Var vänlig skriv in en text')
        self.inputTextEdit = QtGui.QLineEdit()
        self.letterCounterLabel = QtGui.QLabel(self.createTextToOutput(''))

        # Set up layout to contain the widgets.
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # Add widgets to the layout.
        grid.addWidget(inputTextLabel, 1, 0)
        grid.addWidget(self.inputTextEdit, 1, 1)
        grid.addWidget(self.letterCounterLabel, 2, 0, 1, 2)

        # Create layout to take care of extra vertical space.
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addStretch(1)

        # A set layout of this widget.
        self.setLayout(vbox) 

        # Connect signals to slots.
        self.inputTextEdit.textChanged.connect(self.inputTextChanged)

        # Position on screen and show.
        self.resize(400, 100)
        self.center()
        self.show()
 
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())       
        
    def inputTextChanged(self):
        inputtedText = self.inputTextEdit.text()
        self.letterCounterLabel.setText(self.createTextToOutput(inputtedText))

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = TwoChallengeTwo()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
