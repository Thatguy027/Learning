x = "There are %f types of people." % round(float(10),5)
binary = "binary"
do_not = "don't"
y = "Those who know {binary} and those who {do_not}.".format(**locals())

print x
print y

# notice when using %r instead of %s it automatically inserts a '' for text because
# it realizes that it is inside another ""
print "I said: %r." % x
print "I said: %s." % x
print "I also said: '%s'." % y

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# connects the two strings w and e
# does not include an extra space
print w + e
# this does incluse a space between the strings
print w , e
