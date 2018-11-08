# enum.py
# Reads input file lines and creates git commits based on emails read from input
# When pushed to Github the commit history should show which user is connected to the supplied email
#
# Version: 1.0
# Author: antnks <antnks@users.noreply.github.com>
# License: public domain
#
# Usage: python enum.oy emails.txt
# Input file is one email per line
# Example:
#
# a@b.com
# c@d.com
#

import sys
import os
import time

branch = time.time()
print ("Creating a new branch...")
os.system ("git checkout master -b {}".format (branch))

print ("Opening input file {}".format(sys.argv[1]))
fe = open(sys.argv[1], "r")
line = fe.readline()
cnt = 1
while line:

	print ("Updating seed file...")
	fs = open ("seed.txt", "w")
	fs.write (str(cnt))
	fs.close()
	
	print ("Changing git repo author to {} {}".format(cnt, line.strip()))
	os.system ("git add seed.txt")
	os.system ("git config user.name {}".format(cnt))
	os.system ("git config user.email {}".format(line.strip()))
	
	print ("Commiting...")
	os.system ("git commit -a -m {}".format(cnt))
	
	line = fe.readline()
	cnt += 1

fe.close()

print ("Pushing to Github...")
os.system ("git push origin {}".format(branch))
