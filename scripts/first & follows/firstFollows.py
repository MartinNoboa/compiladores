# ------------------------------------
# Compiladores
# Firsts & Follows
# @author:        Martin Noboa - A01704052
# @date:          October 18, 2022
# @last_modified: October 18, 2022
# ------------------------------------

from ctypes import string_at
from distutils.command.clean import clean
from os.path import exists
import sys
#dictionary to hold answers
original = {}
firstsDic = {}
followsDic = {}
# left values -> not terminal
left = []
# right values
right = []
#input value
input = []

def fillDictionary():
    for i in left:
        i.strip()
        if i not in firstsDic:
            firstsDic[i] = []
            followsDic[i] =[]
    firstKey = list(followsDic.keys())[0]
    followsDic[firstKey] += "$"

def main():
    print("Starting...")
    fileName = sys.argv[1]
    success = readFile(fileName)
    if (success):
        print("File loaded correctly.")
        fillDictionary()
        print("Dictionary populated correctly.")
        print("Computing firsts...")
        firsts()
        print("First computed correctly.")
        print("Computing follows...")
        follows()
        print("Follows computed correctly.")
        printAnswer()
    else:
        print("The file does not exist.")
        exit()

def readFile(filename):
# reads file and processes content
# @input : name of the file to read
# @output : cleaned up list
    if (exists(filename)):
        with open(filename) as file:
            n = int(file.readline().strip())
            for i in range(n):
                input.append(next(file).strip())
                clean = empty(input,True)
            for line in clean:
                temp = line.split("->",1)
                left.append(temp[0].strip())
                right.append([x for x in list(temp[1].split(" ")) if x])
            return True
    else:
        return False

def empty(list, strng):
# change empty space for "empty" string and viceversa
# @input : list to be processed, flag to indicate order to reverse
# @output : cleaned up list
    clean = []
    if strng:
        for line in list:
            newLine = line.replace(" ' '","epsilon")
            clean.append(newLine)
    else:
        for line in list:
            newLine = line.replace("epsilon"," ' '")
            clean.append(newLine)
    return clean
            
def firsts():
    for i in range(len(right)):
        temp = []
        if right[i][0] == 'epsilon':
            temp.append("' '")
        else:
            temp.append(right[i][0])
        [firstsDic[left[i]].append(x) for x in temp if x not in firstsDic[left[i]]]

    while True:
        cleanFirsts()
        if not checkUpper():
            break

def getFirst(list, index):
    if list[index] in firstsDic.keys():
        return firstsDic[list[index]]
    else:
        return list[index]
 
def cleanFirsts():
    #loop through keys
    for i in firstsDic.keys():
        #loop through list
        for char in firstsDic[i]:
            if char in firstsDic.keys():
                firstsDic[i] = firstsDic[char]

def checkUpper():
    for i in firstsDic:
        for char in firstsDic[i]:
            if char in firstsDic.keys():
                return True
    return False

def follows():
    for key in followsDic.keys():
        for element in right:
            for i in range(len(element)):
                if element[i] == key:
                    #check next element exists
                    if i+1 < len(element):
                        #if true append first of next element
                        followsDic[key].append(getFirst(element, i+1))
                    else:
                        #else append key
                        followsDic[key].append(key)
   

        
         
def toString(list):
    string = ''
    for i in list:
        string += str(i)
        string += ","
    return string

def printAnswer():
    """ S => FIRST = {b,c,a,''}, FOLLOW = {$}
    A => FIRST = {b,c,a,''}, FOLLOW = {a}
    APrime => FIRST = {c,a,''}, FOLLOW = {a} """
    for key in firstsDic.keys():
        print(key + " => FIRST = {" + toString(firstsDic[key]) + "}, FOLLOW = {"+ toString(followsDic[key]) + "}")

main()
