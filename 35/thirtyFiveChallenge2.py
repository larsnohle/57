#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random
import sched
import time
from  threading import Timer


from PyQt4 import QtGui
from PyQt4 import QtCore

########################## MAIN CLASS ##########################
        
class ThirtyFiveChallenge2(QtGui.QWidget):    
    def __init__(self):
        super(ThirtyFiveChallenge2, self).__init__()

        # CONSTANTS
        self.FILENAME = "contestants.txt"
        self.NUMBER_OF_MIXES = 5

        # Instance variables.
        self.timer = None
        self.performedNumberOfMixes  = 0
        self.contestants = None
        self.contestants_labels = list()
        self.contestantsHeadingLabel = None
        self.winnerMessageLabel = None
        self.winnerValueLabel = None

        self.setWindowTitle('Thirty three challenge 1')
        
        # Setup the GUI.
        self.initUI()

        self.startTimer()
        
    def initUI(self):
        self.contestants = self.read_contestants()
        
        # Create widgets.
        self.contestantsHeadingLabel = QtGui.QLabel("The contestants are:")
        self.winnerMessageLabel = QtGui.QLabel("The winner is: ")
        self.winnerValueLabel = QtGui.QLabel("")

        for contestant in self.contestants:
            contestants_label = QtGui.QLabel(contestant)
            self.contestants_labels.append(contestants_label)

        # Color for winner label.
        labelPalette = QtGui.QPalette()
        labelPalette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.blue)
        self.winnerValueLabel.setPalette(labelPalette)
            
        # LAYOUT FOR THE WIDGETS.

        # Set up layout to contain the widgets.
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # Add widgets to the layout.
        grid.addWidget(self.contestantsHeadingLabel, 0, 0)

        label_in_layout_index = 1
        for contestants_label in self.contestants_labels:
            grid.addWidget(contestants_label, label_in_layout_index, 1)
            label_in_layout_index += 1
        
        grid.addWidget(self.winnerMessageLabel, label_in_layout_index, 0)
        grid.addWidget(self.winnerValueLabel, label_in_layout_index, 1)        

        #grid.setColumnStretch(1, 1)
        
        # Create layout to take care of extra vertical space.
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addStretch(1)
        
        # A set layout of this widget.
        self.setLayout(vbox) 

        # Position on screen and show.
        self.resize(400, 100)
        self.center()
        self.show()
 
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())       

    def read_contestants(self):
        f = open(self.FILENAME, 'r')
        contestants = list()
        for contestant in f:
            contestants.append(contestant.strip())

        return contestants

    def startTimer(self):
        self.timer = Timer(2.0, self.mixContestants)
        self.timer.start()

    def mixContestants(self):
        self.performedNumberOfMixes += 1
        copyOfContestants = list(self.contestants)

        for contestants_label in self.contestants_labels:
            index = random.randint(0, len(copyOfContestants) - 1)
            contestant = copyOfContestants.pop(index)
            contestants_label.setText(contestant)

        if self.performedNumberOfMixes < self.NUMBER_OF_MIXES:
            self.startTimer()
        else:
            self.pickWinner()

    def pickWinner(self):
        winnerIndex = random.randint(0, len(self.contestants) - 1)
        winner = self.contestants.pop(winnerIndex)
        self.winnerValueLabel.setText(winner);            
                    
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = ThirtyFiveChallenge2()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
