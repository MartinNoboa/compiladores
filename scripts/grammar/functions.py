from Grammar import *
from distutils.command.clean import clean
from os.path import exists, os
import collections

        
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
        elif(args['flag'] == '-i' or args['flag'] == '-a'):
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
    l = []
    r = []
    values = {}
    input = []
    grammar = {}
    with open(fileName) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            aux = next(f).strip().split()
            if aux[0] not in grammar.keys():
                grammar[aux[0]] = []
            if "'" in aux[2:]:
                aux.remove("'")
                aux = list(map(lambda x: x.replace("'","eps"),aux))
            r.append(aux[2:])
            grammar[aux[0]].append(aux[2:])
    
    r = list(dict.fromkeys([item for sublist in r for item in sublist]))
    l = list(grammar.keys())
    
    return l,r,grammar


def readInput():
    """
    reads input from user 
    returns right and left lists and grammar dict
    """
    l = []
    r = []
    grammar = {}
    # number of lines to read
    print("Enter number n of lines: ")
    n = int(input())
    for i in range(n):
        line = input()
        temp = line.split()
        if temp[0] not in grammar.keys():
            grammar[temp[0]] = []
        if "'" in temp[2:]:
            temp.remove("'")
            temp = list(map(lambda x: x.replace("'","eps"),temp))
        r.append(temp[2:])
        grammar[temp[0]].append(temp[2:]) 
        
    r = list(dict.fromkeys([item for sublist in r for item in sublist]))
    l = list(grammar.keys())
    
    return l,r,grammar


def testAll():
    testFiles = os.listdir('./inputs/')
    # add script to read and compare result vs expected result
    for i,testFile in enumerate(testFiles,start=1):
        print("-" * 50)
        print(f'Input {i}')
        dir = "inputs/" + testFile
        left, right, values = parseContent(dir)
        # declare Grammar object
        grammar = Grammar(values, left, right)
        # build object 
        grammar.build()
        # grammar.grammarToString()
        # grammar.terminalsToString()
        # grammar.nonTerminalsToString()
        grammar.firstsToString()
    