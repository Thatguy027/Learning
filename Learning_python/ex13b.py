# from the sys module you want to import the argv function
from sys import argv

# now when executing the script you need to input 3 additional arugments
# these arguments get assigned to variables that are indicated here
script, first, second = argv

print "Why are you learning python?",
third = raw_input()

print "The script is called: {script}".format(**locals())
print "Your first variable is: {first}".format(**locals())
print "Your second variable is: {second}".format(**locals())
print "You are learning python, just {third}".format(**locals())

print """
The script is called: {script}
Your first variable is: {first}
Your second variable is: {second}
You are learning pythin, just {third}
""".format(**locals())
