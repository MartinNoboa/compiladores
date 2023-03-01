from lexer import *
import sys

if __name__ == '__main__':
	lexer = Lexer("test_cases/prog4.txt")
	
	token = lexer.scan()
	while token.getTag() != Tag.EOF:
		print(str(token))
		##sys.stdin.read(1)
		token = lexer.scan()
	print("END")
