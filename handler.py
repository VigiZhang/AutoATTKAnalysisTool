# -*- UTF-8 -*-
'''
Created on 2012-7-4

@author: Vigi
'''
from module import File, Autorun, Process
from tools import getValue
from xml.etree.ElementTree import ElementTree
import os
import sys
import xml.etree

def xmlFileParse(xmlFile):
    "Use xml.etree parse XML doc."
    
    tree = ElementTree()
    tree.parse(open(xmlFile))
    systemInfo = tree.find('SystemInformation')
    computerName = getValue(systemInfo.findtext('ComputerName'))
    files = tree.find('Files')
    fileList = {}
    for file in files.iter('File'):
        f = File()
        f.id = file.get('Id')
        f.path = getValue(list(file)[0].text)
        f.size = getValue(list(file)[1].text)
        f.attributes = getValue(list(file)[2].text)
        f.signer = getValue(list(file)[3].text)
        f.productName = getValue(list(file)[4].text)
        f.productVersion = getValue(list(file)[5].text)
        f.companyName = getValue(list(file)[6].text)
        f.fileDescription = getValue(list(file)[7].text)
        f.originalFilename = getValue(list(file)[8].text)
        f.fileVersionLabel = getValue(list(file)[9].text)
        f.fileVersionNumber = getValue(list(file)[10].text)
        f.sha1 = getValue(list(file)[11].text)
        f.md5 = getValue(list(file)[12].text)
        f.rootkitInfo = getValue(list(file)[13].text)
        f.createTime = getValue(list(file)[14].text)
        f.lastAccessTime = getValue(list(file)[15].text)
        f.lastWriteTime = getValue(list(file)[16].text)
        fileList[f.id] = f
    autoruns = tree.find('Autoruns')
    autorunList = {}
    for autorun in autoruns.iter('Autorun'):
        a = Autorun()
        a.id = autorun.get('Id')
        a.fileId = getValue(list(autorun)[0].text)
        a.location = getValue(list(autorun)[1].text)
        a.itemName = getValue(list(autorun)[2].text)
        a.launchString = getValue(list(autorun)[3].text)
        a.groupId = getValue(list(autorun)[4].text)
        autorunList[a.id] = a
    processes = tree.find('Processes')
    processList = {}
    for process in processes.iter('Process'):
        p = Process()
        p.id = process.get('Id')
        p.pid = getValue(list(process)[0].text)
        p.parentPid = getValue(list(process)[1].text)
        p.commandLine = getValue(list(process)[2].text)
        p.userName = getValue(list(process)[3].text)
        p.fileId = getValue(list(process)[4].text)
        for i in range(0, len(list(process)[5])):
            p.dlls.append(getValue(list(process)[5][i][0].text))
        processList[p.id] = p
    
    return (computerName, fileList, autorunList, processList)
        
def generateFilesDir():
    "Generate .\files"
    
    try: 
        os.mkdir(r'.\result')
        os.mkdir(r'.\result\files')
    except: return False
    else: return True
    
def writeToHTML(file):    
    "Generate .\files\[fileid].html"
    
    with open(r'.\result\files\\' + file.id + r'.html', 'w') as f:
        f.write(r'<html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8" /><title>' + file.id + r'</title><style type="text/css">p{margin:5px;}a:link,a:hover,a:visited,a:active{text-decoration:none;}</style></head><body>')
        f.write(r'<p>Path: %s</p>' % file.path)
        f.write(r'<p>Size: %s</p>' % file.size)
        if file.attributes.strip() != 'A':
            f.write(r'<p>Attributes: <font color="red">%s</font></p>' % file.attributes)
        else:
            f.write(r'<p>Attributes: %s</p>' % file.attributes)
        f.write(r'<p>Signer: %s</p>' % file.signer)
        f.write(r'<p>ProductName: %s</p>' % file.productName)
        f.write(r'<p>ProductVersion: %s</p>' % file.productVersion)
        f.write(r'<p>CompanyName: %s</p>' % file.companyName)
        f.write(r'<p>FileDescription: %s</p>' % file.fileDescription)
        f.write(r'<p>OriginalFileName: %s</p>' % file.originalFilename)
        f.write(r'<p>FileVersionLabel: %s</p>' % file.fileVersionLabel)
        f.write(r'<p>FileVersionNumber: %s</p>' % file.fileVersionNumber)
        f.write(r'<p>Autorun: <font color="#ff0000">%s</font></p>' % file.autorun)
        f.write(r'<p>Service: <font color="#ff0000">%s</font></p>' % file.service)
        f.write(r'<p>Drivers: <font color="#ff0000">%s</font></p>' % file.drivers)
        f.write(r'<p>Process: ')
        for i in range(0, len(file.process)):
            f.write(r'<font color="#ff0000">' + file.process[i] + r'</font><br/>')
        f.write(r'</p>')
        f.write(r'<p>SHA1: %s</p>' % file.sha1)
        f.write(r'<p>MD5: %s</p>' % file.md5)
        f.write(r'<p>RootkitInfo: %s</p>' % file.rootkitInfo)
        f.write(r'<p>CreateTime: %s</p>' % file.createTime)
        f.write(r'<p>LastAccessTime: %s</p>' % file.lastAccessTime)
        f.write(r'<p>LastWriteTime: %s</p>' % file.lastWriteTime)
        f.write(r'</body></html>')
    
def createIndexHtml(computerName):
    "Create directory structure."
    
    generateFilesDir()
    with open(r'.\index.html', 'w') as f:
        f.write(r'<frameset rows="15%, 85%">')
        f.write(r'<frame name="top" src=".\result\top.html"></frame>')
        f.write(r'<frameset cols="45%, 55%">')
        f.write(r'<frame name="left" src=".\result\left.html"></frame>')
        f.write(r'<frame name="right" src=".\result\right.html"></frame>')
        f.write(r'</frameset>')
        f.write(r'</frameset>')
    with open(r'.\result\top.html', 'w') as f:
        f.write(r'<html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8" /><title>top</title><script language="javascript">function setUpper(obj){var links = document.getElementsByTagName("a");for(i=0;i<links.length;i++){links[i].innerHTML=links[i].id}obj.innerHTML=obj.name}</script></head><body>')
        f.write(r'<center><h1>Auto ATTK Analysis Tool</h1></center>')
        f.write(r'<h2><a id="HighSuspect" name="HIGHSUSPECT" href=".\highsuspect.html" target="left" onclick="setUpper(this)">HighSuspect</a>&nbsp;&nbsp;<a id="Autorun" name="AUTORUN" href=".\autorun.html" target="left" onclick="setUpper(this)">Autorun</a>&nbsp;&nbsp;<a id="Process" name="PROCESS" href=".\process.html" target="left" onclick="setUpper(this)">Process</a>&nbsp;&nbsp;<a id="Service" name="SERVICE" href=".\service.html" target="left" onclick="setUpper(this)">Service</a>&nbsp;&nbsp;<a id="Drivers" name="DRIVERS" href=".\drivers.html" target="left" onclick="setUpper(this)">Drivers</a><span style="float:right;padding-right:20px;">Computer Name: %s</span></h2>' % computerName)
        f.write(r'</body></html>')
    with open(r'.\result\left.html', 'w') as f:
        f.write(r'<html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8" /><title>left</title></head><body>')
        f.write(r'<h2>ResultList</h2>')
        f.write(r'</body></html>')
    with open(r'.\result\right.html', 'w') as f:
        f.write(r'<html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8" /><title>right</title></head><body>')
        f.write(r'<h2>FileDetails</h2>')
        f.write(r'</body></html>')
