from urllib.request import urlopen 
from urllib.error import HTTPError
def getSinglePage(url):
    try:
        rawPage = urlopen(url)
        print(rawPage.read)
    except HTTPError as ee:
        print(ee.reason)
        print(ee.code)
        #print(ee.headers)
        return None
    
urlToGet = r'http://www.niituniversity.in/'
ourPage = getSinglePage(urlToGet)