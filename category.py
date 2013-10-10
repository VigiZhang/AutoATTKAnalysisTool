'''
Created on 2012-7-4

@author: Vigi
'''
import re

class Categorizer():
    def __init__(self, file):
        self.file = open(file, 'w')
        
    def generateList(self):
        "Generate list"
        pass
        
    def startPage(self):
        self.file.write(r'<html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8" /><title>')
        m = re.match(r"[\.\\a-zA-Z]*?\\([a-zA-Z]*)\.html", self.file.name)
        self.file.write(m.group(1))
        self.file.write(r'</title><script language="javascript">function select(obj){var links = document.getElementsByTagName("a");for(i=0;i<links.length;i++){links[i].style.fontWeight="normal"}obj.style.fontWeight="bold"}</script></head><body>')

    def endPage(self):
        self.file.write(r'</body></html>')
        self.file.close()
        
    def writeToHTML(self):
        self.startPage()
        self.generateList()
        self.endPage()