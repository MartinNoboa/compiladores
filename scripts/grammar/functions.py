from distutils.command.clean import clean
from os.path import exists
import collections
import sys

        
def parseArgv(arg):
    """
    verifies sys.argv values
    returns dictionary w/ flag and filename
    """
    # define dictionary
    args = {
        'flag': '',
        'fileName': ''
    }
    # number of args
    if (2 <= len(arg)):
        args['flag'] = arg[1]
        # flag -> file input
        if(args['flag'] == '-f'):
            # check if filename provided
            if(len(arg) < 3):
                print('No file specified.')
                exit()
            else:
                args['fileName'] = './inputs/' + arg[2]
                if (exists(args['fileName'])):
                    return args
                else:
                    print("The file does not exist.")
                    exit()
        # flag -> user input 
        elif(args['flag'] == '-i'):
                return args
        else:
            print("Not a valid flag.")
            exit()
    else:
        print("No flag selected.")
        exit()
    

def parseContent(fileName):
    """
    converts text file content in 2 lists
    returns right and left lists
    """
    # read file values and convert to lists
    values = {}
    input = []
    grammar = []
    with open(fileName) as f:
        n = int(f.readline().strip())
        for i in range(n):
            input.append(next(f).strip())
            # define left and right lists 
            l = []
            r = []
            for line in input:
                temp = line.split()
                for j in range(len(temp)):
                    if j>=2:
                        r.append(temp[j])
                l.append(temp[0])
    #clean outputs 
    r = cleanList(r)
    grammar = list(map(cleanList,grammar))
    # remove doubles
    r = list(dict.fromkeys(r))
    l = list(dict.fromkeys(l))

    return l,r,grammar


def readInput():
    """
    reads input from user 
    returns right and left lists
    """
    l = []
    r = []
    grammar = []
    # number of lines to read
    print("Enter number n of lines: ")
    n = int(input())
    for i in range(n):
        line = input()
        temp = line.split()
        grammar.append(line.split()) 
        for j in range(len(temp)):
            if j>=2:
                r.append(temp[j])
        l.append(temp[0])
    #clean outputs 
    r = cleanList(r)
    grammar = list(map(cleanList,grammar))
    # remove doubles
    r = list(dict.fromkeys(r))
    l = list(dict.fromkeys(l))

    return l,r,grammar

def cleanList(list):
    """
    change ' ' for eps and remove ->
    returns updated list
    """
    for i, char in enumerate(list):
        if char == "'":
            # del list[i+1]
            list[i] = "eps"
        if char == '->':
            del list[i]
    return list