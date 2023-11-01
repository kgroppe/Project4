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

userSpecifiedPath = raw_input("Path: ")
result = 