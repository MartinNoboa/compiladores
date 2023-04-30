
class Grammar:
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
        self.__setFollows()
        
    def __terminals(self):
        self.__terminal = [char for char in self.__terminal if char not in self.__nonTerminal and char != 'eps']
            
    def __recursiveFirst(self, list):
        firsts = []
        for item in list:
            if item in self.__terminal:
                return item
            else:
                if item != 'eps':
                    firsts.extend(self.__getFirsts(item))
                    if self.__producesEpisolon(item):
                        if self.__hasNext(list,item):
                            firsts.extend(self.__recursiveFirsts(self.__getNext(list, item)))
                    # firsts = [item for sublist in firsts for item in sublist]
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
    
    def __recursiveFollow(self, list, key):
        follows = []
        for item in list:
            if item == key:
                # tiene next
                if self.__hasNext(list, key):
                    # obtener next
                    next = self.__getNext(list, item)
                    # next es terminal
                    if next in self.__terminal:
                        # devolver next
                        return next
                    # next no es terminal
                    else:
                        # agregar first de next a follows
                        follows.append([i for i in self.__firsts[next] if i != 'eps'])
                        # next produce epsilon
                        if self.__producesEpisolon(next):
                            # llamada recursiva con la lista y key = next
                            follows.append(self.__recursiveFollow(list, next)) 
                        # follows = [item for sublist in follows for item in sublist]
                        return follows
                # no tiene next
                else:
                    # devolver follow de la key
                    current_key = self.getKey(list) 
                    if key != current_key and item != current_key:
                        return self.__getFollows(current_key)
                
    def __setFollows(self):
        # initialize dictionary with non terminal keys
        for key in self.__nonTerminal:
            self.__follows[key] = []
        self.__follows[list(self.__follows.keys())[0]].append('$')
        for key in self.__grammar:
            for productions in self.__grammar.values():
                for production in (productions):
                    if key in production:
                        follows = self.__recursiveFollow(production, key)
                        if type(follows) == list and follows != None:
                            for i in follows:
                                if i not in self.__follows[key]:
                                    self.__follows[key].append(i)
                        else:
                            if follows != None and follows != '.':
                                self.__follows[key].append(follows)
            
        
        for key in self.__follows:
            if None in self.__follows[key]:
                self.__follows[key].remove(None)
            for i in self.__follows[key]:
                if type(i) == list:
                    self.__follows[key] = [item for sublist in self.__follows[key] for item in sublist]
            
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
        print("*"*3 + " Follows " + "*"*3)
        for key in self.__follows:
            print(f'' + key + " = {" + ', '.join(self.__follows[key]) + "}")
        # print(self.__follows)
    
    def firstsFollowsToString(self):
        print("*"*3 + " Firsts & Follows" + "*"*3)
        for key in self.__firsts:
            print(f'' + key + " => FIRSTS = {" + ', '.join(self.__firsts[key]) + "}, " + "FOLLOWS = {" + ', '.join(self.__follows[key]) + "}")
    
    # Gets --------------------------------------------------------------------------------------------------------
    def __getFirsts(self, key):
        if key in self.__nonTerminal:
            return self.__firsts[key] 
        else:
            return key
    
    def __getFollows(self, key):
        return self.__follows[key]
    
    def getKey(self, list):
        for key in self.__grammar:
            if list in self.__grammar[key]:
                return key