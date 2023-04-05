import os
from enum import Enum

class LexicalErrorException(Exception):
    "Generated when there is a lexical error"
    pass


class Tag(Enum):
	EOF = 65535
	ERROR = 65534
	## Operators ##
	GEQ = 258
	LEQ = 259
	NEQ = 260
	ASSIGN = 261
	## REGULAR EXPRESSIONS ##
	ID = 357
	NUMBER = 358
	STRING = 359
	TRUE = 360
	FALSE = 361
	## RESERVED WORDS ##
	VAR = 457
	FORWARD = 548
	BACKWARD = 459
	LEFT = 460
	RIGHT = 461
	SETX = 462
	SETY = 463
	SETXY = 464
	CLEAR = 465
	CIRCLE = 466
	ARC = 467
	PENUP = 468
	PENDOWN = 469
	COLOR = 470
	PENWIDTH = 471
	PRINT = 472
	REPEAT = 473
	IF = 474
	IFELSE = 475
	HOME = 476
	NOT = 477
	OR = 478
	AND = 479
	MOD = 480
	
class Token:
	__tag = Tag.EOF
	
	def __init__(self, value):
		self.__tag = value
		
	def getTag(self):
		return self.__tag
		
	def __str__(self):
		if self.__tag == Tag.GEQ:
			return "Token - value >="
		elif self.__tag == Tag.LEQ:
			return "Token - value <="
		elif self.__tag == Tag.NEQ:
			return "Token - value <>"
		elif self.__tag == Tag.EQ:
			return "Token - value :="
		elif self.__tag == Tag.TRUE:
			return "Token - value TRUE"
		elif self.__tag == Tag.FALSE:
			return "Token - value FALSE"
		elif self.__tag == Tag.VAR:
			return "Token - value VAR"
		else:
			return "TOKEN - value " + chr(self.__tag)
			
class Number(Token):
	__value = 0.0
	
	def __init__(self, val):
		super().__init__(Tag.NUMBER)
		self.__value = val

	def getTag(self):
		return super().getTag()
	
	def getValue(self):
		return self.__value
	
	def __str__(self):
		return "Number - value: " + str(self.__value)
	
class Word(Token):
	__lexeme = ""
	
	def __init__(self, tag, lex):
		super().__init__(tag)
		self.__lexeme = lex

	def getTag(self):
		return super().getTag()
	
	def getLexeme(self):
		return self.__lexeme
	
	def __str__(self):
		if self.getTag() == Tag.ID:
			return "Word - lexeme: " + str(self.__lexeme)
		else:
			return "Reserved Word - lexeme: " + str(self.__lexeme)

class String(Token):
	__string = ""
	
	def __init__(self, s):
		super().__init__(Tag.STRING)
		self.__string = s

	def getTag(self):
		return super().getTag()
	
	def getString(self):
		return self.__string
	
	def __str__(self):
		return "String - text: " + str(self.__string)

