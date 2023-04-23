
class Grammar:
    # declare attributes

    # declare constructor
    def __init__(self, values , left, right):
        self.grammar = values
        self.nonTerminal = left
        self.terminal = []
        self.production = right
        self.first = {}
        self.follows = {}
        
    #declare methods
    def terminals(self):
        self.terminal = [char for char in self.production if char not in self.nonTerminal and char != 'eps']
    
    def getTerminals(self):
        return self.terminal
    
    def terminalsToString(self):
        print("Terminal:", ', '.join(self.terminal))
    
    
    def nonTerminalsToString(self):
        print("Terminal:", ', '.join(self.nonTerminal))

