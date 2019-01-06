# TODO 1: Update the file name
infile = open("dictionary.txt", "r")
line = infile.readline()

# The while loop that runs throgh the finger prints
while line:
    line = line[0:len(line)-1]
    for i in range (1,len(line)+1):
        for j in range (len(line)-i+1):
            print(line[j:i+j])
    line = infile.readline()
   
# TODO 2: Make sure to add one character at the end of the text file