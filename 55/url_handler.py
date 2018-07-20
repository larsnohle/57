import mongo_dao


class UrlHandler:
    def __init__(self):
        self.mongoDao = mongo_dao.MongoDao()
    
    def getTextForUrl(self, url):
        return self.mongoDao.getTextForUrl(url)
        
    def snippetExistsForUrl(self, url):
        return self.mongoDao.urlExists(url)

    def addTextSnippet(self, url, text):
        self.mongoDao.addTextSnippet(url, text)

    def setTextForUrl(self, url, text):
        self.mongoDao.setTextForUrl(url, text)
        
    def generateAndAddSnippet(self, text):
        # Fetch all used urls.
        urls = self.mongoDao.getAllUrls()

        # First mapping ever?
        if len(urls) == 0:
            url = 'a'
        else:
            # No. Generate next mapping
            urlsSorted = self.sortListByLength(urls)
            url = self.nextIdentifierAfter(urlsSorted[-1])
            
        self.addTextSnippet(url, text)
        return url
            
    ### UTILITY METHODS
        
    def sortListByLength(self, l):
        new_list = list()
        for i in l:
            if len(new_list) == 0:
                new_list.append(i)
        else:
            for (index, ni) in enumerate(new_list):
                if len(i) < len(ni) or (len(i) == len(ni) and i < ni):
                    new_list.insert(index, i)
                    break
            else:
                new_list.append(i)
                    
        return new_list

    def nextIdentifierAfter(self, s):
        index_of_last_character = len(s) - 1
        next_identifier_as_list = list(s)
        last_character = s[index_of_last_character]
        if last_character < 'z':
            next_identifier_as_list[index_of_last_character] = chr(ord(last_character) + 1)
        else:
            i = index_of_last_character - 1
            while i >= 0:
                if next_identifier_as_list[i] < 'z':
                    next_identifier_as_list[i] = chr(ord(next_identifier_as_list[i]) + 1)
                    break
                else:
                    i -= 1
            else:
                next_identifier_as_list = list('a' * (len(s) + 1))
        return ''.join(next_identifier_as_list)
    
### MAIN ###

if __name__ == '__main__':
    # Test some stuff.
    instance = UrlHandler()
    text = 'a.b.c'
    url = instance.generateAndAddSnippet(text)
    print("text: %s url: %s" % (text, url))
    text = 'a.b.c'
    url = instance.generateAndAddSnippet(text)
    print("text: %s url: %s" % (text, url))
    text = 'a.b.b'
    url = instance.generateAndAddSnippet(text)
    print("text: %s url: %s" % (text, url))
    text = 'b.b.b'
    url = instance.generateAndAddSnippet(text)
    print("text: %s url: %s" % (text, url))
    text = 'a.b.b'
    url = instance.generateAndAddSnippet(text)
    print("text: %s url: %s" % (text, url))   
    
