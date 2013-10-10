'''
Created on 2012-7-4

@author: Vigi
'''
from autorun import Autorun
import re

class Drivers(Autorun):
    "Drivers Info."
    
    def __init__(self, file, autorunList):
        Autorun.__init__(self, file, autorunList)
        
    def addToFile(self, fileList):
        "Add autorun property to file object."
        for autorun in self.autorunList.values():
            if autorun.groupId == 'Codecs':
                if int(autorun.fileId) < 0: continue
                fileList[autorun.fileId].drivers = autorun.location
                if re.search(r'HKLM\\SOFTWARE\\Classes\\CLSID\\\{(.*)\}(.*)', autorun.location):
                    continue
                self.autoruns[fileList[autorun.fileId].path] = autorun