class Lexer:
	__peek = ' '
	__words = {}
	__input = None

	def __init__(self, filepath):
		#assert(not(os.path.isfile(filepath)), "File Not Found")
		
		self.__input = open(filepath, "r")
		self.__peek = ' '

		self.__words["VAR"] = Word(Tag.VAR, "VAR")
		self.__words["FORWARD"] = Word(Tag.FORWARD, "FORWARD")
		self.__words["FD"] = Word(Tag.FORWARD, "FORWARD")
		self.__words["BACKWARD"] = Word(Tag.BACKWARD, "BACKWARD")
		self.__words["BK"] = Word(Tag.BACKWARD, "BACKWARD")
		self.__words["LEFT"] = Word(Tag.LEFT, "LEFT")
		self.__words["LT"] = Word(Tag.LEFT, "LEFT")
		self.__words["RIGHT"] = Word(Tag.RIGHT, "RIGHT")
		self.__words["RT"] = Word(Tag.RIGHT, "RIGHT")
		self.__words["SETX"] = Word(Tag.SETX, "SETX")
		self.__words["SETY"] = Word(Tag.SETY, "SETY")
		self.__words["SETXY"] = Word(Tag.SETXY, "SETXY")
		self.__words["HOME"] = Word(Tag.HOME, "HOME")
		self.__words["CLEAR"] = Word(Tag.CLEAR, "CLEAR")
		self.__words["CLS"] = Word(Tag.CLEAR, "CLEAR")
		self.__words["ARC"] = Word(Tag.ARC, "ARC")
		self.__words["PENUP"] = Word(Tag.PENUP, "PENUP")
		self.__words["PU"] = Word(Tag.PENUP, "PENUP")
		self.__words["PENDOWN"] = Word(Tag.PENDOWN, "PENDOWN")
		self.__words["PD"] = Word(Tag.PENDOWN, "PENDOWN")
		self.__words["COLOR"] = Word(Tag.COLOR, "COLOR")
		self.__words["PENWIDTH"] = Word(Tag.PENWIDTH, "PENWIDTH")
		self.__words["PRINT"] = Word(Tag.PRINT, "PRINT")
		self.__words["REPEAT"] = Word(Tag.REPEAT, "REPEAT")
		self.__words["IF"] = Word(Tag.IF, "IF")
		self.__words["IFELSE"] = Word(Tag.IFELSE, "IFELSE")
		self.__words["NOT"] = Word(Tag.NOT, "NOT")
		self.__words["OR"] = Word(Tag.OR, "OR")
		self.__words["AND"] = Word(Tag.AND, "AND")
		self.__words["MOD"] = Word(Tag.MOD, "MOD")

	def read(self):
		self.__peek = self.__input.read(1)
	
	def readch(self, c):
		self.read()
		if self.__peek != c:
			return False

		self.__peek = ' '
		return True

	def __skipSpaces(self):
		while True:
			if self.__peek == ' ' or self.__peek == '\t' or self.__peek == '\r' or self.__peek == '\n':
				self.read()
			else:
				break
	
	def scan(self):
		self.__skipSpaces()

		## ADD CODE TO SKIP COMMENTS HERE ##
		if self.__peek == '%':
			while True:
				self.read()
				if self.__peek == '\n':
					break
			self.__skipSpaces()

		if self.__peek == '<':
			if self.readch('='):
				return Word(Tag.LEQ, "<=")
			elif self.readch('>'):
				return Word(Tag.NEQ, "<>")
			else:
				return Token(ord('<'))
		elif self.__peek == '>':
			if self.readch('='):
				return Word(Tag.GEQ, ">=")
			else:
				return Token(ord('>'))
		elif self.__peek == '#':
			if self.readch('t'):
				return Word(Tag.TRUE, "#t")
			elif self.readch('>'):
				return Word(Tag.FALSE, "#f")
			else:
				return Token(ord('#'))
		elif self.__peek == ':':
			if self.readch('='):
				#print("reading :=")
				return Word(Tag.EQ, ":=")
			else:
				return Token(ord(':'))

		if self.__peek  == '"':
			val = ""
			while True:
				val = val + self.__peek
				self.read()
				if self.__peek == '"':
					break
			
			val = val + self.__peek
			self.read()
			return String(val)

		if self.__peek.isdigit():
			val = 0.0
			while True:
				val = (val * 10) + int(self.__peek)
				self.read()
				if not(self.__peek.isdigit()):
					break
			if self.__peek  == '.':
				self.read()
				if self.__peek.isdigit():
					divisor = 10.0
					while True:
						val = val + (float(self.__peek) / divisor)
						divisor = divisor * 10.0
						self.read()
						if not(self.__peek.isdigit()):
							break
				else:
					raise Exception('Lexical error')
			return Number(val)

		if self.__peek.isalpha():
			val = ""
			while True:
				val = val + self.__peek.upper()
				self.read()
				if not(self.__peek.isalnum()):
					break

			if val in self.__words:
				return self.__words[val]

			w = Word(Tag.ID, val)
			self.__words[val] = Word(Tag.ID, val)
			return w

		if not(self.__peek):
			return Token(Tag.EOF)			

		token = Token(ord(self.__peek))
		self.__peek = ' ' 
		return token
