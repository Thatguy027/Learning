# copy existing file into another file
# arg1 - existing file name
# arg2 - new file name

# load modules
from sys import argv
from os.path import exists

# define variables by arguments
script, original, copy = argv

print "Copying from {original} to {copy}".format(**locals())

# simultaneously opens and reads text in the original argument
original1 = open(original).read()
#indata = in_file.read()

print original1

# determines the length of text
print "The input file is %d bytes long" % len(original1)

# determines if the file you want to create already exists
print "Does the output file exist? %r" % exists(copy)
# quit program if you do not want to overwrite
print "Ready, hit RETURN to continue, CTRL-C to abort."
# if return is enter it executes rest of code.
raw_input()

out_file = open(copy, 'w')
out_file.write(original1)

print "Alright, all done."


out_file.close()
