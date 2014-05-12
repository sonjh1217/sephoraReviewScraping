# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 10:55:48 2014

@author: user
"""



import urllib
import re

 
def extractproductid(line):
   
    productid = re.search('data-product_id="P[0-9]+',line)
   
    if(productid): 
       
        return productid        
  
    
   
      


rootUrl  = "http://www.sephora.com/contentStore/mediaContentTemplate.jsp?mediaId=14300062&icid2=HomePage_QuickLink_Bestsellers_04.15.14_Link";
htmlFile = urllib.urlopen(rootUrl)


outFile = "C:/Users/user/Documents/NYU/FCS/finalProject/sephora_reviewurl.txt";


fout=open(outFile, "w")
 
for line in htmlFile:
    if "data-product_id=\"P" in line:
        productid = extractproductid(line)
        if(productid != None):
            onlyproductid = productid.group().split("\"")
           #print"inside:","http://reviews.sephora.com/8723Illuminate/"+onlyproductid[1]+"/reviews.htm?format=noscript"
            fout.write("http://reviews.sephora.com/8723Illuminate/"+onlyproductid[1]+"/reviews.htm?format=noscript"+"\n");
fout.close()

    