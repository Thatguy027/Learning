from sys import argv

script, string = argv

DNA = open(string).read()

DNA = DNA.split("\n")

print DNA

seq = DNA[0]
subseq = DNA[1]

# Start with this value.
location = -1

# Loop while true.
while True:
    # Advance location by 1.
    location = seq.find(subseq, location +1)
    # Break if not found.
    if location == -1: break

    # Display result.
    print(location)+1
