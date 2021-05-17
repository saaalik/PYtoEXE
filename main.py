import os
import sys

mypath = os.getcwd()
pyScript = sys.argv[0]

"""
myprojects = os.listdir()
for project in myprojects:
    os.chdir(mypath)
    if os.path.isfile(project):
        continue
    print()
    print(project)
    thisPath = os.path.join(mypath,project)
    thisPath = os.path.join(thisPath,"Main_Application")
    if os.getcwd()==thisPath:
        pass
    else:
        os.chdir(thisPath)
    myfiles = os.listdir()
    isWindowed = any(True if file.endswith(".config") else False for file in myfiles)
    for file in myfiles:
        if file.endswith(".py") and isWindowed:
            os.system("pyinstaller --onefile "+os.path.join(thisPath,file))
        elif file.endswith(".py"):
            os.system("pyinstaller --onefile -w "+os.path.join(thisPath,file))
"""

for (root,dirs,files) in os.walk(mypath, topdown=True):
    os.chdir(root)
    print(root)
    print(dirs)
    print(files)

    for file in files:
        if file==pyScript:
            continue
        if file.endswith(".py"):
            os.system("pyinstaller --onefile "+os.path.join(root,file))
    print ('--------------------------------')
    os.chdir(mypath)
