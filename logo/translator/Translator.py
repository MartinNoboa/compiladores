from Environment import *
from Type import *
import turtle

#------------------------- Base class && classes --------------------------#
class Node:
	def __init__(self, line = None):
		self._line = line

	def eval(self, env, aTurtle):
		pass

class Numeric(Node):
	def __init__(self, line = None):
		super().__init__(line)

	def eval(self, env, aTurtle):
		pass

class Logic(Node):
	def __init__(self, line = None):
		super().__init__(line)

	def eval(self, env, aTurtle):
		pass

class Character(Node):
	def __init__(self, line = None):
		super().__init__(line)

	def eval(self, env, aTurtle):
		pass

class Void(Node):
	def __init__(self, line = None):
		super().__init__(line)

	def eval(self, env, aTurtle):
		pass
#------------------------- Base class && classes --------------------------#

#--------------------------- Numeric Subclasses ---------------------------#
class Number(Numeric):
	def __init__(self, value, line = None):
		super().__init__(line)
		self.__value = value
	
	def eval(self, env, a_turtle):
		return self.__value
	
class Identifier(Numeric):
	def __init__(self, name, line):
		super().__init__(line)
		self.__name = name

	def eval(self, env, aTurtle):
		result = env.lookup(self.__name)
		if result != None:
			(_, value) = result
			return value
		else:
			text = 'Line ' + self._line + " - " + self.__name + " has not been declared"
			raise Exception(text)
	
class Minus(Numeric):
	def __init__(self, right, line = None):
		super().__init__(line)
		self.__right = right

	def eval(self, env, aTurtle):
		return -1 * float(self._right.eval(env, aTurtle))
	
class Add(Numeric):
	def __init__(self, left, right, line = None):
		super().__init__(line)
		self.__left = left
		self.__right = right

	def eval(self, env, aTurtle):
		left = float(self.__left.eval(env, aTurtle))
		right = float(self.__right.eval(env, aTurtle))
		return (left + right)

class Substract(Numeric):
	def __init__(self, left, right, line = None):
		super().__init__(line)
		self.__left = left
		self.__right = right

	def eval(self, env, aTurtle):
		left = float(self.__left.eval(env, aTurtle))
		right = float(self.__right.eval(env, aTurtle))
		return (left - right)

class Multiply(Numeric):
	def __init__(self, left, right, line = None):
		super().__init__(line)
		self.__left = left
		self.__right = right

	def eval(self, env, aTurtle):
		left = float(self.__left.eval(env, aTurtle))
		right = float(self.__right.eval(env, aTurtle))
		return (left * right)

class Divide(Numeric):
	def __init__(self, left, right, line = None):
		super().__init__(line)
		self.__left = left
		self.__right = right

	def eval(self, env, aTurtle):
		left = float(self.__left.eval(env, aTurtle))
		right = float(self.__right.eval(env, aTurtle))
		return (left / right)

class Module(Numeric):
	def __init__(self, left, right, line = None):
		super().__init__(line)
		self.__left = left
		self.__right = right

	def eval(self, env, aTurtle):
		left = float(self.__left.eval(env, aTurtle))
		right = float(self.__right.eval(env, aTurtle))
		return (left % right)
	

#--------------------------- Numeric Subclasses ---------------------------#
#---------------------------- Logic Subclasses ----------------------------#
class Boolean(Logic):
	def __init__(self, value, line = None):
		super().__init__(line)
		self.__value = value
		
	def eval(self, env, a_turtle):
		return self.__value
	
class Not(Logic):
	def __init__(self, right, line = None):
		super().__init__(line)
		self.__right = right

	def eval(self, env, aTurtle):
		return not(bool(self.__right.eval(env, aTurtle)))
	
class Not(Logic):
	def __init__(self, right, line):
		super().__init__(line)
		self.__right = right

	def eval(self, env, a_turtle):
		if not(isinstance(self.__right, Logic)):
			text = 'Line ' + str(self._line) + " - the expression must be boolean."
			raise Exception(text)
	
