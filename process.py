'''
Created on 2012-7-4

@author: Vigi
'''
from category import Categorizer
from tools import generateProcessTree, getRoots

class Process(Categorizer):
    "Process Info."
    
    def __init__(self, file, processList):
        Categorizer.__init__(self, file)
        self.processList = processList
        self.processes = []
        
        
    def generateList(self):
        "Generate page contents."
        listFlag = None
        processList = generateProcessTree(list(set(self.processes)))
        roots = getRoots(processList)
        for root in roots:
#            if not listFlag:
#                listFlag = 'startUL'
#                self.file.write("<ul>")
#            self.file.write(r'<li><a href=".\files\%s.html" target="right" onclick="select(this)">%s</a></li><br>' % (root.fileId, root.commandLine))   # Modified by Vigi on 2012-7-9
            if root.commandLine.lower().find('.exe') == -1:
                if root.commandLine.lower().find('/') == -1:
                    if root.commandLine.lower().find('-') == -1: end = len(root.commandLine)
                    else: end = root.commandLine.lower().find('-') - 1
                else: end = root.commandLine.lower().find('/') - 1
            else: end = root.commandLine.lower().find('.exe') + 4
            self.file.write(r'- <a href=".\files\%s.html" target="right" onclick="select(this)"><font color="blue" size="2">%s</font></a><br>' % (root.fileId, root.commandLine[:end].strip('"')))   # Modified by Vigi on 2012-7-9
            self.generateChildren(root, 1)
#        for process in sorted(set(self.processes), key=lambda process: process.commandLine):
#            if not listFlag:
#                listFlag = 'startUL'
#                self.file.write("<ul>")
#            self.file.write(r'<li><a href=".\files\%s.html" target="right">%s</a></li>' % (process.fileId, process.commandLine))
#        if listFlag == 'startUL':
#            self.file.write("</ul>")
            
    def addToFile(self, fileList):
        "Add process property to file object."
        for processid, process in self.processList.items():
            for dll in process.dlls:
                fileList[dll].process.append(process.commandLine)
                self.processes.append(process)
    
    def toHtml(self, fileList):
        "Generate process list html"
        self.startPage()
        self.addToFile(fileList)
        self.generateList()
        self.endPage()
    
    def generateChildren(self, process, level):
        if process.children == []: return
        for childProcess in process.children:
            self.file.write('&nbsp;&nbsp;' * level)
            if childProcess.commandLine.lower().find('.exe') == -1:
                if childProcess.commandLine.lower().find('/') == -1:
                    if childProcess.commandLine.lower().find('-') == -1: end = len(childProcess.commandLine)
                    else: end = childProcess.commandLine.lower().find('-') - 1
                else: end = childProcess.commandLine.lower().find('/') - 1
            else: end = childProcess.commandLine.lower().find('.exe') + 4 # Thanks Zero.
            self.file.write(r'|- <a href=".\files\%s.html" target="right" onclick="select(this)"><font color="blue" size="2">%s</font></a><br/>' % (childProcess.fileId, childProcess.commandLine[:end].strip('"')))
            self.generateChildren(childProcess, level+1)
        