import os, datetime, shutil, sys, time, urllib.request 

path = "c:\\temp\\" # This code defines the path and stores it in the variable 'dirs'
dirs = filter(os.path.isdir, os.listdir ( path )) # Saves a list of the directories in the defined directory in a variable

file_list = []
for i in dirs:
    a = os.stat(os.path.join(path,i)) #os.stat returns file attributes about an inode. os.path.join joins one or more path components
    file_list.append([time.ctime(a.st_ctime)]) #time of most recent metadata change on Unix, or the time of creation on Windows)

newpath = (os.path.join(path,i))

for filename in os.listdir(newpath):
    if filename.endswith('.txt'):
	    dest_path = "c:\\temp2\\" # This code defines the destination path of downloaded file
shutil.move(newpath, dest_path)
		
# References:
#dirs = os.listdir( path ) # Saves a list of the files and directories in the defined directory in a variable		
#today = datetime.datetime.now().isoformat() # Grabs the current time
#file_time = datetime.datetime.fromtimestamp(os.path.getmtime( path )) # Grabs the time stamp on the main directory

##for i in dirs: # Starts looping through each file in the directory
##    print(file_time, i) # Displays each time stamp on the directory and the file name on the screen
##file_list.append([i,time.ctime(a.st_atime),time.ctime(a.st_ctime)]) # [file,most_recent_access,created]
#os.chdir( newpath ) 
#urllib.request.urlretrieve(url, "test.txt") # May be needed for URL

# ----------------------------------------------

# Start test.py

#import os
#import urllib.request

## directory = 'http://adict.bcn.rd.hpicorp.net:88/cim/fmw/ipg-atlas_bcd/vulcan/wrl60-haswell_x86_64-dbg/'

# This code lists the files in the specified directory
#directory = 'c:\\temp\\'
#dirs = os.listdir( directory )
#for file in dirs:
#   print(file)

# This code works to retrieve the file but must be manually set
#url = 'http://adict.bcn.rd.hpicorp.net:88/cim/fmw/ipg-atlas_bcd/vulcan/wrl60-haswell_x86_64-dbg/179356/vulcan-trunk-R179356-170907.unsigned.fmw'

#print ("Retrieving file")
#urllib.request.urlretrieve(url, "vulcan-trunk-R179356-170907.unsigned.fmw")

# End test.py

# ----------------------------------------------------

# -----------------------------------------

# Start schedule.python

##!/usr/bin/python
#import profile as profile
#import urllib.request

#from datetime import datetime
#from threading import Timer

#x=datetime.today()
#y=x.replace(day=x.day+1, hour=15, minute=21, second=0, microsecond=0)

#delta_t=y-x
#secs=delta_t.seconds+1

#def testUrllib():
#	getFmwFile = urllib.request.URLopener()
#	getFmwFile.retrieve("http://adict.bcn.rd.hpicorp.net:88/cim/fmw/ipg-atlas_bcd/vulcan/wrl60-haswell_x86_64-dbg/179113/vulcan-trunk-R179113-170907.unsigned.fmw" , "vulcan-trunk-R179113-170907.unsigned.fmw")
	
#	getShFile = urllib.request.URLopener()
#	getShFile.retrieve("http://adict.bcn.rd.hpicorp.net:88/cim/fmw/ipg-atlas_bcd/vulcan/wrl60-haswell_x86_64-dbg/179113/vulcan-trunk-R179113-170907.sh" , "vulcan-trunk-R179113-170907.sh")
	
#t = Timer(secs, testUrllib)
#t.start()

# End schedule.py

# -------------------------------------------