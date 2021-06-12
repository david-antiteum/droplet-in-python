#!/usr/bin/python

import sys

print( 'Number of arguments: {} arguments'.format( len(sys.argv) ) )
f = open("main.log", "a")
f.write( 'Argument List: {}'.format( str(sys.argv) ))
f.close()
