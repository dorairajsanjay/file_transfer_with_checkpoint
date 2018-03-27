
## STEP 3: Copy files over with checkpointing support. 
## Checkpointing remembers the last file transferred so that a failed transfer can be resumed

import sys
import subprocess

privateKey = sys.argv[1]
serverInfo = sys.argv[2]
sourceDir = sys.argv[3]

#privateKey = "~/sanjayd_keypair.pem"
#serverInfo = "ubuntu@75.101.192.90:/media/vol"
#sourceDir = "/Volumes/LDC2012T21"

print("Transferring files using %s and %s. Source dir:%s" %  (privateKey, serverInfo,sourceDir))

fList = open("fileslist.txt")
fCheckpoint = open("checkpoint.txt")
lastFile = fCheckpoint.read().strip()
fCheckpoint.close()

checkPointFound = False
for file in fList:
        
    file = file.strip()
    
    #print "Last File:%s,len(lastFile):%d" % (lastFile,len(lastFile))
    #print "File:%s,len(file):%d" % (file,len(file))

    # check to see if we are at directory
    fileName = file.split("/")[-1]
    if "." not in fileName:
        print "Skipping directory:%s" % file
        continue
    
    if checkPointFound == False:
        if lastFile == "":
            print "Empty checkpoint file."
            checkPointFound = True
        elif lastFile != file:
            print "Skipping file. Checkpoint not reached"
            continue
        else:
            print "Checkpoint reached. Starting to process files"
            checkPointFound = True
    
    # add file to checkpoint
    command = "scp -i " + privateKey + " " + sourceDir + file + " " + serverInfo + file
    
    # print command
    subprocess.call(command,shell=True)
    
    # add to checkpoint
    fCheckpoint = open("checkpoint.txt","w")
    fCheckpoint.write(file)
    fCheckpoint.close()


    