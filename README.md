# file_transfer_with_checkpoint

This is a python script to allow users to transfer files from a source server to a destination server with the ability to resume the upload via checkpointing.

Below are the steps (also outlined in the Jupyter Notebook)

## STEP 1: Create list of unique folders on the destination machine corresponding to the files being transferred

#### get list of unique folders on source machine
!find . -name "*" |  awk -F'/' '{for (i=1; i<NF; i++) printf("%s/", $i);print "\n"}' | sort | uniq > unique_dirs.txt

#### create identical directory structure on the destination machine
!cat unique_dirs.txt | xargs mkdir -p

## STEP 2: Get list of all files to be copied from the source machine, also create an initial empty checkpoint file

!find . -name "*" |  awk -F'/' '{for (i=1; i<NF; i++) printf("%s/", $i);print "\n"} > filelist.txt
!touch checkpoint.txt 

## STEP3: Invoke the command to do the file transfers

Syntax:  python transfer_files.py <keyfile> <destination location> <source directory>

where,

keyfile - PEM file used for the file transfer
destination location - is the full path including server address to location on the remote server where the file should be moved. This will be the path that will be appended to the path in fileslist.txt to get the full destination path.
source directory - location of directory of source files. This is the path that will be appended to the path in fileslist.txt to get the full source path.

Example:

python transfer_files.py ~/testkey.pem ubuntu@11.111.112.10:/media/vol /Volumes/XYZ
