#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Python code by Marcio to do the convertion of OBJ files meshes generated 
from Google Sketchup to become simple arrays of Y heights to be used in JME
"""

import sys
import os, glob
import xml.dom.minidom

from xml.dom.minidom import parse, parseString, getDOMImplementation
from ConfigParser import ConfigParser

path    = '.'

def main():

    vertexfile = sys.argv[1]

    f = open(vertexfile, 'r+')
    for line in f: 
        #print s[0] + "-" + s[1] +"-" + s[2] + "-" + s[3]  
        if line[0] == "v" and line[1] ==" ": 
	   chunk = line.split(" ")
           if float(chunk[1])<10: 
              chunk[1]= "0"+chunk[1]
           if float(chunk[1])<100: 
              chunk[1]= "0"+chunk[1]
           if float(chunk[3])<10: 
              chunk[3]= "0"+chunk[3]
           if float(chunk[3])<100: 
              chunk[3]= "0"+chunk[3]
           new =  "v "+chunk[1]+" "+ chunk[2] + " " + chunk[3] 
           new2 = new.strip("\n\r");
           print new2

    f.close()
if __name__ == '__main__':
	main()
