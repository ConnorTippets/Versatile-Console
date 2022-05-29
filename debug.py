from sys import argv as args
import sys
debug = False
debug_log = []
try:
    if args[2] == "1":
        debug = True
except:
    debug = False
