# ------------------------------------
# Compiladores
# Final Project - Part I
# Detecting Terminals and NonTerminals
# @author:        Martin Noboa - A01704052
# @last_modified: March 19, 2022
# ------------------------------------

from Grammar import *
from functions import *
import sys


def main():
    # check argv inputs
    args = parseArgv(sys.argv)
    # get grammar
    if(args['flag'] == '-f'):
        left, right, values = parseContent(args['fileName'])
    elif(args['flag'] == '-i'):
        left , right, values = readInput()
    elif(args['flag'] == '-a'):
        testAll()
        sys.exit()
    
    # declare Grammar object
    grammar = Grammar(values, left, right)
    # build object
    grammar.build()
    # grammar.grammarToString()
    # grammar.terminalsToString()
    # grammar.nonTerminalsToString()
    grammar.firstsToString()
    # grammar.followsToString()
           
if __name__ == "__main__":
    main()
            