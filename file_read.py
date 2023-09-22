## Reading file using read() function

# read() reads all the contents in one shot
def read_file():
    """Read entire content from the file"""
    infile = open("Games.txt", 'r', encoding="utf-8")
    print("1) Reading contents with read() function\n")
    file_contents = infile.read()
    print("Type of fileContents object = ", type(file_contents))
    print(file_contents)
    print("---------------------------------------------\n")
    #close file
    infile.close()


def read_specific_characters():
    """Reading specific number of characters"""
    infile = open("Games.txt", 'r', encoding="utf-8")
    print("2) Reading using read(n) function\n")
    char = infile.read(4) #Read first four characters
    print(char)
    next_char = infile.read(10) # Read 10 characters
    print(next_char)
    print(repr(next_char))
    more_char = infile.read(8) # Read 8 more characters
    print(more_char)
    print(repr(more_char))
    print("---------------------------------------------\n")
    infile.close()


def read_file_readline():
    """Reading text file using readlines() function"""
    infile = open("Games.txt", 'r', encoding="utf-8")
    linelist = infile.readlines()
    print(linelist)
    for line in linelist:
        print(line.rstrip())
    infile.close()
    print("---------------------------------------------\n")


read_file()
read_specific_characters()
read_file_readline()
