'''
#What steps would you take to rename a bunch of files
 #identify if there is a pattern for renaming
 #regex to identify specific files and then strip/logic to rename in place


'''

import os


# def listdir_nohidden(path):
#     # function built to work os.listdir while removing hidden files
#     # designed as a generator
#     for f in os.listdir(path):
#         if not f.startswith('.'):
#             yield f



def rename_files(path):
    '''
    #(1) get file names

    #(2) for each file, rename files
    '''

    #identify the files (ignoring hidden)
    files = filter(lambda f: not f.startswith('.'),os.listdir(path))

    #get current directory
    curDir = os.getcwd()

    #change directory to images
    os.chdir(r"/Users/wmj809/Desktop/Udacity_FUllStackNano/secretMessage/prankImageFiles")

    #change fileNames
    for fileName in files:
        oldFileName = fileName
        newFileName = fileName.translate(None,'0123456789')
        os.rename(oldFileName, newFileName)
        print oldFileName + " became " + newFileName

    #revert directory
    os.chdir(curDir)



rename_files(r'prankImageFiles')

