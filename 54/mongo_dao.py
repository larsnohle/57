from pymongo import MongoClient

HOST = 'localhost'
PORT = 27017

SHORT_URL = "shortUrl"
LONG_URL = "longUrl"
NUMBER_OF_INVOCATIONS = "numberOfInvocations"

class MongoDao:   
    def __init__(self):
        self.mongoClient = MongoClient(HOST, PORT)
        self.db = self.mongoClient.exercise54
        self.urlMappings = self.db.urlMappings
        self.invocations = self.db.invokations

    def getAllUrlMappings(self):
        return self.urlMappings.find()

    def getAllShortUrls(self):
        shortUrls = list()
        for mapping in self.urlMappings.find():
            shortUrls.append(mapping[SHORT_URL])            
        return shortUrls

    def getShortUrlForLongUrl(self, longUrl):
        mapping = self.urlMappings.find_one({LONG_URL: longUrl})
        shortUrl = None
        if mapping:
            shortUrl = mapping[SHORT_URL]
        return shortUrl
            
    def getLongUrlForShortUrl(self, shortUrl):
        mapping = self.urlMappings.find_one({SHORT_URL: shortUrl})
        longUrl = None
        if mapping:
            longUrl = mapping[LONG_URL]
        return longUrl

    def addMapping(self, shortUrl, longUrl):
        self.urlMappings.insert({LONG_URL: longUrl, SHORT_URL: shortUrl})

    def shortUrlInvoked(self, shortUrl):
        invocation_document = self.invocations.find_one({SHORT_URL: shortUrl})
        if invocation_document == None:
            self.invocations.insert({SHORT_URL: shortUrl, NUMBER_OF_INVOCATIONS: 1})
        else:
            self.invocations.update_one({SHORT_URL: shortUrl}, {'$inc': {NUMBER_OF_INVOCATIONS: 1}})

    def getNumberOfInvocations(self, shortUrl):
        invocation_document = self.invocations.find_one({SHORT_URL: shortUrl})
        if invocation_document == None:
            return 0
        else:
            return invocation_document[NUMBER_OF_INVOCATIONS]
        
### MAIN ###

if __name__ == '__main__':
    instance = MongoDao()
    mappings = instance.getAllUrlMappings()
    for mapping in mappings:
        print("Short URL: %s Long URL: %s" % (mapping[SHORT_URL], mapping[LONG_URL]))

    shortUrl = 'd'
    numberOfInvocations = instance.getNumberOfInvocations(shortUrl)
    print("Number of invocations of %s is %d" % (shortUrl, numberOfInvocations))
    print("Will invoke %s" % shortUrl)

    instance.shortUrlInvoked(shortUrl)

    numberOfInvocations = instance.getNumberOfInvocations(shortUrl)
    print("Number of invocations of %s is now %d" % (shortUrl, numberOfInvocations))

    longUrl = instance.getLongUrlForShortUrl(shortUrl)
    print("LongURL: %s for shortUrl: %s" % (longUrl, shortUrl))    
    print("ShortURL: %s for longtUrl: %s" % (shortUrl, instance.getShortUrlForLongUrl(longUrl)))
    
#    instance.addMapping('d', "www.dn.se")
#    mappings = instance.getAllUrlMappings()
#    for mapping in mappings:
#        print("Short URL: %s Long URL: %s" % (mapping[SHORT_URL], mapping[LONG_URL]))

    
