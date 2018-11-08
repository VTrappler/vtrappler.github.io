# -*- coding: utf-8 -*-

import urllib
import re
import sys


            
def download_mp3(url, filename):
    page = urllib.urlopen(url).read()
    test = re.search(r"data-asset-source=(.)*\.mp3", page)
    mp3url = test.group(0)[19:];mp3url

    mp3link = urllib.URLopener()
    mp3link.retrieve(mp3url, filename + '.mp3')


with open('podcasts_to_download.txt', 'r') as file_to_down:
        for i,line in enumerate(file_to_down):
            print 'Link number ' + str(i)
            url,filename = line.split()
            download_mp3(url,filename)
