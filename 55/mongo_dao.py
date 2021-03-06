from pymongo import MongoClient

HOST = 'localhost'
PORT = 27017

# FIELDS IN THE DOCUMENTS.
URL = "url"
TEXT = "text"

# DAO CLASS FOR TEXT SNIPPETS.
class MongoDao:   
    def __init__(self):
        self.mongoClient = MongoClient(HOST, PORT)
        self.db = self.mongoClient.exercise55
        self.textSnippets = self.db.textSnippets

    def getAllTextSnippets(self):
        return self.textSnippets.find()

    def getAllUrls(self):
        urls = list()
        for textSnippet in self.textSnippets.find():
            urls.append(textSnippet[URL])            
        return urls

    def urlExists(self, url):
        textSnippet = self.textSnippets.find_one({URL: url})
        return textSnippet != None
    
    def getTextForUrl(self, url):
        textSnippet = self.textSnippets.find_one({URL: url})
        text = None
        if textSnippet:
            text = textSnippet[TEXT]
        return text
            
    def setTextForUrl(self, url, text):
        self.textSnippets.update_one({URL: url}, {'$set': {TEXT: text}})
    
    def addTextSnippet(self, url, text):
        self.textSnippets.insert({URL: url, TEXT: text})

        
### MAIN ###

if __name__ == '__main__':
    # TEST STUFF
    instance = MongoDao()
    textSnippets = instance.getAllTextSnippets()
    for textSnippet in textSnippets:
        print("URL: %s Text: %s" % (textSnippet[URL], textSnippet[TEXT]))

    text = 'A small text'
    url = 'a'
#    instance.addTextSnippet(url, text)

    textSnippets = instance.getAllTextSnippets()
    for textSnippet in textSnippets:
        print("URL: %s Text: %s" % (textSnippet[URL], textSnippet[TEXT]))

    urls = instance.getAllUrls()
    print("All URLs:")
    for u in urls:
        print(u)

    print('Will get text for URL: %s' % url)
    t = instance.getTextForUrl(url)
    print(t)

    t2 = t + "_again"
    print('Will set text for URL %s to %s' % (url, t2))
    instance.setTextForUrl(url, t2)

    print('Text for URL %s is now:' % url)
    t = instance.getTextForUrl(url)
    print(t)