class Lesser(Logic):
	def __init__(self, left, right, line = None):
		super().__init__(line)
		self.__left = left
		self.__right = right

	def eval(self, env, aTurtle):
		left = float(self.__left.eval(env, aTurtle))
		right = float(self.__right.eval(env, aTurtle))
		return (left < right)

class LesserOrEqual(Logic):
	def __init__(self, left, right, line = None):
		super().__init__(line)
		self.__left = left
		self.__right = right

	def eval(self, env, aTurtle):
		left = float(self.__left.eval(env, aTurtle))
		right = float(self.__right.eval(env, aTurtle))
		return (left <= right)

class Greater(Logic):
	def __init__(self, left, right, line = None):
		super().__init__(line)
		self.__left = left
		self.__right = right

	def eval(self, env, aTurtle):
		left = float(self.__left.eval(env, aTurtle))
		right = float(self.__right.eval(env, aTurtle))
		return (left > right)

class GreaterOrEqual(Logic):
	def __init__(self, left, right, line = None):
		super().__init__(line)
		self.__left = left
		self.__right = right

	def eval(self, env, aTurtle):
		left = float(self.__left.eval(env, aTurtle))
		right = float(self.__right.eval(env, aTurtle))
		return (left >= right)

class Equal(Logic):
	def __init__(self, left, right, line = None):
		super().__init__(line)
		self.__left = left
		self.__right = right

	def eval(self, env, aTurtle):
		left = float(self.__left.eval(env, aTurtle))
		right = float(self.__right.eval(env, aTurtle))
		return (left == right)

class Different(Logic):
	def __init__(self, left, right, line = None):
		super().__init__(line)
		self.__left = left
		self.__right = right

	def eval(self, env, aTurtle):
		left = float(self.__left.eval(env, aTurtle))
		right = float(self.__right.eval(env, aTurtle))
		return (left != right)
	
# LesserOrEqual, Greater, GreaterOrEqual, Equal, Different

class And(Boolean):
	def __init__(self, left, right, line = None):
		super().__init__(line)
		self.__left = left
		self.__right = right

	def eval(self, env, aTurtle):
		left = bool(self.__left.eval(env, aTurtle))
		right = bool(self.__right.eval(env, aTurtle))
		return (left and right)

class Or(Boolean):
	def __init__(self, left, right, line = None):
		super().__init__(line)
		self.__left = left
		self.__right = right

	def eval(self, env, aTurtle):
		left = bool(self.__left.eval(env, aTurtle))
		right = bool(self.__right.eval(env, aTurtle))
		return (left or right)

# Or 
#---------------------------- Logic Subclasses ----------------------------#
#--------------------------- String Subclasses ----------------------------#
class If(Void):
	def __init__(self, condition, sequence, line = None):
		super().__init__(line)
		self.__condition = condition
		self.__sequence = sequence

	def eval(self, env, aTurtle):
		env = Environment(env)
		if bool(self.__condition.eval(env, aTurtle)):
			self.__sequence.eval(env, aTurtle)
		env = env.getPrevious()

class IfElse(Void):
	def __init__(self, condition, ifSequence, elseSequence, line = None):
		super().__init__(line)
		self.__condition = condition
		self.__ifSequence = ifSequence
		self.__elseSequence = elseSequence

	def eval(self, env, aTurtle):
		env = Environment(env)
		if bool(self.__condition.eval(env, aTurtle)):
			self.__ifSequence.eval(env, aTurtle)
		else:
			self.__elseSequence.eval(env, aTurtle)
		env = env.getPrevious()

class Repeat(Void):
	def __init__(self, expression, sequence, line = None):
		super().__init__(line)
		self.__expression = expression
		self.__sequence = sequence

	def eval(self, env, aTurtle):
		times = int(self.__expression.eval(env, aTurtle))
		for i in range(times):
			env = Environment(env)
			self.__sequence.eval(env, aTurtle)
			env = env.getPrevious()

