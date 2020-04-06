from Node import Node


class Tree:
	def __init__(self):
	        self.root = None
	
	# def insert(self, data):
	# 	if(self.root == None):
	# 		self.root = Node(data)			
	# 	else:
	# 		if(self.root.left == None):
	# 			self.root.left = Node(data)
	# 		elif(self.root.right == None):
	# 			self.root.right = Node(data)
	
	def is_empty(self):
		if(self.root == None):
			return 1
		else:
			return 0
		self.root=None

	def set_root(self,node):
		self.root=node

			

	# def inOrder(self):
	# 	if self.is_empty():
	# 		return
	# 	else:
	# 		self.root.left.inOrder()
	# 		print(self.root.data)
	# 		self.root.right.inOrder()

	def get_tree(self):
		print (self.root.data)
		print (self.root.left.data)
		print (self.root.right.data)
		print (self.root.left.right.data)
		print (self.root.left.left.data)
		print (self.root.right.left.data)
		print (self.root.right.right.data)

	
	def inOrder(self,root):
		if root ==None :
			return
		else:
			#print(root.left.data)
			self.inOrder(root.left)
			print(root.data)
			self.inOrder(root.right)
 		
	def get_leafs(self,root):
		if root ==None :
			return
		else:
			if(root.is_leaf()):
				print(root.data)
			self.get_leafs(root.left)
			
			self.get_leafs(root.right)
 		
	


