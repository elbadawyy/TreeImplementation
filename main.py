from Tree import Tree
from Node import Node
my_tree = Tree()


# lvl 3
node_d=Node(12)
node_e=Node(13)
node_f=Node(2)
node_g=Node(10)

#lvl 2

node_b=Node(5,node_d,node_e)
node_c=Node(15,node_f,node_g)


# lvl 1
node_a=Node(9,node_b,node_c)

my_tree.set_root(node_a)




