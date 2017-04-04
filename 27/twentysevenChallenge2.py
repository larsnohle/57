#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import re

class TwentySevenChallengeTwo(QtGui.QWidget):
    
    def __init__(self):
        super(TwentySevenChallengeTwo, self).__init__()
        
        # Constants
        self.firstNameRegExp = re.compile("[a-zåäöA-ZÅÄÖ][a-zåäöA-ZÅÄÖ]+")
        self.lastNameRegExp = re.compile("[a-zåäöA-ZÅÄÖ][a-zåäöA-ZÅÄÖ]+")
        self.employIdRegExp = re.compile("[a-zåäöA-ZÅÄÖ]{2}-\d\d\d\d$")
        self.zipCodeRegExp = re.compile("^\d+$")

        self.MIN_FIRST_NAME_LEN = 2
        self.MIN_LAST_NAME_LEN = 2

        # Instance variables.
        self.firstNameLabel = None
        self.firstNameEdit = None
        self.lastNameLabel = None
        self.lastNameEdit = None

        self.zipCodeLabel = None
        self.zipCodeEdit = None

        self.employeeIdLabel = None
        self.employeeIdEdit = None

        self.firstNameValidationMessageLabel = None
        self.lastNameValidationMessageLabel = None
        self.zipCodeValidationMessageLabel = None
        self.employeeIdValidationMessageLabel = None

        self.labelPalette = None

        # Setup the GUI.
        self.initUI()
        
    def initUI(self):        
        # Create widgets.
        self.firstNameLabel = QtGui.QLabel("First name")
        self.firstNameEdit = QtGui.QLineEdit()
        self.lastNameLabel = QtGui.QLabel("Last name")
        self.lastNameEdit = QtGui.QLineEdit()
        self.zipCodeLabel = QtGui.QLabel("ZIP code")
        self.zipCodeEdit = QtGui.QLineEdit()
        self.employeeIdLabel = QtGui.QLabel("Employee ID")
        self.employeeIdEdit = QtGui.QLineEdit()

        self.firstNameValidationMessageLabel = QtGui.QLabel("")
        self.lastNameValidationMessageLabel = QtGui.QLabel("")
        self.zipCodeValidationMessageLabel = QtGui.QLabel("")
        self.employeeIdValidationMessageLabel = QtGui.QLabel("")

        # LAYOUT FOR THE WIDGETS.

        # Set up layout to contain the widgets.
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # Add widgets to the layout.
        grid.addWidget(self.firstNameLabel, 1, 0)
        grid.addWidget(self.firstNameEdit, 1, 1)

        grid.addWidget(self.firstNameValidationMessageLabel, 2, 1)

        grid.addWidget(self.lastNameLabel, 3, 0)
        grid.addWidget(self.lastNameEdit,3, 1)

        grid.addWidget(self.lastNameValidationMessageLabel, 4, 1)

        grid.addWidget(self.zipCodeLabel, 5, 0)
        grid.addWidget(self.zipCodeEdit, 5, 1)

        grid.addWidget(self.zipCodeValidationMessageLabel, 6, 1)

        grid.addWidget(self.employeeIdLabel, 7, 0)
        grid.addWidget(self.employeeIdEdit, 7, 1)

        grid.addWidget(self.employeeIdValidationMessageLabel, 8, 1)

        # Create layout to take care of extra vertical space.
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addStretch(1)

        # A set layout of this widget.
        self.setLayout(vbox) 

        # Set up palette for the output text field.
        self.labelPalette = QtGui.QPalette()
        self.labelPalette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
        self.firstNameValidationMessageLabel.setPalette(self.labelPalette)
        self.lastNameValidationMessageLabel.setPalette(self.labelPalette)
        self.zipCodeValidationMessageLabel.setPalette(self.labelPalette)
        self.employeeIdValidationMessageLabel.setPalette(self.labelPalette)

        # Connect signals to slots.
        self.firstNameEdit.editingFinished.connect(self.firstNameEditingFinished)
        self.lastNameEdit.editingFinished.connect(self.lastNameEditingFinished)
        self.zipCodeEdit.editingFinished.connect(self.zipCodeEditingFinished)
        self.employeeIdEdit.editingFinished.connect(self.employeeIdEditingFinished)

        # Position on screen and show.
        self.resize(400, 100)
        self.center()
        self.show()
 
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())       
        
    def firstNameEditingFinished(self):
        firstName = self.firstNameEdit.text()
        validationError = self.validateFirstName(firstName)
        self.firstNameValidationMessageLabel.setText(validationError)

    def lastNameEditingFinished(self):
        lastName = self.lastNameEdit.text()
        validationError = self.validateLastName(lastName)
        self.lastNameValidationMessageLabel.setText(validationError)

    def zipCodeEditingFinished(self):
        zipCode = self.zipCodeEdit.text()
        validationError = self.validateZipCode(zipCode)
        self.zipCodeValidationMessageLabel.setText(validationError)

    def employeeIdEditingFinished(self):
        employeeId = self.employeeIdEdit.text()
        validationError = self.validateEmployeeId(employeeId)
        self.employeeIdValidationMessageLabel.setText(validationError)

    def validateMinimumStringLength(self, aString, minLen, fieldName):
        if len(aString) == 0:
            return "The %s must be filled in." % fieldName
        elif len(aString) < minLen:
            return "\"%s\" is not a valid %s. It is too short." % (aString, fieldName)
        return None

    def validateFirstName(self, firstName):
        lengthValidationResult = self.validateMinimumStringLength(firstName, self.MIN_FIRST_NAME_LEN, "first name")

        if lengthValidationResult != None:
            return lengthValidationResult

        if self.firstNameRegExp.match(firstName):
            return None 
        else:
            return "\"%s\" is not a valid first name. It must contain at least two letters." % firstName

    def validateLastName(self, lastName):
        lengthValidationResult = self.validateMinimumStringLength(lastName, self.MIN_LAST_NAME_LEN, "last name")

        if lengthValidationResult != None:
            return lengthValidationResult

        if self.lastNameRegExp.match(lastName):
            return None 
        else:
            return "\"%s\" is not a valid last name. It must contain at least two letters." % lastName

    def validateEmployeeId(self, employeeId):
        ret_val = "%s is not a valid ID." % employeeId

        if len(employeeId) != 7:
            return ret_val

        if not self.employIdRegExp.match(employeeId):
            return ret_val
                
        return None
    
    def validateZipCode(self, zipCode):
        if not self.zipCodeRegExp.match(zipCode):
            return "The ZIP code must be numeric."

        return None

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = TwentySevenChallengeTwo()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
