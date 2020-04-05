from Node import Node


class Tree:
	def __init__(self):
		self.root=None

	def set_root(self,node):
		self.root=node

	

	
	def insert2(self, data):
		new_node = Node(data)

		if self.root == None:
			self.root = new_node
		else:
			self.__insert_a_not_root_node(self.root,new_node)

	def __insert_a_not_root_node(self,current_node ,new_node,perviuos_node=None):
		if current_node.right == None and current_node.left != None:
			current_node.right = new_node
			return
			
		elif current_node.right == None and current_node.left == None:
			current_node.left = new_node
			return
		else:
			self.__insert_a_not_root_node(current_node.right,new_node)
			self.__insert_a_not_root_node(current_node.left,new_node,current_node)
		
		



