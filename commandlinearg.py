import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("-path", action="store", dest="logpath" )
parser.add_argument("-name", action="store", dest="logfilename" )
results = parser.parse_args()

if(results.logfilename == None):
    results.logfilename = "sessionLog.txt";


#check if file exist in this path
if os.path.isfile(results.logpath +  "/" + results.logfilename):
   print("File exists")
#else throw error
else :
   print("LOG FILE does not exist...")




