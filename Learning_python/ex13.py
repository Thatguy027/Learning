# from the sys module you want to import the argv function
from sys import argv

# now when executing the script you need to input 3 additional arugments
# these arguments get assigned to variables that are indicated here
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
