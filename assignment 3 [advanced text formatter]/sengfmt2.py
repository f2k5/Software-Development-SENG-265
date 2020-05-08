#!/opt/local/bin/python

import sys
import fileinput
#from formatter import Formatter
from formatter import *

def main():
	new = Formatter()
	#print("Called from sengfmt2.py:")
	new.get_lines()




if __name__ == "__main__":
    main()
