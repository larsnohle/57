#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class TwentyFiveChallengeOne(QtGui.QWidget):
    
    def __init__(self):
        super(TwentyFiveChallengeOne, self).__init__()
        
        # Constants
        self.VERY_WEAK = 1
        self.WEAK = 2
        self.STRONG = 3
        self.VERY_STRONG = 4
        self.AVERAGE = 5

        self.VERY_WEAK_STRING = "very weak"
        self.WEAK_STRING = "weak"
        self.STRONG_STRING = "strong"
        self.VERY_STRONG_STRING = "very strong"
        self.AVERAGE_STRING = "average"

        self.rating_dict = {}
        self.rating_dict[self.VERY_WEAK] = self.VERY_WEAK_STRING
        self.rating_dict[self.WEAK] = self.WEAK_STRING
        self.rating_dict[self.STRONG] = self.STRONG_STRING
        self.rating_dict[self.VERY_STRONG] = self.VERY_STRONG_STRING
        self.rating_dict[self.AVERAGE] = self.AVERAGE_STRING

        self.rating_colour_dict = {}
        self.rating_colour_dict[self.VERY_WEAK] = QtCore.Qt.red
        self.rating_colour_dict[self.WEAK] = QtCore.Qt.yellow
        self.rating_colour_dict[self.STRONG] = QtCore.Qt.green
        self.rating_colour_dict[self.VERY_STRONG] = QtCore.Qt.blue
        self.rating_colour_dict[self.AVERAGE] = QtCore.Qt.black

        self.special_characters = "! \" # $ % & \\ ' ( ) * + , - . / : ; < = > ? @ [ \ \ ] ^ _ ` { | } ~".split()

        # Instance variables.
        self.passwordLabel = None
        self.passwordEdit = None
        self.ratingMessageLabel = None
        self.ratingLabel = None

        self.labelPalette = None

        # Setup the GUI.
        self.initUI()
        
    def initUI(self):        
        # Create widgets.
        self.passwordLabel = QtGui.QLabel("Password")
        self.passwordEdit = QtGui.QLineEdit()
        self.ratingLabel = QtGui.QLabel("Rating")
        self.ratingMessageLabel = QtGui.QLabel("")

        # LAYOUT FOR THE WIDGETS.

        # Set up layout to contain the widgets.
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # Add widgets to the layout.
        grid.addWidget(self.passwordLabel, 1, 0)
        grid.addWidget(self.passwordEdit, 1, 1)

        grid.addWidget(self.ratingLabel, 2, 0)
        grid.addWidget(self.ratingMessageLabel, 2, 1)

        # Create layout to take care of extra vertical space.
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addStretch(1)

        # A set layout of this widget.
        self.setLayout(vbox) 

        # Set up palette for the output text field.
        self.labelPalette = QtGui.QPalette()
        self.labelPalette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.black)
        self.ratingMessageLabel.setPalette(self.labelPalette)

        # Connect signals to slots.
        self.passwordEdit.textChanged.connect(self.passwordChanged)

        # Position on screen and show.
        self.resize(400, 100)
        self.center()
        self.show()
 
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())       
        
    def passwordChanged(self):
        password = self.passwordEdit.text()
        rating = self.ratePassword(password)
        self.ratingMessageLabel.setText(self.translateRatingToString(rating))
        self.setColorBasedOnRating(rating)

    def contains_digit(self, s):
        for c in s:
            if c.isdigit():            
                return True
        return False

    def contains_only_digits(self, s):
        for c in s:
            if not c.isdigit():
                return False
        return True

    def contains_special_character(self, s):
        for c in s:
            if c in self.special_characters:
                return True
        return False

    def contains_letter(self, s):
        for c in s:
            if c.isalpha():
                return True
        return False

    def contains_only_letters(self, s):
        for c in s:
            if not c.isalpha():
                return False
        return True


    def ratePassword(self, pwd):
        if len(pwd) < 8:
            if self.contains_only_digits(pwd):
                return self.VERY_WEAK
            elif self.contains_only_letters(pwd):
                return self.WEAK
        else:
            if self.contains_letter(pwd) and self.contains_digit(pwd):
                if self.contains_special_character(pwd):
                    return self.VERY_STRONG
                else:
                    return self.STRONG

        return self.AVERAGE # Not defined in the exercise. 

    def translateRatingToString(self, rating):
        return self.rating_dict[rating]

    def setColorBasedOnRating(self, rating):
        colourToSet = self.rating_colour_dict[rating]
        self.labelPalette.setColor(QtGui.QPalette.Foreground, colourToSet)
        self.ratingMessageLabel.setPalette(self.labelPalette)

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = TwentyFiveChallengeOne()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
