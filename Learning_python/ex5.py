from pprint import pprint as pp

## Define variables
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
heightcm = height*2.54
weight = 180.0 # lbs
weightkg = weight*2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Print variables
# %d is to introduce a digit variable in a print statement
# %s is for string
# %f is for floats
# notice that there is a % variable after the print
print "Let's talk about %s." %name
print "He's %d inches tall." % height
print "He's %f cm tall." % heightcm
print "He's %d pounds heavy." %   weight
print "He's %d kilograms heavy." %   weightkg
print "Actually that's not too heavy."
# if you want to call multiple variables you need to have % (variable1, variable2)
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
# you can use + sign instead of , when defining variables in tuple
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

# dan's advanced trick
# temporary variables are denoted by {} which are defined after the print statement
# locals() inputs variables from local environment
print "If I add {age}, {weight}, and {height}, I get {weight}".format(**locals())
# alternatively you can define variables in format()
print "If I add {age}, {weight}, and {height}, I get {weight}".format(age=1,weight=2,height=3)
