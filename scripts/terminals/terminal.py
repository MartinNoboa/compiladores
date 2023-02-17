# ------------------------------------
# Compiladores
# Final Project - Primera entrega
# @author:        Martin Noboa - A01704052
# @date:          September 5, 2022
# @last_modified: September 9, 2021
# ------------------------------------

from distutils.command.clean import clean
from os.path import exists
import sys

# number of CLI flags 
numberFlags = len(sys.argv)
# number of CLI flags 
flag = sys.argv[1]
# left values -> not terminal
left = []
# right values
right = []
# terminal values
terminal = []


# reads input flags and validates accordingly
def validate():
    input = []
    if(flag == '-f'):
        if(numberFlags < 3):
            print('No file specified.')
            exit()
        else:
            fileName = sys.argv[2]
            if (exists(fileName)):
                with open(fileName) as f:
                    n = int(f.readline().strip())
                    for i in range(n):
                        input.append(next(f).strip())
                left,right = cleanFileContent(input)
                left = cleanArray(left)
                right = cleanArray(right)
                result(left,right)
            else:
                print("The file does not exist.")
                exit()
    elif(flag == '-i'):
            left , right = readInput()
            left = cleanArray(left)
            right = cleanArray(right)
            result(left, right)
    else:
        print("Not a valid flag.")
        exit()

# function that reads and processes the input
# @output : 2 lists - left and right values
def readInput():
    l = []
    r = []
    print("Enter number n of lines: ")
    n = int(input())
    for i in range(n):
        line = input()
        temp = line.split()
        for j in range(len(temp)):
            if j>=2:
                r.append(temp[j])
        l.append(temp[0])
    return l,r
# cleans up the content of a text file
# @input : list with file content, each index is a line
# @output : 2 lists - left and right values

def cleanFileContent(input):
    l = []
    r = []
    for line in input:
        temp = line.split()
        for j in range(len(temp)):
            if j>=2:
                r.append(temp[j])
        l.append(temp[0])
    return l,r

# removes repeated and unnecesary characters
# @input : list to be processed
# @output : cleaned up list
def cleanArray(input):
    temp = []
    for i in input:
        if i not in temp:
            if i != "'":
                temp.append(i)
    return temp 

# find terminal values comparing 2 lists - non terminal values and values to be defined
# @input : nonterminal values list, right values list
# @output : terminal values list
def findTerminal(r,l):
    t = []
    for i in l:
        match = False
        for j in r:
            if j == i:
                match = True
        if match == False:
            t.append(i)
    return t

# calls findTerminal(a,b) function and prints results
# @input : nonterminal values list, right values list
def result(l,r):
    terminal = findTerminal(l,r)
    print("Non terminal:")
    print(l)
    print("Terminal:")
    print(terminal)
            
                


validate()
