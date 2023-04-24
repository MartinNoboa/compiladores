
class Grammar:
    # declare attributes

    # declare constructor
    def __init__(self, values , left, right):
        # all values in the grammar
        self.__grammar = values
        # non terminal values
        self.nonTerminal = left
        # terminal values
        self.terminal = right
        # reduced grammar with all productions per non terminal
        self.productions = {}
        self.firsts = {}
        self.follows = {}
        
    #declare methods
    
    # basics--------------------------------------------------------------------------------------------------
    def build(self):
        self.__terminals()
        self.__setProductions()
        self.__setFirsts()
        self.__setFollows()
        
    def __terminals(self):
        self.terminal = [char for char in self.terminal if char not in self.nonTerminal and char != 'eps']
        
    def __setProductions(self):
        # set keys of non terminal values
        for key in self.nonTerminal:
            self.productions[key] = set()
        # set values to keys
        for line in self.__grammar:
            for i in line[1:]:
                self.productions[line[0]].add(i)
                
    def __setFirsts(self):
        for key in self.nonTerminal:
            self.firsts[key] = []
        for i,line in enumerate(self.__grammar,start=1):
            self.firsts[line[0]].append(line[1])
            if line[1] in self.nonTerminal:
                i = 1
                while self.__hasNext(line,line[i]) and self.__producesEpisolon(line[i]):
                    self.firsts[line[0]].append(line[i])
                    i += 1
        # remove key from values
        for value in self.firsts:
            if value in self.firsts[value]:
                self.firsts[value].remove(value)
        # remove non terminal from lists
        for line in reversed(self.firsts.values()):
            for line in self.firsts.values():
                for i,value in enumerate(line):
                    if value in self.nonTerminal:
                        line.extend(self.firsts[value])
                        del line[i]
        #remove doubles
        for key in self.firsts:
            self.firsts[key] = list(set(self.firsts[key]))
    
    def __setFollows(self):
        for key in self.nonTerminal:
            self.follows[key] = []
        self.follows[self.nonTerminal[0]].append('$')
        for key in self.follows:
            for line in self.__grammar:
                if key in line and line.index(key) != 0:
                    if self.__hasNext(line,key):
                        next = self.__getNext(line,key)
                        ## is it non Terminal
                        if next in self.terminal:
                            self.follows[key].append(next)
                        else:
                            # yes store firsts of next value
                            self.follows[key].extend(self.firsts[next])
                            # first of next value has eps
                            if 'eps' not in self.firsts[next]:
                                continue
                    else:
                        self.follows[key].append(line[0])
        # add follows 
        for lines in reversed(self.follows.values()):
            for val in lines:
                if val in self.nonTerminal:
                    lines.extend(self.follows[val])
                    del lines.index(val)
            #     for i,value in enumerate(line):
            #         if value in self.nonTerminal:
            #             line.extend(self.firsts[value])
            #             del line[i]
        #remove doubles
        for key in self.follows:
            self.follows[key] = list(set(self.follows[key]))
        for lines in self.follows.values():
            if 'eps' in lines:
                del lines[lines.index('eps')]
            
        
    
    def __hasNext(self, list, value):
        return list.index(value) + 1 <= len(list) - 1
    
    def __getNext(self, list, value):
        return list[list.index(value) + 1]
    
    def __producesEpisolon(self, key):
        return 'eps' in self.productions[key]
    
    # To Strings ------------------------------------------------------------------------------------------------
    def terminalsToString(self):
        print("Terminal:", ', '.join(self.terminal))
    
    def nonTerminalsToString(self):
        print("Terminal:", ', '.join(self.nonTerminal))

    def grammarToString(self):
        for i in self.__grammar:
            print(f'' + i[0] + ' -> ' + ' '.join(i[1:]))
    
    def productionsToString(self):
        for key in self.productions:
            print(f'' + key + " -> " + ', '.join(self.productions[key]))
    
    def firstsToString(self):
        # print(self.firsts)
        for key in self.firsts:
            print(f'' + key + " -> " + ', '.join(self.firsts[key]))
    
    def followsToString(self):
        print(self.follows)
    
    
    # Gets --------------------------------------------------------------------------------------------------------
    def getTerminals(self):
        return self.terminal
    
    def getFirsts(self):
        return self.firsts
    
    def getFollows(self):
        return self.follows
    
    def getFirst(self, key):
        return self.firsts[key] 
    
    def getFollow(self, key):
        return self.follows[key] 
    