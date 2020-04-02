'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def has_left(self):
        if self.left == None:
            return 1
        else:
            return 0

    def has_right(self):    
        if self.right == None:
            return 1
        else:
            return 0

    def insert(self,data):
        if self.data:
            
            if self.left == None:
                self.left = Node(data)
            
            elif self.right == None:
                self.right = Node(data)
            
            else:
                
                if self.left.has_left() | self.left.has_right() :
                    self.left.insert(data)
                
                elif self.right.has_left() | self.right.has_right() :
                    self.right.insert(data)
        else:
            self = Node(data)

    def getTree(self):
        if self.left:
            self.left.getTree()
            print( self.data),

        if self.right:
            self.right.getTree()

    def is_empty(self):
        if self.data == None:
            print("empty")
        else:
            print("non empty")

root = Node(20)
root.insert(11)
root.insert(25)
root.insert(10)
root.insert(30)
root.insert(19)
root.getTree()
root.is_empty()