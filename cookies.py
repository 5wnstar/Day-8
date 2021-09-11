import cookielib 
import urllib
import urllib2
ID_USERNAME = ('id_username')
ID_PASSWORD = ('id_password')
USERNAME = ('you@email.com')
PASSWORD = ('mypassword')
LOGIN_URL = ('https://facebook.com/account/signin/?next=/')
NORMAL_URL = ('https://facebook.com/')
def extract_cookie_info():
    # setting up cookie jar
    cj = cookielib.CookieJar()
    login_data = urllib.urlencode({ID_USERNAME : USERNAME, 
    ID_PASSWORD : PASSWORD})
    # creating  url opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    resp = opener.open(LOGIN_URL, login_data)
    # sending login info 
    for cookie in cj:
        print ("----First time cookie:  --> ", (cookie.name, cookie.value))
        print ("Headers: %s", resp.headers)
    # now accessing without any login info
    resp = opener.open(NORMAL_URL)
    for cookie in cj:
        print ("Second time cookie: --> ", (cookie.name, cookie.value))
 
    print ("Headers: ", resp.headers)
if __name__ == '__main__':
 extract_cookie_info()
