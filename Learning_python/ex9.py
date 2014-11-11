# define variables
# \n denotes new line
# \t denotes tab
# play around with strings
days = "Mon\n\t Tue\n Wed\n Thu\n Fri\n Sat\n Sun"
months = "Jan\n'Feb'\nMar\nApr\nMay\nJun\nJul\nAug"


print "Here are the days: ", days
print "Here are the months: ", months

# looks like double quotes allow for indentation without the use of \n
print """
There's something going on here.
\tWith the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want,
or 5,
or 6.

d
"""