class While(Void):
	def __init__(self, expression, sequence, line = None):
		super().__init__(line)
		self.__expression = expression
		self.__sequence = sequence

	def eval(self, env, aTurtle):
		condition = int(self.__expression.eval(env, aTurtle))
		while(condition):
			env = Environment(env)
			self.__sequence.eval(env, aTurtle)
			env = env.getPrevious()

class Print(Void):
	def __init__(self, element, elementList = None, line = None):
		super().__init__(line)
		self.__element = element
		self.__elementList = elementList

	def eval(self, env, aTurtle):
		text = self.__element.eval(env, aTurtle)
		if self.__elementList != None:
			text = text + " " + self.__elementList.eval(env, aTurtle)
		aTurtle.write(text)

class PenWidth(Void):
	def __init__(self, expression, line = None):
		super().__init__(line)
		self.__expression = expression

	def eval(self, env, aTurtle):
		value = int(self.__expression.eval(env, aTurtle))
		aTurtle.pensize(value)

class Color(Void):
	def __init__(self, redExpression, greenExpression, blueExpression, line = None):
		super().__init__(line)
		self.__redExpression = redExpression
		self.__greenExpression = greenExpression
		self.__blueExpression = blueExpression

	def eval(self, env, aTurtle):
		red = int(self.__redExpression.eval(env, aTurtle))
		if red < 0 or red > 255:
			text = 'Line ' + self._line + "expected a positive number between 0..255 in the red value."
			raise Exception(text)
		green = int(self.__greenExpression.eval(env, aTurtle))
		if green < 0 or green > 255:
			text = 'Line ' + self._line + "expected a positive number between 0..255 in the blue value."
			raise Exception(text)
		blue = int(self.__blueExpression.eval(env, aTurtle))
		if blue < 0 or blue > 255:
			text = 'Line ' + self._line + "expected a positive number between 0..255 in the green value."
			raise Exception(text)
		aTurtle.pencolor(red, green, blue)

class PenDown(Void):
	def __init__(self, line = None):
		super().__init__(line)

	def eval(self, env, aTurtle):
		aTurtle.pendown()

class PenUp(Void):
	def __init__(self, line = None):
		super().__init__(line)

	def eval(self, env, aTurtle):
		aTurtle.penup()

class Arc(Void):
	def __init__(self, ratioExpression, angleExpression, line = None):
		super().__init__(line)
		self.__ratioExpression = ratioExpression
		self.__angleExpression = angleExpression

	def eval(self, env, aTurtle):
		ratio = int(self.__ratioExpression.eval(env, aTurtle))
		angle = int(self.__angleExpression.eval(env, aTurtle))
		aTurtle.circle(ratio, angle)

class Circle(Void):
	def __init__(self, ratioExpression, line = None):
		super().__init__(line)
		self.__ratioExpression = ratioExpression

	def eval(self, env, aTurtle):
		ratio = int(self.__ratioExpression.eval(env, aTurtle))
		aTurtle.circle(ratio)

class Clear(Void):
	def __init__(self, line = None):
		super().__init__(line)
		

	def eval(self, env, aTurtle):
		aTurtle.clear()
  
class SetXY(Void):
	def __init__(self, xExpression, yExpression, line = None):
		super().__init__(line)
		self.__xExpression = xExpression
		self.__yExpression = yExpression

	def eval(self, env, aTurtle):
		x = int(self.__xExpression.eval(env, aTurtle))
		y = int(self.__yExpression.eval(env, aTurtle))
		aTurtle.setXY(x, y)

class SetX(Void):
	def __init__(self, xExpression, line = None):
		super().__init__(line)
		self.__xExpression = xExpression

	def eval(self, env, aTurtle):
		x = int(self.__xExpression.eval(env, aTurtle))
		aTurtle.setX(x)

class SetY(Void):
	def __init__(self, xExpression, line = None):
		super().__init__(line)
		self.__yExpression = xExpression

	def eval(self, env, aTurtle):
		y = int(self.__yExpression.eval(env, aTurtle))
		aTurtle.setX(y)

class Left(Void):
	def __init__(self, leftValue, line = None):
		super().__init__(line)
		self.__leftValue = leftValue

	def eval(self, env, aTurtle):
		left = int(self.__leftValue.eval(env, aTurtle))
		aTurtle.left(left)
  
