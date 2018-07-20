#!/usr/bin/python
# -*- coding: utf-8 -*-

# Fick inte authentiseringen att funka. Mkt svårt att felsöka. Orkar inte. Skiter i det. LN 2018-07-10.

import sys
import http.client
import re
import datetime;
import random

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QImage
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPixmap


#$ curl --request GET 
# --url 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular' 
# --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
# oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
# oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
# oauth_token="access-token-for-authed-user", oauth_version="1.0"'

# curl --request GET  --url 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular'  --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app",  oauth_nonce="generated-nonce", oauth_signature="generated-signature",  oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp",  oauth_token="access-token-for-authed-user", oauth_version="1.0"'

curl --request GET  --url 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular'  --header 'authorization: OAuth oauth_consumer_key="maDF5Ns7UrP3atWzCt7wJwZ5c",  oauth_nonce="oQdC5xZ10DLhl2jMERIMej1py73fcLOl", oauth_signature="generated-signature",  oauth_signature_method="HMAC-SHA1", oauth_timestamp="1531215246",  oauth_token="1589408701-QQpGPWp04Cc6KtRpNPl3lLJoQjdT3BaWtdVBrTn", oauth_version="1.0"'

# oauth_nonce: oQdC5xZ10DLhl2jMERIMej1py73fcLOl
# oauth_signature: 
# oauth_timestamp: 1531215246



FLICKR_MAIN_URL = 'api.flickr.com'
FLICKR_PATH = '/services/feeds/photos_public.gne?tags='
image_link_reg_exp = re.compile('.*img src=&quot;http(s)*://([^/]+)(.*\\.jpg)&quot;.*')

lower_case_letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
upper_case_letters = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
sequences_to_pick_data_from = [lower_case_letters, upper_case_letters, digits]
NONCE_LENGTH = 32

########################## MAIN CLASS ##########################
class FortyNine(QtGui.QWidget):    
    def __init__(self):
        super(FortyNine, self).__init__()

        # Instance variables.
        self.searchStringLabel = None
        self.searchStringTextEdit = None
        self.searchButton = None
        self.tagDescriptionLabel = None
        self.imageLabels = list()
        self.imageLabelLayout = QtGui.QVBoxLayout()
        
        self.setWindowTitle('Forty Nine Challenge 2')
        
        # Setup the GUI.
        self.initUI()

    def initUI(self):        
        # Create widgets.
        self.searchStringLabel = QtGui.QLabel("Search string")
        self.searchTextEdit = QtGui.QLineEdit("", self)
        self.searchButton = QtGui.QPushButton("&Search")
        self.tagDescriptionLabel = QtGui.QLabel()
        
        # LAYOUT FOR THE WIDGETS.

        # Search layout.
        searchLayout = QtGui.QHBoxLayout()
        searchLayout.addWidget(self.searchStringLabel)
        searchLayout.addWidget(self.searchTextEdit)
        searchLayout.addWidget(self.searchButton)    
        
        # Create scroll area to put the input widgets and the images in.
        groupBox = QtGui.QGroupBox('')
        groupBox.setLayout(self.imageLabelLayout)
        scrollArea = QtGui.QScrollArea()
        scrollArea.setWidget(groupBox)
        scrollArea.setWidgetResizable(True)

        # Add the scroll area to a layout...
        mainLayout = QtGui.QVBoxLayout(self)
        mainLayout.addLayout(searchLayout)
        mainLayout.addWidget(self.tagDescriptionLabel)
        mainLayout.addWidget(scrollArea)
        
        # A set layout of this widget.
        self.setLayout(mainLayout) 

        # Connect signals to slots.
        self.searchButton.clicked.connect(self.searchButtonClicked)

        # Give focus to the seach field.
        self.searchTextEdit.setFocus()
        
        # Position on screen and show.
        self.resize(400, 400)
        self.center()
        self.show()
 
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())       

    def searchButtonClicked(self, index):
        search_criteria = self.searchTextEdit.text()
        feed = self.loadFeedFromFlickr(search_criteria)
        pictures = self.loadPictures(feed)
        print("Number of pictures loaded: %d" % len(pictures))
        self.displayPicturesInLabes(pictures)
        self.tagDescriptionLabel.setText('Photos about "%s"' % search_criteria)

    def loadFeedFromFlickr(self, searchText):
        conn = http.client.HTTPConnection(FLICKR_MAIN_URL)
        sub_url = FLICKR_PATH + searchText
        print("sub_url: %s" % sub_url)
        print(FLICKR_MAIN_URL + sub_url)
        conn.request("GET", sub_url)
        response = conn.getresponse()
        return response.read().decode()

    def loadPictures(self, feed):
        pictures = list()
        lines = feed.split("\n")
        for line in lines:
            match = image_link_reg_exp.match(line)
            if match:
                domain = match.group(2)
                path = match.group(3)
                picture = self.loadPicture(domain, path)
                pictures.append(picture)
            else:
                pass
        return pictures
    
    def loadPicture(self, domain, path):        
        conn = http.client.HTTPConnection(domain)        
        conn.request("GET", path)
        response = conn.getresponse()
        return response.read()

    def displayPicturesInLabes(self, pictures):
        self.removeAllImageLabels()
        for picture in pictures:
            imageLabel = self.createImageLabel(picture)
            self.imageLabelLayout.addWidget(imageLabel)
            self.imageLabels.append(imageLabel)
            
    def removeAllImageLabels(self):
        for imageLabel in self.imageLabels:
            self.imageLabelLayout.removeWidget(imageLabel)
            
    def createImageLabel(self, picture):
        image = QImage()
        image.loadFromData(picture)
        imageLabel = QLabel()
        imageLabel.setPixmap(QPixmap.fromImage(image))
        return imageLabel

    def generateTimestamp(self):
        return int(datetime.datetime.now().timestamp())

    def generate_nonce(self, length):
        return self.generate_random_string(NONCE_LENGTH)
    
    def generate_random_string(self, length):
        l = list()
        for i in range(length):
            sequence = sequences_to_pick_data_from[random.randint(0, len(sequences_to_pick_data_from) - 1)]
            c = sequence[random.randint(0, len(sequence) - 1)]
            l.append(c)
        return ''.join(l)

    
def main():
    app = QtGui.QApplication(sys.argv)
    ex = FortyNine()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
