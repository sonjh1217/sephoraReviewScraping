# -*- coding: utf-8 -*-
"""
Created on Wed May  7 14:14:29 2014

@author: user
"""
import re
import glob

listOfFiles=  glob.glob("C:/Users/user/Documents/NYU/FCS/finalProject/*.html")
reviewData = []
products = []
productHasReview =[]
for file1 in listOfFiles:
    print "parsing file ",file1
    htmlFile = open(file1,"r")
    productDict  = {}  
    
    tmpId = file1.split("\\")[-1]
    productId = tmpId.split("review.html")[0];
    products.append(productDict)
    productDict['productId']=productId

    for line in htmlFile:
        if "<div id=\"BVRRCustomQuickTakeRatingSummaryOverallImage\" class=\"BVRRRatingNormalImage\"><img src=\"http://reviews.sephora.com/8723illuminate/" in line:
            tavgrating = re.search("<div id=\"BVRRCustomQuickTakeRatingSummaryOverallImage\" class=\"BVRRRatingNormalImage\"><img src=\"http://reviews.sephora.com/8723illuminate/[0-9_]*",line)
            tmavgrating = tavgrating.group().split("/")[-1]
            productDict['avgrating'] = tmavgrating.replace("_",".")

        if "BVRRDisplayContentReviewID_" in line:
            trvId = re.search("BVRRDisplayContentReviewID_[0-9]*",line)
            
            reviewId= trvId.group().split("_")[-1]
            rvDict = {}
            reviewData.append(rvDict)
            rvDict['helpfulVotes']="0"
            rvDict['totalVotes']="0"
            productHasReview.append(productId+","+reviewId)
            rvDict['reviewId'] = reviewId
            rvDict['rating']="Null"
            rvDict['badge'] = "Null"
            rvDict['location'] = "Null"
            rvDict['skin_type'] = "Null"
            rvDict['skin_tone'] = "Null"
            rvDict['eye_color'] = "Null"
            rvDict['age'] = "Null"
            rvDict['title'] = "Null"
            rvDict['cusId']="Null"
            rvDict['date']="Null"
      
            
        if "span class=\"BVRRNickname\"" in line:
            tcusId = re.search("span class=\"BVRRNickname\">[0-9a-zA-Z]*",line)
            cusId= tcusId.group().split(">")[-1]
            rvDict['cusId']= cusId
        if "BVRRReviewBadgeGraphic BVRR" in line:
            badge = re.search("BVRRReviewBadgeGraphic BVRR[A-Za-z]+",line)
            cbadge =  badge.group().split("BVRR")[2]   
            rvDict['badge'] = cbadge
        
        if "BVRRValue BVRRUserLocation" in line:
            location = re.search("BVRRValue BVRRUserLocation\">[a-zA-Z A-Z.]*",line)
            tmpl = location.group().split(">")[1]
            rvDict['location'] = tmpl
        
        if "ValueskinType" in line:
            skin_type = re.search("ValueskinType\">[A-Za-z]+",line)
            tmps = skin_type.group().split(">")[1]
            rvDict['skin_type'] = tmps

        if "ValueskinTone" in line:
            skin_tone = re.search("ValueskinTone\">[A-Za-z]+",line)
            tmpst = skin_tone.group().split(">")[1]
            rvDict['skin_tone'] = tmpst
        
        if "ValueeyeColor" in line:
            eye_color = re.search("ValueeyeColor\">[A-Za-z]+",line)
            tmpe = eye_color.group().split(">")
            rvDict['eye_color'] = tmpe[1]
        
        if "DataValueage" in line:
            age = re.search("DataValueage\">[0-9-]+",line)
            if(age):
                tmpa = age.group().split(">")
                rvDict['age'] = tmpa[1]

        if "class=\"BVImgOrSprite\"" in line and 'rvDict' in locals():
            rating = re.search("class=\"BVImgOrSprite\" alt=\"[0-5.]*",line)
            tmpAr = rating.group().split("=\"")
       
            rvDict['rating'] = tmpAr[2];
    
        if "</span><span class=\"BVRRValue BVRRReviewTitle\">" in line:
            titles = re.search("</span><span class=\"BVRRValue BVRRReviewTitle\">[A-Za-z._ -]+",line)
            if(titles):
                res =  titles.group().split("\">")
   
                rvDict['title'] = res[1]
            
        if "ReviewDate\">" in line:
            date = re.search("ReviewDate\">[0-9.]+",line)
            tmpdate = date.group().split(">")
            rvDict['date'] = tmpdate[1]
        
        if "Positive BVDI_FVLevel1\"><span class=\"BVDIValue BVDINumber\">" in line:
            helpfulVotes = re.search("Positive BVDI_FVLevel1\"><span class=\"BVDIValue BVDINumber\">[0-9]+",line);
            tmpAr = helpfulVotes.group().split(">")
               
            rvDict['helpfulVotes'] = tmpAr[2]
    
    
        if "Total BVDI_FVLevel1\"><span class=\"BVDIValue BVDINumber\">" in line:
            totalVotes = re.search("Total BVDI_FVLevel1\"><span class=\"BVDIValue BVDINumber\">[0-9]+",line);
            tmptV = totalVotes.group().split(">")
            rvDict['totalVotes'] = tmptV[2]
            
           
path = "C:/Users/user/Documents/NYU/FCS/finalProject/"
reviewsFile = open(path+"reviews.csv","w")

reviewsFile.write("Review Id, Customer Id, Badge, Location, Skin Type, Skin Tone, Eye Color, Age, rating, Title, Date, Helpful Votes, Total Votes")

productHasReviewsFile = open(path+"productHasReviews.csv","w")

productHasReviewsFile.write("productId,review Id")
productFile = open(path+"product.csv","w")

productFile.write("product,avgrating")


print"Writing reviews..."

for rvDict in reviewData:
    print rvDict
    reviewsFile.write("\n"+rvDict["reviewId"]+","+rvDict["cusId"]+","+rvDict["badge"]+","+rvDict["location"]+","+rvDict["skin_type"]+","+rvDict["skin_tone"]+","+rvDict["eye_color"]+","+rvDict["age"]+","+rvDict["rating"]+","+rvDict["title"]+","+rvDict["date"]+","+rvDict["helpfulVotes"]
    +","+rvDict["totalVotes"])

print "writing product has reviews..."  

for productReview in productHasReview:
    productHasReviewsFile.write("\n"+productReview)



for productDict in products:
    productFile.write("\n"+productDict['productId']+","+productDict['avgrating'])    


productFile.close()
productHasReviewsFile.close()
reviewsFile.close()
print "done"




