#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import os
import sys
import subprocess
import numpy as np
import nrrd

# some sample numpy data
nonBinaryPath = (sys.argv)[1]
#destPath = r'BinaryMasks'
#os.makedirs(destPath)
files = os.listdir(nonBinaryPath)
for file in files:
	infilename, extname = os.path.splitext(file)
	#print "Extenstion: ",extname
	if extname == '.nrrd':
		print "Reading file",infilename,extname
		readPath = nonBinaryPath + '/' + file
		readData, options = nrrd.read(readPath)
		binaryPath = infilename + '-bin' + extname
		binaryData = np.where(readData > 0,1,readData)
		nrrd.write(binaryPath,binaryData,options)

print "Done"