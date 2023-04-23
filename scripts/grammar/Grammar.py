
class Grammar:
    # declare attributes

    # declare constructor
    def __init__(self, values , left, right):
        self.grammar = values
        self.nonTerminal = left
        self.terminal = []
        self.production = right
        self.firsts = {}
        self.follows = {}
        
    #declare methods
    
    # Terminals and Nonterminals ------------------------------------------------------------------------------
    def terminals(self):
        self.terminal = [char for char in self.production if char not in self.nonTerminal and char != 'eps']
    
    def getTerminals(self):
        return self.terminal
    
    def terminalsToString(self):
        print("Terminal:", ', '.join(self.terminal))
    
    def nonTerminalsToString(self):
        print("Terminal:", ', '.join(self.nonTerminal))

    # Grammar---------------------------------------------------------------------------------------------------
    def grammarToString(self):
        pass
    
    # First and Follows -----------------------------------------------------------------------------------------
    def setFirst(self, key, values):
        # add key to First dictionary and set set of values
        pass
    
    def setFollow(self, key, values):
        # add key to First dictionary and set set of values
        pass
    
    def first(self, key):
        return self.firsts[key] 
    
    def follow(self, key):
        return self.follows[key] 
    
    def getFirsts(self):
        return self.firsts
    
    def getFollows(self):
        return self.follows
    
    def hasNext(self, index, value):
        pass