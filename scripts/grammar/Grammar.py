
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
        self.__setFirsts()
        # self.__setFollows()
        
    def __terminals(self):
        self.__terminal = [char for char in self.__terminal if char not in self.__nonTerminal and char != 'eps']
            
    def __recursiveFirst(self, list):
        firsts = []
        for item in list:
            if item in self.__terminal:
                return item
            else:
                if item != 'eps':
                    firsts.append(self.getFirst(item))
                    if self.__producesEpisolon(item):
                        if self.__hasNext(list,item):
                            firsts.append(self.__recursiveFirst(self.__getNext(list, item)))
                    firsts = [item for sublist in firsts for item in sublist]
                    return firsts
                else:
                    return 'eps'
                
    def __setFirsts(self):
        # initialize dictionary with non terminal keys
        for key in self.__nonTerminal:
            self.__firsts[key] = []
        for key in reversed(self.__grammar):
            for production in self.__grammar[key]:
                firsts = self.__recursiveFirst(production)
                if type(firsts) == list:
                    for i in firsts:
                        self.__firsts[key].append(i)
                else:
                    self.__firsts[key].append(firsts)
            self.__firsts[key] = list(dict.fromkeys(self.__firsts[key]))
    
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
        print("*"*3 + " Firsts " + "*"*3)
        for key in self.__firsts:
            print(f'' + key + " = {" + ', '.join(self.__firsts[key]) + "}")
    
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
        if key in self.__nonTerminal:
            return self.__firsts[key] 
        else:
            return key
    
    def getFollow(self, key):
        return self.__follows[key] 
    