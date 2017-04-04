#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class NineteenChallengeThree(QtGui.QWidget):
    
    def __init__(self):
        super(NineteenChallengeThree, self).__init__()
        
        # Constants
        self.temperatureInCelsiusMessage = "Temperature in Celsius"
        self.temperatureInFahrenheitMessage = "Temperature in Fahrenheit"
        self.celsius = "Celsius"
        self.fahrenheit = "Fahrenheit"

        # Instance variables.
        self.celsiusRadioButton = None
        self.fahrenheitRadioButton  = None

        self.weightLabel = None
        self.heightLabel = None
        self.weightValueLabel = None
        self.heightValueLabel = None

        self.weightSlider = None
        self.heightSlider = None

        self.firstOutputLabel = None

        self.labelPalette = None

        # Setup the GUI.
        self.initUI()
        
    def initUI(self):        
        # Create widgets.
        self.weightLabel = QtGui.QLabel("Weight")
        self.heightLabel = QtGui.QLabel("Height")
        self.weightValueLabel = QtGui.QLabel(self.assembleWeightString(0))
        self.heightValueLabel = QtGui.QLabel(self.assembleHeightString(0))

        self.weightSlider = QtGui.QSlider()
        self.weightSlider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
#        self.weightSlider.setGeometry(10, 10, 200, 30)
        self.weightSlider.setFocusPolicy(QtCore.Qt.NoFocus)

        self.heightSlider = QtGui.QSlider()
        self.heightSlider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.weightSlider.setFocusPolicy(QtCore.Qt.NoFocus)

        self.firstOutputLabel = QtGui.QLabel("")

        # LAYOUT FOR THE WIDGETS.

        # Set up layout to contain the widgets.
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # Add widgets to the layout.
        grid.addWidget(self.weightLabel, 1, 0)
        grid.addWidget(self.weightSlider, 1, 1)
        grid.addWidget(self.weightValueLabel, 1, 2)

        grid.addWidget(self.heightLabel, 2, 0)
        grid.addWidget(self.heightSlider, 2, 1)
        grid.addWidget(self.heightValueLabel, 2, 2)
        grid.addWidget(self.firstOutputLabel, 4, 0, 1, 2)

        # Create layout to take care of extra vertical space.
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addStretch(1)

        # A set layout of this widget.
        self.setLayout(vbox) 

        # Set up palette for the output text field.
        self.labelPalette = QtGui.QPalette()
        self.labelPalette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.black)
        self.firstOutputLabel.setPalette(self.labelPalette)

        # Connect signals to slots.
        self.weightSlider.valueChanged.connect(self.weightChanged)
        self.heightSlider.valueChanged.connect(self.heightChanged)

        # Position on screen and show.
        self.resize(400, 100)
        self.center()
        self.show()
 
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())       
        
    def weightChanged(self):
        weight = self.weightSlider.value()
        self.weightValueLabel.setText(self.assembleWeightString(weight))
        self.calculateAndSetBmiText()

    def assembleWeightString(self, weight):
        return str(weight) + " kg"

    def heightChanged(self):
        height = self.heightSlider.value() * 2
        self.heightValueLabel.setText(self.assembleHeightString(height))
        self.calculateAndSetBmiText()

    def assembleHeightString(self, height):
        return str(height) + " cm"

    def calculateBmiUsingMetricUnits(self, weight, height):
        if height <= 0:
            return 0

        return weight / (height * height)

    def calculateAndSetBmiText(self):
        weight = self.weightSlider.value()
        height = float(self.heightSlider.value() * 2 / 100) # Should be in kg.

        bmi = self.calculateBmiUsingMetricUnits(weight, height)

#        print("Weight: %.2f" % weight)
#        print("Height: %.2f" % height)
#        print("BMI: %.2f" % bmi)

        bmiString = ""
        if (bmi < 18.5):
            bmiString = "You are underweight. You should see your doctor."
            self.labelPalette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.blue)
        elif (bmi > 28.5):
            bmiString = "You are overweight. You should see your doctor."
            self.labelPalette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
        else:            
            bmiString = "You are within the ideal weight range."
            self.labelPalette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.black)

        self.firstOutputLabel.setPalette(self.labelPalette)
        self.firstOutputLabel.setText(bmiString)

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = NineteenChallengeThree()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
