'''
Created on 2012-7-6

@author: Vigi
'''
from distutils.core import setup
from glob import glob
import py2exe
import sys

sys.path.append(r"C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT")
data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]
includes = ["encodings", "encodings.*"]
options = {"py2exe":
            {   "compressed": 1,
                "optimize": 2,
                "includes": includes,
                "bundle_files": 1
            }
          }
setup(version = "1.2.0",
      description = "Auto ATTK Analysis Tool",
      name = "Auto ATTK Analysis Tool",
      author = "Vigi",
      options = options,
      data_files=data_files,
      zipfile = None,
      console=['main.py'])