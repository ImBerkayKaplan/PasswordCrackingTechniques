import math

# The function to generate the number incrementing as a binary
def binarycode(number, length):
    result = [0]*length
    for i in range(length):
        result[i]= int(number%2)
        number=number/2
    return result;

# TODO 1: Update the file name
infile = open("dictionary.txt", "r")
line = infile.readline()

# Go through all the lines
while line:
    for i in range (int(math.pow(2,len(line)-1))):
        code = binarycode(i, len(line)-1)

        # Create the string with the upper case letters
        s=""
        for j in range (len(line)-1):
            if code[j]:
                s=s+line[j].upper()
            else:
                s=s+line[j]
        print(s)
    line = infile.readline()
   
#TODO 2: Make sure to add one character to the end of the text file
