from Node import Node


class Tree:
	root = None

	def insert(self, data):
		new_node = Node(data)

	if self.root == None:
		self.root = new_node
	else:
		self.__insert_a_not_root_node(self.root,new_node)

	def __insert_a_not_root_node(self,current_node ,new_node):
		if current_node.right == None && current_node.left != None:
			current_node.right = new_node
			
		elif current_node.right == None && current_node.left == None:
			current_node.left = new_node
		



