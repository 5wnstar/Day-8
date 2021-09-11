# Day-8
30 days of codding 


Extracting cookie information after visiting a website
Many websites use cookies to store their various information on to your local disk. You would like 
to see this cookie information and perhaps log in to that website automatically using cookies.


Let us try to pretend to log in to a popular code-sharing website, www.facebook.com. We 
would like to submit the login information on the login page, https://facebook.com/
account/signin/?next=/.





We have used Python's cookielib and set up a cookie jar, cj. The login data has been 
encoded using urllib.urlencode. urllib2 has a build_opener() method, which takes 
the predefined cookie jar with an instance of HTTPCookieProcessor() and returns a URL 
opener. We call this opener twice: once for the login page and once for the home page of the 
website. It seems that only one cookie, bb_session, was set with the set-cookie directive 
present in the page header.
