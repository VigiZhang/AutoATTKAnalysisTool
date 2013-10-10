'''
Created on 2012-7-4

@author: Vigi
'''
from ConfigParser import ConfigParser
import sys

def getValue(str):
    "Convert str coding and assign default value"
    return convertCoding(assignDefault(str))
    
def convertCoding(str):
    "Convert coding"
#    if str:
#        str.decode('UTF-8').encode('GB18030')
    return str

def assignDefault(str):
    "Assign default value to str"
    return str if str is not None else ''

def whiteList(file):
    "Reading .\config.ini [WHITEPAPER] section and compare"
    config = ConfigParser()
    try:
        config.read(r'config.ini')
        whiteFlag = False
        filename = getFileName(file)
        for item in config.items('WHITELIST'):
            if filename == item[0]:
                if file.md5 == item[1]:
                    whiteFlag = True
                    break
    except: pass
    finally: return whiteFlag
    
def parseHighlightConfig():
    config = ConfigParser()
    highlightConfig = dict()
    highlightConfig['productName'] = '0'
    highlightConfig['productVersion'] = '0'
    highlightConfig['companyName'] = '0'
    highlightConfig['fileDescription'] = '0'
    highlightConfig['originalFilename'] = '0'
    highlightConfig['fileVersionLabel'] = '0'
    highlightConfig['fileVersionNumber'] = '0'
    try:
        config.read(r'config.ini')
        for item in config.items('HIGHLIGHT'):
            if item[0] == 'productname':
                highlightConfig['productName'] = item[1]
            elif item[0] == 'productversion':
                highlightConfig['productVersion'] = item[1]
            elif item[0] == 'companyname':
                highlightConfig['companyName'] = item[1]
            elif item[0] == 'filedescription':
                highlightConfig['fileDescription'] = item[1]
            elif item[0] == 'originalfilename':
                highlightConfig['originalFilename'] = item[1]
            elif item[0] == 'fileversionlabel':
                highlightConfig['fileVersionLabel'] = item[1]
            elif item[0] == 'fileversionnumber':
                highlightConfig['fileVersionNumber'] = item[1]
            else: pass
    except Exception: pass
    return highlightConfig
    
def parseValidateConfig():
    config = ConfigParser()
    validateConfig = dict()
    validateConfig['productName'] = '0'
    validateConfig['productVersion'] = '0'
    validateConfig['companyName'] = '0'
    validateConfig['fileDescription'] = '0'
    validateConfig['originalFilename'] = '0'
    validateConfig['fileVersionLabel'] = '0'
    validateConfig['fileVersionNumber'] = '0'
    try:
        config.read(r'config.ini')
        for item in config.items('CONFIG'):
            if item[0] == 'productname':
                validateConfig['productName'] = item[1]
            elif item[0] == 'productversion':
                validateConfig['productVersion'] = item[1]
            elif item[0] == 'companyname':
                validateConfig['companyName'] = item[1]
            elif item[0] == 'filedescription':
                validateConfig['fileDescription'] = item[1]
            elif item[0] == 'originalfilename':
                validateConfig['originalFilename'] = item[1]
            elif item[0] == 'fileversionlabel':
                validateConfig['fileVersionLabel'] = item[1]
            elif item[0] == 'fileversionnumber':
                validateConfig['fileVersionNumber'] = item[1]
            else: pass
    except Exception: pass
    return validateConfig

def getFileName(file):
    "Split file path. Get file name."
    index = file.path.rindex('\\')
    return file.path[index+1:]
        
def generateProcessTree(processList):      
    "Add process root and children property." 
    
    # Find roots and children.
    hasChildFlag = False
    for i in range(0, len(processList)):
        for j in range(0, len(processList)):
            if i == j: continue
            if processList[i].parentPid == processList[j].pid:
                hasChildFlag = True
            if processList[i].pid == processList[j].parentPid:
                processList[i].children.append(processList[j])
        if hasChildFlag: 
            hasChildFlag = False
            continue
        processList[i].root = True
    return processList
    
#    # Find children.
#    for i in range(0, len(processList)):
#        for j in range(0, len(processList)):
#            if i == j: continue
#            if processList[j].parentPid == processList[i].pid:
#                processList[i].children.append(processList[j].parentPid)
                
def getRoots(processList):
    "Get all roots in processList."
    roots = []
    for process in processList:
        if process.root:
            roots.append(process)
    return roots

#def generateProcessDict(processList):
#    "Convert processList to processDict."
#    processDict = {}
#    for process in processList:
#        processDict[process.pid] = process
#    return processDict




