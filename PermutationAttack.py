from itertools import permutations

# TODO 1: Update the file name
infile = open("dictionary.txt", "r")
line = infile.readline()
while line:
    line = line[0:len(line)-1]

    # Get all permutations of the string in the line.
    perms = [''.join(p) for p in permutations(line)]
    for i in range (len(perms)):
        print(perms[i])
    line = infile.readline()
   
#TODO 2: Make sure to add one character random at the end of the text file
