class Node:
	def __init__(self, data):
	        self.data = data
	        self.left = None
	        self.right = None

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
