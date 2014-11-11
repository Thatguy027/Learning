from sys import argv

script, filename = argv

# opens file indicated by first argument after script
# then txt.read() reads the file
txt = open(filename)
# this can be assigned to a variable
tt = txt.read()
# which can be printed
print tt
txt.close()

txt1 = open(filename)
print "Here's your file {filename}:".format(**locals())
print txt1.read()
txt1.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
