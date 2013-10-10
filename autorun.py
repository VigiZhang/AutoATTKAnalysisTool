'''
Created on 2012-7-4

@author: Vigi
'''
from category import Categorizer

class Autorun(Categorizer):
    "Autorun lists."
    
    def __init__(self, file, autorunList):
        Categorizer.__init__(self, file)
        self.autorunList = autorunList
        self.autoruns = {}
        
    def generateList(self):
        "Generate page contents."
        listFlag = None
        for filePath, autorun in sorted(self.autoruns.items(), key=lambda d: d[1]):
            if not listFlag:
                listFlag = 'startUL'
                self.file.write("<ul>")
            self.file.write(r'<li>%s<br/><a href=".\files\%s.html" target="right" onclick="select(this)"><font color="blue">%s</font></a></li>' % (autorun.location, autorun.fileId, filePath))
        if listFlag == 'startUL':
            self.file.write("</ul>")
            
    def addToFile(self, fileList):
        "Add autorun property to file object."
        for autorun in self.autorunList.values():
            if autorun.groupId == 'Logon' or autorun.groupId == 'App_Inits' or autorun.groupId == 'WinLogon':
                if int(autorun.fileId) < 0: continue
                fileList[autorun.fileId].autorun = autorun.location
                self.autoruns[fileList[autorun.fileId].path] = autorun
    
    def toHtml(self, fileList):
        "Generate autorun list html"
        self.startPage()
        self.addToFile(fileList)
        self.generateList()
        self.endPage()