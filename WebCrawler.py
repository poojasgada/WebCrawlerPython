'''
Created on Jun 30, 2013

@author: psgada
'''
#References:
#http://answers.oreilly.com/topic/1088-how-to-build-a-simple-web-crawler/
#http://stackoverflow.com/questions/3276040/how-can-i-use-the-python-htmlparser-library-to-extract-data-from-a-specific-div

#Ways 
#Way 1 - Beautiful Soup - Next Check in
#Way 2 - HTMLParser - Implemented In here

import urllib2
from HTMLParser import HTMLParser

def crawler_basic():
    page = urllib2.urlopen('http://kiwitobes.com/wiki/Programming_language.html')
    page_content = page.read()
    
    print page_content[0:50]
    
#crawler_basic()

#An extremely simple crawler which extract all the <a> tag href values
class YetAgainHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)        
        self.foundTag = 0
        self.dataTag = []
        
    def handle_starttag(self, tag, attr):
        if tag == 'a':
            for attr_name, attr_value in attr:
                if attr_name == "href":
                    print "URL " + attr_value
                
                self.foundTag = 1
        
    def handle_endtag(self, tag):
        if tag == 'a':
            self.foundTag -= 1
         
    def handle_data(self, data):
        if self.foundTag:
            self.dataTag.append(data)
            
def htmlparser_based_crawler():
    page = urllib2.urlopen('http://kiwitobes.com/wiki/Programming_language.html')
    page_content = page.read()
    
    par = YetAgainHTMLParser()
    par.feed(page_content)
    
    #print par.dataTag
    
    par.close()
    
htmlparser_based_crawler()