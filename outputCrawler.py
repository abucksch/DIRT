'''
outputCrawler.py

module to collect the results generated by runOnFolder.py

The code is free for non-commercial use.
Please contact the author for commercial use.

Please cite the DIRT Paper if you use the code for your scientific project.

Bucksch et al., 2014 "Image-based high-throughput field phenotyping of crop roots", Plant Physiology

-------------------------------------------------------------------------------------------
Author: Alexander Bucksch
School of Biology and Interactive computing
Georgia Institute of Technology

Mail: bucksch@gatech.edu
Web: http://www.bucksch.nl
-------------------------------------------------------------------------------------------

Copyright (c) 2014 Alexander Bucksch
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

  * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

  * Redistributions in binary form must reproduce the above
    copyright notice, this list of conditions and the following
    disclaimer in the documentation and/or other materials provided
    with the distribution.

  * Neither the name of the DIRT Developers nor the names of its
    contributors may be used to endorse or promote products derived
    from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''

import os
import csv

def combineOutput(dir):
    filewriter=None
    ''' save file'''
    
    files=os.listdir(dir)
    ''' remove the old output '''
    try:
        os.remove(dir+'outputAll.csv')
    except:
        pass
    try:
        os.remove(dir+'crawler.out')
    except:
        pass
    files=os.listdir(dir)
    directories=[]
    for i in files:
        if os.path.isdir(dir+i)==True:
            directories.append(i)
            
    ''' copy header'''
    with open (dir+directories[0]+'/output.csv','U') as csvfile:
        filedata= csv.reader(csvfile)
        rows=filedata.next()
    
        with open(dir+'outputAll.csv', 'wb') as f:
            filewriter=csv.writer(f)
            filewriter.writerow(rows)
    ''' append data'''
    countOK=0
    countBAD=0
    badFolder=[]
    for f in directories:
        try:
            with open (dir+f+'/output.csv','U') as csvfile:
                countOK+=1
                filedata= csv.reader(csvfile)
                with open(dir+'outputAll.csv', 'ab') as f:
                    filewriter=csv.writer(f)
                    rows=filedata.next()
                    rows=filedata.next()
                    filewriter.writerow(rows)
        except:
            countBAD+=1
            badFolder.append(f)
            # Open a file
    fo = open(dir+"crawler.out", "wb")
    fo.write( str(countOK)+' images are processed and '+str(countBAD)+' images failed: \n'+str(badFolder))
    # Close opend file
    fo.close()
    print str(countOK)+' images are processed and '+str(countBAD)+' images failed: \n'+str(badFolder)
            
