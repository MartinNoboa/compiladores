
class Grammar:
    # declare attributes

    # declare constructor
    def __init__(self, values , left, right):
        # all values in the grammar
        self.__grammar = values
        # non terminal values
        self.__nonTerminal = left
        # terminal values
        self.__terminal = right
        # reduced grammar with all productions per non terminal
        self.__firsts = {}
        self.__follows = {}
        
    
    # basics--------------------------------------------------------------------------------------------------
    def build(self):
        self.__terminals()
        # self.__setProductions()
        # self.__setFirsts()
        # self.__setFollows()
        
    def __terminals(self):
        self.__terminal = [char for char in self.__terminal if char not in self.__nonTerminal and char != 'eps']
        
            
    def __setFirsts(self):
        # initialize dictionary with non terminal keys
        for key in self.__nonTerminal:
            self.__firsts[key] = []
        for i,line in enumerate(self.__grammar,start=1):
            if line[1] in self.__terminal:
                self.__firsts[line[0]].append(line[1])
            else:
                i = 1
                while self.__hasNext(line,line[i]) and self.__producesEpisolon(line[i]):
                    self.__firsts[line[0]].append(line[i])
                    i += 1
        # remove key from values
        for value in self.__firsts:
            if value in self.__firsts[value]:
                self.__firsts[value].remove(value)
        # remove non terminal from lists
        for line in reversed(self.__firsts.values()):
            for line in self.__firsts.values():
                for i,value in enumerate(line):
                    if value in self.__nonTerminal:
                        line.extend(self.__firsts[value])
                        del line[i]
        #remove doubles
        for key in self.__firsts:
            self.__firsts[key] = list(set(self.__firsts[key]))
    
    def __setFollows(self):
        for key in self.__nonTerminal:
            self.__follows[key] = []
        self.__follows[self.__nonTerminal[0]].append('$')
        for key in self.__follows:
            for line in self.__grammar:
                if key in line and line.index(key) != 0:
                    if self.__hasNext(line,key):
                        next = self.__getNext(line,key)
                        ## is it non Terminal
                        if next in self.__terminal:
                            self.__follows[key].append(next)
                        else:
                            # yes store firsts of next value
                            self.__follows[key].extend(self.__firsts[next])
                            # first of next value has eps
                            if 'eps' in self.__firsts[next]:
                                if self.__hasNext(line,next):
                                    next = self.__getNext(line,next)
                                    if next in self.__terminal:
                                        self.__follows[key].append(next)
                                    else:
                                        # yes store firsts of next value
                                        self.__follows[key].extend(self.__firsts[next])
                    else:
                        self.__follows[key].append(line[0])
                        
        # add follows 
        for lines in reversed(self.__follows.values()):
            for val in lines:
                if val in self.__nonTerminal:
                    lines.extend(self.__follows[val])
                    lines.remove(val)
        #remove doubles
        for key in self.__follows:
            self.__follows[key] = list(set(self.__follows[key]))
        for lines in self.__follows.values():
            if 'eps' in lines:
                del lines[lines.index('eps')]
            
    def __hasNext(self, list, value):
        return list.index(value) + 1 <= len(list) - 1
    
    def __getNext(self, list, value):
        return list[list.index(value) + 1]
    
    def __producesEpisolon(self, key):
        productions = [item for sublist in self.__grammar[key] for item in sublist]
        return 'eps' in productions
    
    # To Strings ------------------------------------------------------------------------------------------------
    def terminalsToString(self):
        print("Terminal:", ', '.join(self.__terminal))
    
    def nonTerminalsToString(self):
        print("Terminal:", ', '.join(self.__nonTerminal))

    def grammarToString(self):
        print("*"*3 + " Grammar " + "*"*3)
        for i in self.__grammar:
            for values in self.__grammar[i]:
                print(f'' + i + ' -> ' + ' '.join(values))
    
    def firstsToString(self):
        for key in self.__firsts:
            print(f'' + key + " -> " + ', '.join(self.__firsts[key]))
    
    def followsToString(self):
        print(self.__follows)
    
    
    # Gets --------------------------------------------------------------------------------------------------------
    def getTerminals(self):
        return self.__terminal
    
    def getFirsts(self):
        return self.__firsts
    
    def getFollows(self):
        return self.__follows
    
    def getFirst(self, key):
        return self.__firsts[key] 
    
    def getFollow(self, key):
        return self.__follows[key] 
    