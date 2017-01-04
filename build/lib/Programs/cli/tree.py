class Tree:
	def __init__(self, data):
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
		if tree == None: return
    		print tree.data,
    		tree.printme(tree.left)
    		tree.printme(tree.right)

    # For CLI to get series of inputs. Stops till Negative.
	def get_input(self):
		print "Give Negative Value to Stop Reading Inputs"
		data = 0
		while data >= 0:
			data = int(input())
			self.insert(data)
 










