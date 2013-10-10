'''
Created on 2012-7-4

@author: Vigi
'''
from handler import xmlFileParse, writeToHTML, createIndexHtml
from autorun import Autorun
from process import Process
from service import Service
from driver import Drivers
from highsuspect import HighSuspecter
import webbrowser
import sys

reload(sys)
sys.setdefaultencoding("utf-8") #@UndefinedVariable

def print_help():
    print("The available commands are:")
    print("all   : All commands include (H)ighsuspect, (A)utorun, (P)rocess, (S)ervice, (D)river.")
    print("h(H)  : Only generate highsuspect.html. This is default option.")
    print("a(A)  : Generate both highsuspect.html and autorun.html.")
    print("s(S)  : Generate highsuspect.html, autorun.html and service.html")
    print("d(D)  : Generate highsuspect.html, autorun.html and drivers.html")
    print("p(P)  : Generate both highsuspect.html and process.html")
    print("quit  : exit program.")
    print("?     : Prints this message.")

def enter_command():
    cmd = raw_input("Enter command (? for help): ")
    cmd = cmd.strip().lower()
    return cmd

def main():
    while True:
        doFileFlag = False
        doProcessFlag = False
        doAutorunFlag = False
        doServiceFlag = False
        doDriversFlag = False
        cmd = enter_command()
        if cmd == '':
            continue
        if cmd == '?':
            print_help()
        elif cmd == 'quit':
            return
        elif cmd == 'all':
            doFileFlag = True
            doProcessFlag = True
            doAutorunFlag = True
            doServiceFlag = True
            doDriversFlag = True
        else:
            wrongFlag = False
            for i in range(0, len(cmd)):
                if cmd[i] not in ('h','a','s','d','p'): 
                    wrongFlag = True
                    break
            if wrongFlag:
                continue
            doFileFlag = True
            if 'p' in cmd:
                doProcessFlag = True
            if 'a' or 's' or 'd' in cmd:
                doAutorunFlag = True
            if 's' in cmd:
                doServiceFlag = True
            if 'd' in cmd:
                doDriversFlag = True
        if doFileFlag:
            try:
                xmlFile = r'assessreport.xml'
                print("Starting parsing assessreport.xml...")
                computerName, fileList, autorunList, processList = xmlFileParse(xmlFile)
                print("Parsing is finished.")
            except:
                print("Sorry, parsing is failed. The program will exit.")
                raw_input("Exit program.")
                return
            if doProcessFlag:
                try:
                    createIndexHtml(computerName)
                    print("Starting collecting process info...")
                    process = Process(r'.\result\process.html', processList)
                    process.toHtml(fileList)
                    print("Collecting process info is finished.")
                except:
                    print("Sorry, collecting process info is failed. The program will exit.")
                    raw_input("Exit program.")
                    return
            if doAutorunFlag:
                try:
                    print("Starting collecting autorun info...")
                    autorun = Autorun(r'.\result\autorun.html', autorunList)
                    autorun.toHtml(fileList)
                    print("Collecting autorun info is finished.")
                except:
                    print("Sorry, collecting autorun info is failed. The program will exit.")
                    raw_input("Exit program.")
                    return
            if doServiceFlag:
                try:
                    print("Starting collecting service info...")
                    service = Service(r'.\result\service.html', autorunList)
                    service.toHtml(fileList)
                    print("Collecting service info is finished.")
                except:
                    print("Sorry, collecting service info is failed. The program will exit.")
                    raw_input("Exit program.")
                    return
            if doDriversFlag:
                try:
                    print("Starting collecting drivers info...")
                    drivers = Drivers(r'.\result\drivers.html', autorunList)
                    drivers.toHtml(fileList)
                    print("Collecting drivers info is finished.")
                except:
                    print("Sorry, collecting drivers info is failed. The program will exit.")
                    raw_input("Exit program.")
                    return
            print("Starting creating files...")
            for file in fileList.values():
                writeToHTML(file)
            HighSuspecter(r'.\result\highsuspect.html', fileList).toHtml()
            print("Files have been created.")
            open = raw_input("The program will open your default web browser to open index.html. If you don't want. Please enter (n/N): ")
            open = open.strip().lower()
            if open == 'n': return
            else: 
                webbrowser.open(r'index.html')
                return
            
if __name__ == '__main__': main()