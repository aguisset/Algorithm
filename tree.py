#!/usr/bin/env python


from data_structures import Stack 
from data_structures import BinaryTree


def buildParseTree(fpexp):
	exp_list = fpexp.split() # split the expression in a list wth the delimateur being space
	stack = Stack()
	current_node = BinaryTree('')

	tokens = ['+', '-', '/', '*']

	#stack.push(current_node)
	
	for char in exp:

		if char == '(':

			current_node.insertLeft('')
			S.push(current_node) # push parent into the stack
			current_node = current_node.leftChild

		elif char.isdigit():

			current_node.key = int(char)

			current_node = S.pop()

		elif char in tokens:
			current_node.insertRight('')
			current_node.key = char
			S.push(current_node)
			current_node = current_node.rightChild

		elif char == ')':
			current_node = S.pop()

		else:
			raise ValueError

def main():

	pt = buildParseTree("( ( 10 + 5 ) * 3 )")
	pt.postorder()

if '__name__' = '__main__':

	main()


