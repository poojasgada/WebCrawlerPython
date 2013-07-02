'''
Created on Jul 1, 2013

@author: psgada
'''
#References:
#http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html
#http://answers.oreilly.com/topic/1088-how-to-build-a-simple-web-crawler/
#To install the latest BeautifulSoup, just do a easy_install or pip install

#This is a bare minimum web crawler using the Beautiful soup Api
#A lot of features to add in the future like depth and stuff

import urllib2
from bs4 import BeautifulSoup

class YetAgainCrawlerSoup():
     def __init__(self, url):
         self.file_writer = open("Crawler-OutputC.txt", 'w')
         self.init_url = url
         self.urls = None
         self.found_url = False
         
     def extract_urls(self):
        try:
            page = urllib2.urlopen(self.init_url)
        except:
            print "Unable to open the web page"        
            return
    
        page_soup = BeautifulSoup(page.read())
        self.urls = page_soup('a', href=True)
        
        if self.urls:
            self.found_url = True
            self.write_urls_tofile()
    

     def write_urls_tofile(self):
        if self.found_url == True:
            for a_tag in self.urls:
                self.file_writer.write("URL: "+a_tag['href'] +"\n")
                    

def crawler_beautifulsoup():
    crawl = YetAgainCrawlerSoup('http://kiwitobes.com/wiki/Programming_language.html')
    crawl.extract_urls()
    crawl.file_writer.close()


crawler_beautifulsoup()