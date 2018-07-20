import mongo_dao


class UrlHandler:
    def __init__(self):
        self.mongoDao = mongo_dao.MongoDao()

    def short_url_exists_for(self, shortUrl):
        return self.mongoDao.getLongUrlForShortUrl(shortUrl) != None
    
    def get_long_url_for_short_url(self, shortUrl):
        return self.mongoDao.getLongUrlForShortUrl(shortUrl)
        
    def mapping_exists(self, longUrl):
        return self.mongoDao.getShortUrlForLongUrl(longUrl) != None

    def add_mapping(self, shortUrl, longUrl):
        self.mongoDao.addMapping(shortUrl, longUrl)
        
    def generate_and_add_short_url(self, longUrl):
        # Mapping already exists?
        if self.mapping_exists(longUrl):
            return self.mongoDao.getShortUrlForLongUrl(longUrl)

        # Fetch all used short URLs.
        shortUrls = self.mongoDao.getAllShortUrls()

        # No
        # First mapping ever?
        if len(shortUrls) == 0:
            short_url = 'a'
        else:
            # No. Generate next mapping
            existing_short_urls_sorted = self.sort_list_by_length(shortUrls)
            short_url = self.next_identifier_after(existing_short_urls_sorted[-1])
            
        self.add_mapping(short_url, longUrl)
        return short_url

    def short_url_invoked(self, shortUrl):
        self.mongoDao.shortUrlInvoked(shortUrl)

    def get_number_of_invocations(self, shortUrl):
        return self.mongoDao.getNumberOfInvocations(shortUrl)
            
    ### UTILITY METHODS
        
    def sort_list_by_length(self, l):
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

    def next_identifier_after(self, s):
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
    long_url = 'a.b.c'
    short_url = instance.generate_and_add_short_url(long_url)
    print("Long url: %s short url: %s" % (long_url, short_url))
    long_url = 'a.b.c'
    short_url = instance.generate_and_add_short_url(long_url)
    print("Long url: %s short url: %s" % (long_url, short_url))
    long_url = 'a.b.b'
    short_url = instance.generate_and_add_short_url(long_url)
    print("Long url: %s short url: %s" % (long_url, short_url))
    long_url = 'b.b.b'
    short_url = instance.generate_and_add_short_url(long_url)
    print("Long url: %s short url: %s" % (long_url, short_url))
    long_url = 'a.b.b'
    short_url = instance.generate_and_add_short_url(long_url)
    print("Long url: %s short url: %s" % (long_url, short_url))   

    
    instance.short_url_invoked(short_url)
    print("Number of invocations %d" % instance.get_number_of_invocations(short_url))
    instance.short_url_invoked(short_url)
    print("Number of invocations %d" % instance.get_number_of_invocations(short_url))
    instance.short_url_invoked(short_url)
    print("Number of invocations %d" % instance.get_number_of_invocations(short_url))
    instance.short_url_invoked(short_url)
    print("Number of invocations %d" % instance.get_number_of_invocations(short_url))
    instance.short_url_invoked(short_url)
    print("Number of invocations %d" % instance.get_number_of_invocations(short_url))

    