class Right(Void):
	def __init__(self, rightValue, line = None):
		super().__init__(line)
		self.__rightValue = rightValue

	def eval(self, env, aTurtle):
		right = int(self.__rightValue.eval(env, aTurtle))
		aTurtle.right(right)

class Forward(Void):
	def __init__(self, forwardValue, line = None):
		super().__init__(line)
		self.__forwardValue = forwardValue

	def eval(self, env, aTurtle):
		forward = int(self.__forwardValue.eval(env, aTurtle))
		aTurtle.forward(forward)

class Backward(Void):
	def __init__(self, backwardValue, line = None):
		super().__init__(line)
		self.__backwardValue = backwardValue

	def eval(self, env, aTurtle):
		backward = int(self.__backwardValue.eval(env, aTurtle))
		aTurtle.backward(backward)

class Home(Void):
	def __init__(self, line = None):
		super().__init__(line)

	def eval(self, env, aTurtle):
		aTurtle.home()

class Arc(Void):
	def __init__(self, ratioExpression, angleExpression, line = None):
		super().__init__(line)
		self.__ratioExpression = ratioExpression
		self.__angleExpression = angleExpression

	def eval(self, env, aTurtle):
		ratio = int(self.__ratioExpression.eval(env, aTurtle))
		angle = int(self.__angleExpression.eval(env, aTurtle))
		aTurtle.circle(ratio, angle)


class Assigment(Void):
	def __init__(self, id, expression, line):
		super().__init__(line)
		self.__id = id
		self.__expression = expression

	def eval(self, env, aTurtle):
		value = self.__expression.eval(env, aTurtle)

		type = None
		if isinstance(self.__expression, Numeric): 
			type = Type.NUMBER
			value = float(value)
		else: 
			type = Type.BOOLEAN
			value = bool(value)

		if not(env.set(self.__id, type, value)):
			text = 'Line ' + str(self._line) + " - " + self.__id + " is not declared"
			raise Exception(text)
		
class IdDeclaration(Void):
	def __init__(self, id, line = None):
		super().__init__(line)
		self.__id = id

	def eval(self, env, aTurtle):
		if not env.insert(self.__id):
			text = 'Line ' + self._line + " - redeclaration of " + str(self.__id)
			raise Exception(text)

class idDeclarationList(Void):
	def __init__(self, idDeclaration, idDeclarationList = None, line = None):
		super().__init__(line)
		self.__idDeclaration = idDeclaration
		self.__idDeclarationList = idDeclarationList

	def eval(self, env, aTurtle):
		self.__idDeclaration.eval(env, aTurtle)
		if self.__idDeclarationList != None:
			self.__idDeclarationList.eval(env, aTurtle)

class Declaration(Void):
	def __init__(self, idDeclaration, idDeclarationList = None, line = None):
		super().__init__(line)
		self.__idDeclaration = idDeclaration
		self.__idDeclarationList = idDeclarationList

	def eval(self, env, aTurtle):
		self.__idDeclaration.eval(env, aTurtle)
		if self.__idDeclarationList != None:
			self.__idDeclarationList.eval(env, aTurtle)

class StatementSequence(Void):
	def __init__(self, statement, statementSequence = None, line = None):
		super().__init__(line)
		self.__statement = statement
		self.__statementSequence = statementSequence

	def eval(self, env, aTurtle):
		self.__statement.eval(env, aTurtle)
		if self.__statementSequence != None:
			self.__statementSequence.eval(env, aTurtle)

class Program(Void):
	def __init__(self, statementSequence, line = None):
		super().__init__(line)
		self.__statementSequence = statementSequence

	def eval(self, env, aTurtle):
		pass

	def eval(self):
		myEnv = Environment()

		myScreen = turtle.getscreen()
		myTurtle = turtle.Turtle()  
		turtle.mode("logo")
		turtle.colormode(255)

		self.__statementSequence.eval(myEnv, myTurtle)

		turtle.done()
#----------------------------- Void Subclasses ----------------------------#