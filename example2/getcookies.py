#-*- coding:utf-8 -*-
import browsercookie
from scrapy.downloadermiddlewares.cookies import CookiesMiddleware

class BrowserCookiesMiddleware(CookiesMiddleware):
    def __int__(self,debug=False):
        super(debug).__init__(debug)
        self.load_browser_cookies()

    def load_browser_cookies(self):
        #加载chrome浏览器中的cookies
        jar=self.jars['chrome']
        chorme_cookiejar=browsercookie.chrome()
        #firefox_cookiejar=browsercookie.firefox()
        for cookie in chorme_cookiejar:
            jar.set_cookie(cookie)


chorme_cookiejar=browsercookie.chrome()
        #firefox_cookiejar=browsercookie.firefox()
for cookie in chorme_cookiejar:
    print cookie