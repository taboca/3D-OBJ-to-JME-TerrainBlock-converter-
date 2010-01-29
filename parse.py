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

    listVertex = {}
    vertexfile = sys.argv[1]

    f = open(vertexfile, 'r+')
    for line in f: 
        s = line.split(" ")  
        #print s[0] + "-" + s[1] +"-" + s[2] + "-" + s[3]  
        listVertex[s[3].strip("\n\r")+" "+s[1]]=s[1]+" "+s[2]+" "+s[3]
    f.close()
    
    ss = listVertex.keys()
    ss.sort()
 
    listXVertex = {} 

    for key in ss: 
        s = listVertex[key].split(" ")
        listXVertex[s[0]+" "+s[2].strip("\n\r")]=s[0]+" "+s[1]+" "+s[2]

    xx = listXVertex.keys()
    xx.sort()
  
    ii = 0 
    jj = 0 
    currX = "0.000000"
    for key in xx: 
	curr = listXVertex[key].split(" ")
	#print curr[0] + " " + curr[1] + " " + curr[2] 
 	if currX == curr[0]:
           ii=ii+1
           print ""+curr[1]+"f,",
        else: 
           currX = curr[0]
           jj=jj+1
	   ii=0 
           print "\n"+curr[1]+"f,",
        
    #print "Total is cols = " + str(ii) + " and rows = " + str(jj)
 

if __name__ == '__main__':
	main()
