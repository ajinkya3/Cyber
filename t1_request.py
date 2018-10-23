import requests
def getSinglePage(url):
    try:
        rawPage = requests.get(urlToGet)
        print(rawPage.text)
    except:
        print(rawPage.status_code)
        print(rawPage.reason)
urlToGet = r'http://www.niituniversity.in/'
getSinglePage(urlToGet)