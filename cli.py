import sys
from helperFunctions import *

def updateCli(the):
    for idx, arg in enumerate(sys.argv):
        for key, value in the.items():
            if((arg == "--" + key) or (arg == "-" + key[0:1])):
                the[key] = coerce(sys.argv[idx+1])
