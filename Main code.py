import sys
import _NLTKQuery

print("Welcome to the NLTK Query Experimentation")
print("Please wait loading NLTK ...")

import _classNLTKQuery
oNLTK = _classNLTKQuery.classNLTKQuery()

print()
print("Input full path thame where intended corpus file or files are stored")
print("Note: You must enter a quoted string e.g. c:\\simpson\\")
print()

userSpecifiedPath = input("Path: ")
result = oNLTK.textCorpusInit(userSpecifiedPath)

if result == 'Success':
    menuSelection = -1
    while menuSelection != 0:
        if menuSelection != -1:
            print()
            s = input("Press Enter to Continue...")
        menuSelection = _NLTKQuery.getUserSelection()
        if menuSelection == 1:
            oNLTK.printCorpusLength()
        if menuSelection == 2:
            oNLTK.printTokensFound()
        