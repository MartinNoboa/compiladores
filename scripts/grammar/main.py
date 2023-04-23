# ------------------------------------
# Compiladores
# Final Project - Part I
# Detecting Terminals and NonTerminals
# @author:        Martin Noboa - A01704052
# @last_modified: March 19, 2022
# ------------------------------------

from Grammar import *
from functions import *
import os

def main():
    # check argv inputs
    args = parseArgv(sys.argv)
    # get inputs
    if(args['flag'] == '-f'):
        left, right, values = parseContent(args['fileName'])
    elif(args['flag'] == '-i'):
        left , right, values = readInput()
    
    # declare Grammar object
    grammar = Grammar(values, left, right)
    # find terminals 
    grammar.terminals()
    # find print terminals and nonTerminals 
    grammar.terminalsToString()
    grammar.nonTerminalsToString()
    
    
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
        # find terminals 
        grammar.terminals()
        # find print terminals and nonTerminals 
        grammar.terminalsToString()
        grammar.nonTerminalsToString()
    
                
if __name__ == "__main__":
    # main()
    testAll()
            