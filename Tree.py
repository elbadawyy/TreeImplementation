from Node import Node


class Tree:
	root = None

	def insert(self, data):
		if self.root == None:
			new_node = Node(data)
