from Lexer import *
from Parser import *
import sys

if __name__ == '__main__':
	
    print("EXAMPLE 1")
    parser = Parser("test_cases/prog5.txt")
    parser.analize()
    print("ACCEPTED")
