
# Original script by:
# Android file sorter for illustrator exports
# By: Jorge Bautista <jorgebautista@gmail.com>
# This utility allows you to arrange the exported resources from illustrator for android 
# application development. The script removes the extra information on the file names and
# put each file on the correct folder.

# Updated version by:
# Roman Kuleshov
# March 8, 2018
#   CHANGES
# + simplified code
# + add easy way to change the prefix
# + don't make unnecessary folders

import glob, re, os
from shutil import move,copy2

folderprefix = 'drawable-'

# array with the sizes needed to clasify the different files
sizes = ['xxxhdpi','xxhdpi','xhdpi','hdpi','mdpi','ldpi']    

#loop to check all the files in the folder
for filename in glob.glob('*.png'):

	# loop through the different sizes and clasify the file
    for size in sizes:
        
        # Check if the file name contains that extension        
        if size in filename:
            
            # dst will have our destination folder hdpi, xhdpi etc.
            foldername = folderprefix + size

            # new name for our file (without the xxxhdpi, xxhdpi, etc)
            filename_new = filename.replace(size, '')

            # create folder (if we need to)
            if not os.path.exists(foldername):
                os.makedirs(foldername)

            # if the destination file exists, it will be deleted
            if os.path.exists(os.path.join(foldername, filename_new)):                
                os.remove(os.path.join(foldername, filename_new))
                print ('Deleting stale copy of "{}"'.format(os.path.join(foldername, filename_new)))

            print('Moving "{}" to "{}"'.format(filename, foldername))
            
            # move the new file to the destination folder
            move(filename, os.path.join(foldername, filename_new) ,copy_function=copy2)
            
            # we exit to continue with the next file
            break
