import os
import sys  
from distutils.dir_util import copy_tree

print("Inicio do programalho")

if len(sys.argv) < 3:
    print("Usage listdir sourceDir backupDir [onlyNotFound] [copyMissingDir]")
    sys.exit()
else:
    originPath = sys.argv[1]
    backupPath = sys.argv[2]
    if len(sys.argv) >= 4:
        onlyNotFound = sys.argv[3]
    else:
        onlyNotFound = ''
    if len(sys.argv) >= 5:
        copyMissingDir = sys.argv[4]
    else:
        copyMissingDir = ''

print("Origin directory: ",os.path.join(originPath))
print("Backup directory: ",os.path.join(backupPath))
print("Only Not Found param: ",onlyNotFound)
print("Copy Missing Dir param: ",copyMissingDir)
print("-----------------")


with os.scandir(originPath) as it:
    # Iterates thru origin path
    for entry in it:
        # check only for directories
        if entry.is_dir():
            orgDir = os.path.join(originPath, entry.name)
            bkpDir = os.path.join(backupPath, entry.name)
            if (os.path.exists(bkpDir)):
                backupDirNotFound = False
                if onlyNotFound != 'onlyNotFound':
                    print(orgDir, bkpDir, "OK")
            else:
                backupDirNotFound = True
                print(orgDir, bkpDir, "Not Found in backup")
            if backupDirNotFound and copyMissingDir == 'copyMissingDir':
                print("copying...")
                copy_tree(orgDir, bkpDir)
            

print("Fim do programalho")