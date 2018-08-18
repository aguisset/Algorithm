#!/usr/bin/env python


class Stack(object):

	def __init__(self):
		self.items = []

	def push(self,item):
		return self.items.append(item)

	def pop(self):
		if not self.items:
			raise ValueError("underflow")
		
		return self.items.pop()

	def isEmpty(self):
		return self.items == []

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)





class BinaryTree(object):

	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.left is None:
			self.left = newNode
		else:
			t = BinaryTree(newNode)
			t.left = self.leftChild
			self.leftChild = t

	def insertRight(self, newNode):
		if self.right is None:
			self.right = newNode
		else:
			t = BinaryTree(newNode)
			t.right = self.leftChild
			self.rightChild = t

