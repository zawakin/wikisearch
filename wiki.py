# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 18:26:24 2015

@author: Miyake Yuki
"""
import mwclient
from pprint import pprint
import json


site = mwclient.Site(("https",'ja.wikipedia.org'))

bllist = ["ゴンペルツ関数"]
llist = ["根粒菌"]
bldata = []
ldata = []
bldata.append([bllist[0],])
ldata.append([llist[0],])

howmanyreq = 0

nextindex = 0
for d in range(0,2):
    print "depth",d
    n = len(bllist)
    for i in range(nextindex,n):
        data = site.api("query",list="backlinks",bltitle=bllist[i],bllimit="300")
        howmanyreq += 1        
        try:        
            bllist.extend([t[u"title"].encode("utf-8") for t in data[u"query"][u"backlinks"]])
            for t in data[u"query"][u"backlinks"]:
                ss = t[u"title"].encode("utf-8");
                arr = [ss,]
                arr.extend(bldata[i])
                bldata.append(arr)
        except:
            print "error"
                        
            
    nextindex = n
    
print "link search"
nextindex = 0
for d in range(0,2):
    print "depth",d
    n = len(llist)
    for i in range(nextindex,n):
        data = site.api("query",prop="links",titles=llist[i],pllimit="max",indexpageids="")
        howmanyreq += 1        
        try:
            query = data[u"query"]
            pages = query[u"pages"]
            pageid = data[u"query"][u"pageids"]
            links = pages[pageid[0].encode("utf-8")][u"links"]
            llist.extend([t[u"title"].encode("utf-8") for t in links])
            for t in links:
                ss = t[u"title"].encode("utf-8");
                arr = [ss,]
                arr.extend(ldata[i])
                ldata.append(arr)
        except:
            print "error"
    nextindex = n

print len(bllist)
print len(llist)

for bli in range(0,len(bllist)):
    for li in range(0,len(llist)):
        if(bllist[bli]==llist[li]):
            ss = ""
            linkN = -1
            for ll in ldata[li][::-1]:
                ss = ss + "-" + ll + "-"
                linkN += 1
            
            for bb in bldata[bli][1:]:
                ss = ss + "=" + bb + "="
                linkN += 1
            ss = "({N})".format(N=linkN) + ss    
            print ss

print "howmanyreq = ",howmanyreq

#for b in bllist:
#    print b
#
#for l in llist:
#    print l
#    
#blset = set(bllist)
#lset = set(llist)
#
#intersection = blset.intersection(llist)
#
#print len(intersection)
#if(len(intersection)>0):
#    for i in intersection:
#        print i