from Lexer import *
from Parser import *
import sys
import os


# Run all test cases at once
def testAll():
    testFiles = os.listdir('./test_cases/')
    for i,testFile in enumerate(testFiles,start=1):
        print(f'Test file {i}')
        dir = "test_cases/" + testFile
        parser = Parser(dir)
        parser.analize()
        print("ACCEPTED")

# test one file at the time
def unitTest():
    # change this value for each file test
    dir = "test_cases/prog4.txt"
    parser = Parser(dir)
    parser.analize()
    print("ACCEPTED")
        
if __name__ == '__main__':
    # change parameter value for each test file
    # unitTest()
    
    #test all
    testAll()