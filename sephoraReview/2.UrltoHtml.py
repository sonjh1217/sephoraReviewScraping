# -*- coding: utf-8 -*-
"""
Created on Thu May 01 11:23:53 2014

@author: user
"""
import urllib

def saveFile(link,outfile):

    htmlFile = urllib.urlopen(link)
    

    fout=open(outfile, "w")
 
    for line in htmlFile.read():
        fout.write(line)
    fout.close()

url = open("C:/Users/user/Documents/NYU/FCS/finalProject/sephora_reviewurl.txt", "r")
for line in url:
    rootUrl = line;
    currentProduct = rootUrl.split("/")[-2]
 
    path = "C:/Users/user/Documents/NYU/FCS/finalProject/"

    id = line.split("/")
    outFile = path+id[4]+"review.html";

    saveFile(rootUrl, outFile)