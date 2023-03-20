# ------------------------------------
# Compiladores
# Final Project - Part I
# Detecting Terminals and NonTerminals
# @author:        Martin Noboa - A01704052
# @last_modified: March 19, 2022
# ------------------------------------

from functions import *

def terminals(l,r):
    return [char for char in r if char not in l and char != 'eps']

def main():
    # check argv inputs
    args = parseArgv(sys.argv)
    # get inputs
    if(args['flag'] == '-f'):
        left, right = parseContent(args['fileName'])
    elif(args['flag'] == '-i'):
        left , right = readInput()
    
    # find terminals 
    terminal = terminals(left,right)
    print("Terminal:", ', '.join(terminal))
    print("Non terminal:", ', '.join(left))
                
if __name__ == "__main__":
  main()
            