#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 14:17:18 2018

@author: Tyler Laird - tylerscottlaird@gmail.com
"""
#For batch downloading the tar bundles of IMG data which includes both annotation
#and fasta files.

#file is a .txt file containing IMG genome id's
#username is your IMG username/email entered as a string in quotes
#password is your IMG account password entered as a string in quotes

def IMG_download(file, username, password):
    import pycurl
    from io import BytesIO
    import urllib.parse
    import re
    import time
    import os
    
    with open(file) as f:
        IMG_ids = f.read().splitlines()
    
    not_in_Genome_Portal=[]
    for id in IMG_ids:
        available_files = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.VERBOSE,1)
        url='https://signon-old.jgi.doe.gov/signon/create'
        params={'login':username,'password':password}
        c.setopt(c.URL, url)
        c.setopt(c.POSTFIELDS, urllib.parse.urlencode(params).encode())
        c.setopt(c.COOKIEFILE, 'cookies')
        c.perform()
        id_to_search= 'IMG_'+str(id)
        print(id_to_search)
        c.setopt(c.URL,'https://genome.jgi.doe.gov/portal/ext-api/downloads/get-directory?organism='+id_to_search)
        c.setopt(c.COOKIEJAR, 'cookies')
        c.setopt(c.HTTPGET,1)
        #file_handle = open("file.xml","wb")
        c.setopt(c.WRITEDATA, available_files)
        #c.setopt(c.WRITEDATA, file_handle)
        c.perform()
        available_files
        body = available_files.getvalue()
        x=body.decode('iso-8859-1')
        print(x)
        if x == 'Portal does not exist':
            print(id_to_search+':'+ x)
            not_in_Genome_Portal.append(id_to_search)
        else:
            labels=re.findall('(?<=file label=")(.*?)(?=")',x)[0]
            labels=re.sub(' ','_',labels)
            labels=re.sub('\(|\)','',labels)
            labels=re.sub('-','_',labels)
            name=re.findall('(?<=filename=")(.*bundle\.tar\.gz)(?=" size)',x)
            urls=re.findall('(?<=url=")(.*bundle\.tar\.gz)(?=")',x)
            
            name_of_file=labels+'_'+str(name[0])
            print(name_of_file)
            
            file_to_download= 'https://genome.jgi.doe.gov/'+str(urls[0])
            
            c.setopt(c.URL,file_to_download)
            c.setopt(c.COOKIEJAR, 'cookies')
            c.setopt(c.HTTPGET,1)
            file_handle2 = open(name_of_file,"wb")
            c.setopt(c.WRITEDATA, file_handle2)
            c.perform()
            c.close()
            time.sleep(3)
        print('could not download '+str(len(not_in_Genome_Portal))+ ' Genome files:')
        print(not_in_Genome_Portal)
    

