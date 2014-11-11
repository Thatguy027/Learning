tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."


backslash_cat1 = "I'm \\ a \\ cat."
backslash_cat3 = "I'm \ a \\ cat."


fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fat_cat1 = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat1
print backslash_cat3
print fat_cat
print fat_cat1

# solving quote within quote issues using escape characters
print "I am 6'2\" tall."  # escape double-quote inside string
print 'I am 6\'2" tall.'  # escape single-quote inside string

# notice the difference between %r and %s
for i in ["/","-","|","\\", "\n", "\tpopo","|"]:
    print "%s\r" % i

for i in ["/","-","|","\\", "\n", "\tpopo","|"]:
    print "%r\r" % i
