

from data_structures import Stack


def parenthesis_checker(symbolString):
	""" Read a string of parenthesis from left to right and decide
	whether the symbols are balanced
	"""

	S = Stack()

	#Input are valid
	if symbolString is None:
		raise TypeError("cannot be none")

	if not symbolString:
		raise ValueError("cannot be empty")

	for char in symbolString:
		if char == "(":
			S.push(char)

		elif char == "[":
			S.push(char)
		elif char == "{":
			S.push(char)
			
		else:
			if S.isEmpty():
				return False
			else:
				S.pop()


	return S.isEmpty()


#test case

print(parenthesis_checker("(())"))
print(parenthesis_checker("))"))
print(parenthesis_checker("(()())"))
print(parenthesis_checker("("))