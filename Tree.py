from Node import Node


class Tree:
	def __init__(self):
	        self.root = None
	
	def insert(self, data):
		if(self.root == None):
			self.root = Node(data)			
		else:
			if(self.root.left == None):
				self.root.left = Node(data)
			elif(self.root.right == None):
				self.root.right = Node(data)
	
	def is_empty(self):
		if(self.root == None):
			return 1
		else:
			return 0

							

	def inOrder(self):
		if self.is_empty():
			return
		else:
			self.root.left.inOrder()
			print(self.root.data)
			self.root.right.inOrder()
	
	def get_tree(self):
		print (self.root.data)
		print (self.root.left.data)
		print (self.root.right.data)
		print (self.root.left.right.data)
		print (self.root.left.left.data)
		print (self.root.right.left.data)
		print (self.root.right.right.data)

	

 		
	


