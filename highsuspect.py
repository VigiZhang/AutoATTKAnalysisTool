'''
Created on 2012-7-4

@author: Vigi
'''
from category import Categorizer
from tools import *

class HighSuspecter(Categorizer):
    "High suspect file lists"
    
    def __init__(self, file, fileList):
        Categorizer.__init__(self, file)
        self.fileList = fileList
        self.highlightConfig = parseHighlightConfig()
        self.validateConfig = parseValidateConfig()
        
    def generateList(self):
        listFlag = None
        for file in sorted(self.fileList.values(), key=lambda file: file.path):
#            if whiteList(file): continue    # Modified by Vigi on 2012-7-12
            if self.highsuspect(file):
                if not listFlag:
                    listFlag = 'startUL'
                    self.file.write("<ul>")
                if file.attributes != 'A':
                    self.file.write(r'<li><a href=".\files\%s.html" target="right" onclick="select(this)"><font color="red">%s</font></a></li>' % (file.id, file.path))
                elif self.highlightConfigration(self.highlightConfig, file):
                    self.file.write(r'<li><a href=".\files\%s.html" target="right" onclick="select(this)"><font color="red">%s</font></a></li>' % (file.id, file.path))
                else:
                    self.file.write(r'<li><a href=".\files\%s.html" target="right" onclick="select(this)"><font color="blue">%s</font></a></li>' % (file.id, file.path))
            elif self.lowsuspect(file):
                if not listFlag:
                    listFlag = 'startUL'
                    self.file.write("<ul>")
                if self.highlightConfigration(self.highlightConfig, file):
                    self.file.write(r'<li><a href=".\files\%s.html" target="right" onclick="select(this)"><font color="orange">%s</font></a></li>' % (file.id, file.path))
                else:
                    self.file.write(r'<li><a href=".\files\%s.html" target="right" onclick="select(this)"><font color="gray">%s</font></a></li>' % (file.id, file.path))
        if listFlag == 'startUL':
            self.file.write("</ul>")
            
    def highsuspect(self, file):
        "Validate whether it is high suspect."
        if file.attributes.strip():
            if file.attributes.find('H') != -1: return True
        # Remove OriginalFileName condition in high suspect list by Vigi on 2012-7-9
        # Readd OriginalFileName condition in high suspect list by Vigi on 2012-7-12
        if (file.autorun.strip() != '' or file.process != [] or file.service.strip() != '' or file.drivers.strip() != '') and self.validateConfigration(self.validateConfig, file): return True
        else: return False
        
    def lowsuspect(self, file):
        "Validate whether it is low suspect."
        if file.attributes != 'A': return True
        if self.validateConfigration(self.validateConfig, file): return True
        else: return False
        
    def toHtml(self):
        self.startPage()
        self.generateList()
        self.endPage()
        
    def highlightConfigration(self, highlightConfig, file):
        "Set the file colored condition in config.ini."
        if highlightConfig['productName'] == '1' and file.productName != '':
            return False
        if highlightConfig['productVersion'] == '1' and file.productVersion != '':
            return False
        if highlightConfig['companyName'] == '1' and file.companyName != '':
            return False
        if highlightConfig['fileDescription'] == '1' and file.fileDescription != '':
            return False
        if highlightConfig['originalFilename'] == '1' and file.originalFilename != '':
            return False
        if highlightConfig['fileVersionLabel'] == '1' and file.fileVersionLabel != '':
            return False
        if highlightConfig['fileVersionNumber'] == '1' and file.fileVersionNumber != '':
            return False
        return True
    
    def validateConfigration(self, validateConfig, file):
        if validateConfig['productName'] == '1' and file.productName == '':
            return True
        if validateConfig['productVersion'] == '1' and file.productVersion == '':
            return True
        if validateConfig['companyName'] == '1' and file.companyName == '':
            return True
        if validateConfig['fileDescription'] == '1' and file.fileDescription == '':
            return True
        if validateConfig['originalFilename'] == '1' and file.originalFilename == '':
            return True
        if validateConfig['fileVersionLabel'] == '1' and file.fileVersionLabel == '':
            return True
        if validateConfig['fileVersionNumber'] == '1' and file.fileVersionNumber == '':
            return True
        return False
