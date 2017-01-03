class Tree:
	def __init__(self, data):
		#raise "OnlyInteger" if not isinstance(data, int)

		self.data = data
		self.left = None
		self.right = None

	# Recursion Inserting
	def insert(self, data):
		if data < self.data:
			if self.left is not None:
				self.left.insert(data)
			else:
				self.left = Tree(data) 
		else:
			if self.right is not None:
				self.right.insert(data)
			else:
				self.right = Tree(data)

	# Printing using recursion
	def printme(self, tree):
		if tree == None:
			print("Leaf")
		else:
			print tree.data
			tree.printme(tree.left)
			tree.printme(tree.right)

T = Tree(5)
T.insert(4)
T.insert(3)
T.insert(8)
T.insert(9)
T.insert(10)

T.printme(T)