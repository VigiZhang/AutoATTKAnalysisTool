'''
Created on 2012-7-4

@author: Vigi
'''
from autorun import Autorun

class Service(Autorun):
    "Service Info."
    
    def __init__(self, file, autorunList):
        Autorun.__init__(self, file, autorunList)
        
    def addToFile(self, fileList):
        "Add autorun property to file object."
        for autorun in self.autorunList.values():
            if autorun.groupId == 'Service':
                if int(autorun.fileId) < 0: continue
                fileList[autorun.fileId].service = autorun.location
                self.autoruns[fileList[autorun.fileId].path] = autorun
    
