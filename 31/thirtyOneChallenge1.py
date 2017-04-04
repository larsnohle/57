#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class ThirtyOneChallenge1(QtGui.QWidget):
    
    def __init__(self):
        super(ThirtyOneChallenge1, self).__init__()
        
        # Instance variables.
        self.ageLabel = None
        self.ageEdit = None

        self.restingHeardRateLabel = None
        self.restingHeardRateEdit = None
        
        self.intensityLabel = None
        self.intensityValueLabel = None
        self.intensitySlider = None

        self.heartRateLabel = None
        self.heartRateOutputLabel = None

        # Setup the GUI.
        self.initUI()
        
    def initUI(self):        
        # Create widgets.
        self.ageLabel = QtGui.QLabel("Age")
        self.ageEdit = QtGui.QLineEdit()

        self.restingHeardRateLabel = QtGui.QLabel("Resting heart rate")
        self.restingHeardRateEdit = QtGui.QLineEdit()

        self.intensityLabel = QtGui.QLabel("Intensity")
#        self.intensityValueLabel = QtGui.QLabel(self.assembleIntensityValueString(0))

        self.intensitySlider = QtGui.QSlider()
        self.intensitySlider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.intensitySlider.setFocusPolicy(QtCore.Qt.NoFocus)

        self.heartRateLabel = QtGui.QLabel("Target heart rate")        
        self.heartRateOutputLabel = QtGui.QLabel("")        

        # LAYOUT FOR THE WIDGETS.

        # Set up layout to contain the widgets.
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # Add widgets to the layout.
        grid.addWidget(self.ageLabel, 1, 0)
        grid.addWidget(self.ageEdit, 1, 1)
        
        grid.addWidget(self.restingHeardRateLabel, 2, 0)
        grid.addWidget(self.restingHeardRateEdit, 2, 1)
        
        grid.addWidget(self.intensityLabel, 3, 0)
        grid.addWidget(self.intensitySlider, 3, 1)

        grid.addWidget(self.heartRateLabel, 4, 0)
        grid.addWidget(self.heartRateOutputLabel, 4, 1, 1, 2)

        # Create layout to take care of extra vertical space.
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addStretch(1)

        # A set layout of this widget.
        self.setLayout(vbox) 

        # Set up palette for the output text field.
        self.labelPalette = QtGui.QPalette()
        self.labelPalette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.black)
        self.heartRateOutputLabel.setPalette(self.labelPalette)

        # Connect signals to slots.
        self.intensitySlider.valueChanged.connect(self.intensityChanged)

        # Position on screen and show.
        self.resize(400, 100)
        self.center()
        self.show()
 
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())       


    def convertToNumber(self, s):
        i = None
        try:
            i = int(s)
        except ValueError:
            pass

        return i
    
    def intensityChanged(self):
        intensity = self.intensitySlider.value()
        ageAsString = self.ageEdit.text()

        age = self.convertToNumber(ageAsString)
        restingHeardRate = self.convertToNumber(self.restingHeardRateEdit.text())


        if age != None and restingHeardRate != None:
            targetHeartRate = (((220 - age) - restingHeardRate) * intensity / 100) + restingHeardRate
            self.heartRateOutputLabel.setText("%d" % targetHeartRate)
        else:
            self.heartRateOutputLabel.setText("")
            
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = ThirtyOneChallenge1()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
