#!/usr/bin/env python
#-*- coding : utf-8 -*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %r to %r..." % (from_file, to_file)

in_data = open(from_file).read()

#print "The input file is %d bytes long." % len(in_data)

#print "Does the output file exists?", exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alright, all done."

out_file.close()

