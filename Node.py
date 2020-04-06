class Node:
	def __init__(self, data, right=None, left=None):
		self.data = data
		self.left = left
		self.right = right

	def is_leaf(self):
		if (self.left == None and self.right == None):
			return 1
		else:
			return 0

	def has_left(self):
		if(self.left != None):
			return 1

	def has_right(self):
		if(self.right != None):
			return 1
