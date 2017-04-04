#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random

from PyQt4 import QtGui
from PyQt4 import QtCore

########################## MAIN CLASS ##########################
        
class ThirtyThreeChallenge1(QtGui.QWidget):    
    def __init__(self):
        super(ThirtyThreeChallenge1, self).__init__()

        # CONSTANTS
        self.answers = ["Yes", "No", "Maybe", "Ask again later."]
        
        # Instance variables.
        self.questionLabel = None
        self.questionTextEdit = None
        self.questionButton = None
        self.answerLabel = None
        self.answerValueLabel = None
        
        self.setWindowTitle('Thirty three challenge 1')
        
        # Setup the GUI.
        self.initUI()

    def initUI(self):        
        # Create widgets.
        self.questionLabel = QtGui.QLabel("Question")
        self.questionEdit = QtGui.QLineEdit()
        self.questionButton = QtGui.QPushButton("Answer")
        self.answerLabel = QtGui.QLabel("Answer")
        self.answerValueLabel = QtGui.QLabel("")
               
        # LAYOUT FOR THE WIDGETS.

        # Set up layout to contain the widgets.
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # Add widgets to the layout.
        grid.addWidget(self.questionLabel, 0, 0)
        grid.addWidget(self.questionEdit, 0, 1)
        grid.addWidget(self.questionButton, 0, 2)
        grid.addWidget(self.answerLabel, 1, 0)
        grid.addWidget(self.answerValueLabel, 1, 1)        

        grid.setColumnStretch(1, 1)
        
        # Create layout to take care of extra vertical space.
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addStretch(1)
        
        # A set layout of this widget.
        self.setLayout(vbox) 

        # Connect signals to slots.
        self.questionButton.clicked.connect(self.questionButtonClicked)

        # Position on screen and show.
        self.resize(400, 100)
        self.center()
        self.show()
 
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())       

    def questionButtonClicked(self, index):
        answer_index = random.randint(0, len(self.answers) - 1)
        self.answerValueLabel.setText(self.answers[answer_index])
            
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = ThirtyThreeChallenge1()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
