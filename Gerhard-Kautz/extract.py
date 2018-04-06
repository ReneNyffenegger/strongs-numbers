#!/usr/bin/python

import os
import glob
import re

html_dir='../github.bibel/strong/dict/'

html_files = glob.glob(html_dir+'G*.html')
html_files.sort(key = lambda x: int( re.search('\d+', x)[0]  ))

f_de = open('translation-de.txt', 'w')
for html in html_files:
    with open(html) as f_html:
         for l_html in f_html:
             m = re.search('<h2>(.*)</h2>(.*)', l_html)
             if m:
                strongs = os.path.basename(html[:-7]) # remove '_1.html'
                strongs = int(strongs[1:])
                f_de.write('{:d}\t{:s}\t{:s}\n'.format(strongs, m[1], m[2]))
