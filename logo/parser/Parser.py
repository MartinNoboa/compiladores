from Lexer import *

class Parser:
    __lex = None
    __token = None

    def __init__(self, filepath):
        self.__lex = Lexer(filepath)
        self.__token = None

        self.__firstPrimaryExpression = set((Tag.ID, Tag.NUMBER, Tag.TRUE, Tag.FALSE, ord('(')))

        self.__firstUnaryExpression = self.__firstPrimaryExpression.union( set((ord('-'), ord('!'))) )
        
        self.__firstExtendedMultiplicativeExpression = set((ord('*'), ord('/'), Tag.MOD))

        self.__firstMultiplicativeExpression = self.__firstUnaryExpression

        self.__firstExtendedAdditiveExpression = set((ord('+'), ord('-')))
        
        self.__firstAdditiveExpression = self.__firstMultiplicativeExpression

        self.__firstExtendedRelationalExpression = set((ord('<'), ord('>')))
        
        self.__firstRelationalExpression = self.__firstAdditiveExpression    
        
        self.__firstExtendedEqualityExpression = set((ord('='), ord('<')))
            
        self.__firstEqualityExpression =  self.__firstRelationalExpression
        
        self.__firstExtendedConditionalTerm = {Tag.AND}
            
        self.__firstConditionalTerm = self.__firstEqualityExpression
        
        self.__firstExtendedConditionalExpression = {Tag.OR}
        
        self.__firstConditionalExpression = self.__firstConditionalTerm
        
        self.__firstExpression = self.__firstConditionalExpression
        
        self.__firstIfElseStatement = {Tag.IFELSE}
        
        self.__firstIfStatement = {Tag.IF}
        
        self.__firstConditionalStatement = self.__firstIfElseStatement.union(self.__firstIfStatement)
        
        self.__firstRepetitiveStatement = {Tag.REPEAT}
        
        self.__firstStructuredStatement = self.__firstRepetitiveStatement.union(self.__firstConditionalStatement)
        
        self.__firstElementList = {ord(',')}
        
        self.__firstElement = self.__firstExpression.union({Tag.STRING})
        
        self.__firstTextStatement = {Tag.PRINT}
        
        self.__firstPenWidthStatement = {Tag.PENWIDTH}
        
        self.__firstColorStatement = {Tag.COLOR}
        
        self.__firstPenDownStatement = {Tag.PENDOWN}
            
        self.__firstPenUpStatement = {Tag.PENUP}
        
        self.__firstArcStatement = {Tag.ARC}
        
        self.__firstCircleStatement = {Tag.CIRCLE}
        
        self.__firstClearStatement = {Tag.CLEAR}
        
        self.__firstDrawingStatement = self.__firstClearStatement | self.__firstCircleStatement | self.__firstArcStatement | self.__firstPenUpStatement | self.__firstPenDownStatement | self.__firstColorStatement | self.__firstPenWidthStatement
        
        self.__firstSetXYStatement = {Tag.SETXY}
        
        self.__firstSetYStatement = {Tag.SETY}
        
        self.__firstSetXStatement = {Tag.SETX}
        
        self.__firstLeftStatement = {Tag.LEFT}
        
        self.__firstRightStatement = {Tag.RIGHT}
        
        self.__firstBackwardStatement = {Tag.BACKWARD}
        
        self.__firstForwardStatement = {Tag.FORWARD}
        
        self.__firstMovementStatement = self.__firstForwardStatement | self.__firstBackwardStatement | self.__firstRightStatement | self.__firstLeftStatement | self.__firstSetXYStatement | self.__firstSetXStatement | self.__firstSetYStatement | {Tag.HOME}
        
        self.__firstAssigmentStatement = {Tag.ID}
        
        self.__firstIdentifierList = {ord(',')}
        
        self.__firstDeclarationStatement = {Tag.VAR}
        
        self.__firstSimpleStatement = self.__firstDeclarationStatement | self.__firstAssigmentStatement | self.__firstMovementStatement | self.__firstDrawingStatement | self.__firstTextStatement
        
        self.__firstStatement = self.__firstSimpleStatement | self.__firstStructuredStatement
        
        self.__firstStatementSequence = self.__firstStatement
        
        self.__firstProgram = self.__firstStatementSequence
        
    def __check(self, tag):
        if self.__token.getTag() == tag:
            self.__token = self.__lex.scan()
            # print(self.__token.getTag())
        else:
            raise Exception('Syntax Error')
    
    def analize(self):
        self.__token = self.__lex.scan()
        self.__program()

    def __primaryExpression(self):
        if self.__token.getTag() in self.__firstPrimaryExpression:
            if self.__token.getTag() == Tag.ID:
                self.__check(Tag.ID)
            elif self.__token.getTag() == Tag.NUMBER:
                self.__check(Tag.NUMBER)
            elif self.__token.getTag() == Tag.TRUE:
                self.__check(Tag.TRUE)
            elif self.__token.getTag() == Tag.FALSE:
                self.__check(Tag.FALSE)
            elif self.__token.getTag() == ord('('):
                self.__check(ord('('))
                self.__expression()
                self.__check(ord(')'))
        else:
            raise Exception('Syntax Error')
        
    def __unaryExpression(self):
        if self.__token.getTag() in self.__firstUnaryExpression:
            if self.__token.getTag() == ord('-'):
                self.__check(ord('-'))
                self.__unaryExpression()
            elif self.__token.getTag() == ord('!'):
                self.__check(ord('!'))
                self.__unaryExpression()
            else:
                self.__primaryExpression()
        else: 
            raise Exception('Syntax Error')
        
    def __extendedMultiplicativeExpression(self):
        if self.__token.getTag() in self.__firstExtendedMultiplicativeExpression:
            if self.__token.getTag() == ord('*'):
                self.__check(ord('*'))
                self.__unaryExpression()
                self.__extendedMultiplicativeExpression()
            elif self.__token.getTag() == ord('/'):
                self.__check(ord('/'))
                self.__unaryExpression()
                self.__extendedMultiplicativeExpression()
            elif self.__token.getTag() == Tag.MOD:
                self.__check(Tag.MOD)
                self.__unaryExpression()
                self.__extendedMultiplicativeExpression()

    def __multiplicativeExpression(self):
        if self.__token.getTag() in self.__firstMultiplicativeExpression:
            self.__unaryExpression()
            self.__extendedMultiplicativeExpression()
        else:
            raise Exception('Syntax Error')
        
    def __extendedAdditiveExpression(self):
        if self.__token.getTag() in self.__firstExtendedAdditiveExpression:
            if self.__token.getTag() == ord('+'):
                self.__check(ord('+'))
                self.__multiplicativeExpression()
                self.__extendedAdditiveExpression()
            elif self.__token.getTag() == ord('-'):
                self.__check(ord('-'))
                self.__multiplicativeExpression()
                self.__extendedAdditiveExpression()
                
    def __additiveExpression(self):
        if self.__token.getTag() in self.__firstAdditiveExpression:
            self.__multiplicativeExpression()
            self.__extendedAdditiveExpression()
        else:
            raise Exception('Syntax Error')
    
    def __extendedRelationalExpression(self):
        if self.__token.getTag() in self.__firstExtendedRelationalExpression:
            if self.__token.getTag() == ord('<'):
                self.__check(ord('<'))
                self.__check(ord('='))
                self.__additiveExpression()
                self.__extendedRelationalExpression()
            elif self.__token.getTag() == ord('>'):
                self.__check(ord('>'))
                self.__check(ord('='))
                self.__additiveExpression()
                self.__extendedRelationalExpression()
                
    def __relationalExpression(self):
        if self.__token.getTag() in self.__firstRelationalExpression:
            self.__additiveExpression()
            self.__extendedRelationalExpression()
        else:
            raise Exception('Syntax Error')
        
    def __extendedEqualityExpression(self):
        if self.__token.getTag() in self.__firstExtendedEqualityExpression:
            if self.__token.getTag() == ord('='):
                self.__check(ord('='))
                self.__relationalExpression()
                self.__extendedEqualityExpression()
            elif self.__token.getTag() == ord('<'):
                self.__check(ord('<'))
                self.__check(ord('>'))
                self.__relationalExpression()
                self.__extendedEqualityExpression()
                
    def __equalityExpression(self):
        if self.__token.getTag() in self.__firstEqualityExpression:
            self.__relationalExpression()
            self.__extendedEqualityExpression()
        else:
            raise Exception('Syntax Error')
        
    def __extendedConditionalTerm(self):
        if self.__token.getTag() in self.__firstExtendedConditionalTerm:
            if self.__token.getTag() == Tag.AND:
                self.__check(Tag.AND)
                self.__equalityExpression()
                self.__extendedConditionalTerm()
                self.__extendedBooleanTerm()
    
    def __conditionalTerm(self):
        if self.__token.getTag() in self.__firstConditionalTerm:
            self.__equalityExpression()
            self.__extendedConditionalTerm()
        else:
            raise Exception('Syntax Error')
        
    def __extendedConditionalExpression(self):
        if self.__token.getTag() in self.__firstExtendedConditionalExpression:
            # if self.__token.getTag() == Tag.OR:
            self.__check(Tag.OR)
            self.__conditionalTerm()
            self.__extendedConditionalExpression()
        
    def __conditionalExpression(self):
        if self.__token.getTag() in self.__firstConditionalExpression:
            self.__conditionalTerm()
            self.__extendedConditionalExpression()
        else:
            raise Exception('Syntax Error')
            
    def __expression(self):
        if self.__token.getTag() in self.__firstExpression:
            self.__conditionalExpression()
        else:
            raise Exception('Syntax Error')
        
    def __ifElseStatement(self):
        if self.__token.getTag() in self.__firstIfElseStatement:
            self.__check(Tag.IFELSE)
            self.__expression()
            self.__check(ord('['))
            self.__statementSequence()
            self.__check(ord(']'))
        else:
            raise Exception('Syntax Error')
    
    def __ifStatement(self):
        if self.__token.getTag in self.__firstIfStatement:
            self.__check(Tag.IF)
            self.__expression()
            self.__check(ord('['))
            self.__statementSequence()
            self.__check(ord(']'))
        else:
            raise Exception('Syntax Error')
    
    def __conditionalStatement(self):
        if self.__token.getTag() in self.__firstConditionalStatement:
            if self.__token.getTag() in self.__firstIfStatement:
                self.__ifStatement()
            else:
                self.__ifElseStatement()
        else:
            raise Exception('Syntax Error')
        
    def __repetitiveStatement(self):
        if self.__token.getTag() in self.__firstRepetitiveStatement:
            self.__check(Tag.REPEAT)
            self.__expression()
            self.__check(ord('['))
            self.__statementSequence()
            self.__check(ord(']'))
        else:
            raise Exception('Syntax Error')
        
    def __structuredStatement(self):
        if self.__token.getTag() in self.__firstStructuredStatement:
            if self.__token.getTag() in self.__firstRepetitiveStatement:
                self.__repetitiveStatement()
            else:
                self.__conditionalStatement()
        else:
            raise Exception('Syntax Error')
    
    def __elementList(self):
        if self.__token.getTag() in self.__firstElementList:
            self.__check(ord(','))
            self.__element()
            self.__elementList()
    
    def __element(self):
        if self.__token.getTag() in self.__firstElement:
            if self.__token.getTag() == Tag.STRING:
                self.__check(Tag.STRING)
            else:
                self.__expression()
        else:
            raise Exception('Syntax Error')
        
    def __textStatement(self):
        if self.__token.getTag() in self.__firstTextStatement:
            self.__check(Tag.PRINT)
            self.__check(ord('['))
            self.__element()
            self.__elementList()
            self.__check(ord(']'))
        else:
            raise Exception('Syntax Error')
    
    def __penWidthStatement(self):
        if self.__token.getTag() in self.__firstPenWidthStatement:
            self.__check(Tag.PENWIDTH)
            self.__expression()
        else:
            raise Exception('Syntax Error')
        
    def __colorStatement(self):
        if self.__token.getTag() in self.__firstColorStatement:
            self.__check(Tag.COLOR)
            self.__expression()
            self.__check(ord(','))
            self.__expression()
            self.__check(ord(','))
            self.__expression()
        else:
            raise Exception('Syntax Error')
    
    def __penDownStatement(self):
        if self.__token.getTag() in self.__firstPenDownStatement:
            self.__check(Tag.PENDOWN)
        else:
            raise Exception('Syntax Error')
        
    def __penUpStatement(self):
        if self.__token.getTag() in self.__firstPenUpStatement:
            self.__check(Tag.PENUP)
        else:
            raise Exception('Syntax Error')
    
    def __arcStatement(self):
        if self.__token.getTag() in self.__firstArcStatement:
            self.__check(Tag.ARC)
            self.__expression()
        else:
            raise Exception('Syntax Error')
    
    def __circleStatement(self):
        if self.__token.getTag() in self.__firstCircleStatement:
            self.__check(Tag.CIRCLE)
            self.__expression()
        else:
            raise Exception('Syntax Error')
    
    def __clearStatement(self):
        if self.__token.getTag() in self.__firstClearStatement:
            self.__check(Tag.CLEAR)
        else:
            raise Exception('Syntax Error')

    def __drawingStatement(self):
        if self.__token.getTag() in self.__firstDrawingStatement:
            if self.__token.getTag() == Tag.CLEAR:
                self.__clearStatement()
            if self.__token.getTag() == Tag.CIRCLE:
                self.__circleStatement()
            if self.__token.getTag() == Tag.ARC:
                self.__arcStatement()
            if self.__token.getTag() == Tag.PENUP:
                self.__penUpStatement()
            if self.__token.getTag() == Tag.PENDOWN:
                self.__penDownStatement()
            if self.__token.getTag() == Tag.COLOR:
                self.__colorStatement()
            if self.__token.getTag() == Tag.PENWIDTH:
                self.__penWidthStatement()
        else:
            raise Exception('Syntax Error')
        
    def __setXYStatement(self):
        if self.__token.getTag() in self.__firstSetXYStatement():
            self.__check(Tag.SETXY)
            self.__expression()
            self.__check(ord(','))
            self.__expression()
        else:
            raise Exception('Syntax Error')
    
    def __setYStatement(self):
        if self.__token.getTag() in self.__firstSetYStatement:
            self.__check(Tag.SETY)
            self.__expression()
        else:
            raise Exception('Syntax Error')
    
    def __setXStatement(self):
        if self.__token.getTag() in self.__firstSetXStatement:
            self.__check(Tag.SETX)
            self.__expression()
        else:
            raise Exception('Syntax Error')
        
    def __leftStatement(self):
        if self.__token.getTag() in self.__firstLeftStatement:
            self.__check(Tag.LEFT)
            self.__expression()
        else:
            raise Exception('Syntax Error')       
             
    def __rightStatement(self):
        if self.__token.getTag() in self.__firstRightStatement:
            self.__check(Tag.RIGHT)
            self.__expression()
        else:
            raise Exception('Syntax Error') 
                   
    def __backwardStatement(self):
        if self.__token.getTag() in self.__firstBackwardStatement:
            self.__check(Tag.BACKWARD)
            self.__expression()
        else:
            raise Exception('Syntax Error')       
             
    def __forwardStatement(self):
        if self.__token.getTag() in self.__firstForwardStatement:
            self.__check(Tag.FORWARD)
            self.__expression()
        else:
            raise Exception('Syntax Error')    
    
    def __movementStatement(self):
        if self.__token.getTag() in self.__firstMovementStatement:
            if self.__token.getTag() == Tag.FORWARD:
                self.__forwardStatement()
            if self.__token.getTag() == Tag.BACKWARD:
                self.__backwardStatement()
            if self.__token.getTag() == Tag.RIGHT:
                self.__rightStatement()
            if self.__token.getTag() == Tag.LEFT:
                self.__leftStatement()
            if self.__token.getTag() == Tag.SETX:
                self.__setXStatement()
            if self.__token.getTag() == Tag.SETY:
                self.__setYStatement()
            if self.__token.getTag() == Tag.SETXY:
                self.__setXYStatement()
        else:
            raise Exception('Syntax Error')      

    def __assigmentStatement(self):
        if self.__token.getTag() in self.__firstAssigmentStatement:
            self.__check(Tag.ID)
            self.__check(Tag.EQ)
            self.__expression()
        else:
            raise Exception('Syntax Error')
        
    def __identifierList(self):
        if self.__token.getTag() in self.__firstIdentifierList:
            self.__check(ord(','))
            self.__check(Tag.ID)
            self.__identifierList()
            
    def __declarationStatement(self):
        if self.__token.getTag() in self.__firstDeclarationStatement:
            self.__check(Tag.VAR)
            self.__check(Tag.ID)
            self.__identifierList()
        else:
            raise Exception('Syntax Error')
    
    def __simpleStatement(self):
        if self.__token.getTag() in self.__firstSimpleStatement:
            if self.__token.getTag() in self.__firstDeclarationStatement:
                self.__declarationStatement()
            if self.__token.getTag() in self.__firstAssigmentStatement:
                self.__assigmentStatement()
            if self.__token.getTag() in self.__firstMovementStatement:
                self.__movementStatement()
            if self.__token.getTag() in self.__firstDrawingStatement:
                self.__drawingStatement()
            if self.__token.getTag() in self.__firstTextStatement:
                self.__textStatement()
        else:
            raise Exception('Syntax Error')
        
    def __statement(self):
        if self.__token.getTag() in self.__firstStatement:
            if self.__token.getTag() in self.__firstSimpleStatement:
                self.__simpleStatement()
            else:
                self.__structuredStatement()
        else:
            raise Exception('Syntax Error')
    
    def __statementSequence(self):
        if self.__token.getTag() in self.__firstStatementSequence:
            if self.__token.getTag() in self.__firstStatement:
                self.__statement()
            else:
                self.__statementSequence()
        
    def __program(self):
        if self.__token.getTag() in self.__firstProgram:
            self.__statementSequence()
        else:
            raise Exception('Sysntax Error')
    
    
            
                