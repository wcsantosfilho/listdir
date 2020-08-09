import os
import sys  
from distutils.file_util import copy_file

print("Inicio do programalho")

if len(sys.argv) < 3:
    print("Usage listfile sourceDir backupDir [onlyNotFound] [copyMissingFiles]")
    sys.exit()
else:
    originPath = sys.argv[1]
    backupPath = sys.argv[2]
    if len(sys.argv) >= 4:
        onlyNotFound = sys.argv[3]
    else:
        onlyNotFound = ''
    if len(sys.argv) >= 5:
        copyMissingFiles = sys.argv[4]
    else:
        copyMissingFiles = ''

print("Origin directory: ",os.path.join(originPath))
print("Backup directory: ",os.path.join(backupPath))
print("Only Not Found param: ",onlyNotFound)
print("Copy Missing File param: ",copyMissingFiles)
print("-----------------")


with os.scandir(originPath) as it:
    # Iterates thru origin path
    for directory in it:
        print("  ", "Dir:", directory.path)
        # check for directory
        if directory.is_dir():
            with os.scandir(directory.path) as itr:
                for entry in itr:
                    # check for files
                    if entry.is_file() and entry.name != 'Thumbs.db':
                        currentOriginPath = directory.path
                        currentBackupPath = os.path.join(backupPath, directory.name)
                        orgFile = os.path.join(currentOriginPath, entry.name)
                        bkpFile = os.path.join(currentBackupPath, entry.name)
                        if (os.path.exists(bkpFile)):
                            backupFileNotFound = False
                            if onlyNotFound != 'onlyNotFound':
                                print("  ", orgFile, bkpFile, "OK")
                        else:
                            backupFileNotFound = True
                            print("! ", orgFile, bkpFile, "Not Found in backup")
                        if backupFileNotFound and copyMissingFiles == 'copyMissingFiles':
                            print("copying...")
                            copy_file(orgFile, bkpFile)
            

print("Fim do programalho")