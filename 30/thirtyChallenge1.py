#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import re

class ThirtyChallengeOne(QtGui.QWidget):
    
    def __init__(self):
        super(ThirtyChallengeOne, self).__init__()
        
        # Instance variables.
        self.baseNumberLabel = None
        self.baseNumberComboBox = None
        self.exerciseLabels = []

        # Setup the GUI.
        self.initUI()
        
    def initUI(self):        
        # Create widgets.
        self.baseNumberLabel = QtGui.QLabel("Base number")
        self.baseNumberComboBox = QtGui.QComboBox()

        # Add numbers to the combo box.
        for i in range(0, 13):
            self.baseNumberComboBox.addItem(str(i))

        # Create and add exercise labels.
        for i in range(0, 13):
            self.exerciseLabels.append(QtGui.QLabel(""))

        # Set texts for the base number 0.
        self.setExerciseTexts(0)

        # LAYOUT FOR THE WIDGETS.

        # Set up layout to contain the widgets.
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # Add widgets to the layout.
        grid.addWidget(self.baseNumberLabel, 1, 0)
        grid.addWidget(self.baseNumberComboBox, 1, 1)
        for i in range(0, 13):
            grid.addWidget(self.exerciseLabels[i], i + 2, 0)

        # Create layout to take care of extra vertical space.
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addStretch(1)

        # A set layout of this widget.
        self.setLayout(vbox) 

        # Connect signals to slots.
        self.baseNumberComboBox.currentIndexChanged.connect(self.baseNumberComboBoxIndexChanged)
        # Position on screen and show.
        self.resize(400, 400)
        self.center()
        self.show()
 
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())       
        
    def baseNumberComboBoxIndexChanged(self, index):
        print("Index: %d" % index)
        print("Text: %s" % self.baseNumberComboBox.itemText(index))
        self.setExerciseTexts(self.baseNumberComboBox.itemText(index))
        self.repaint()

    def setExerciseTexts(self, baseNumberAsString):
        baseNumber = int(baseNumberAsString)
        for multiplier in range(0, 13):
            self.exerciseLabels[multiplier].setText(self.createExerciseText(baseNumber, multiplier))

    def createExerciseText(self, baseNumber, multiplier):
        return "%d x %d = %d"% (baseNumber, multiplier, baseNumber * multiplier)

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = ThirtyChallengeOne()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
