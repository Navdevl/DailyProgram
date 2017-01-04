
class FixBraces:
	# Setting the input string
	def __init__(self,input_string):
		self.unbalanced = input_string

	def fixing(self):
		# Declaring lists for few processing
		stack,index,remove,result = [],[],[],[]
		unbalanced = self.unbalanced

		for i,j in enumerate(unbalanced):
			if j is ')':
				if stack[len(stack)-1] is '(':
					# Storing the index of elements to remove/ignore
					remove.append(i)
					remove.append(index.pop())
					stack.pop()

				else:
					rev = stack[::-1]
					pos = len(stack) - 1 - rev.index('(') if '(' in stack else -1
					if pos is not -1:
						stack,index = stack[:pos], index[:pos]
			else:
				stack.append(j)
				index.append(i)

		for i in range(len(unbalanced)):
			if(i not in remove):
				result.append(unbalanced[i])

		result = ''.join(result)
		return result

class Tree:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	# Recursion Inserting
	def insert(self,data):
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
	def printme(self,tree):
		
		if tree == None: return
    		print tree.data,
    		tree.printme(tree.left)
    		tree.printme(tree.right)

    # For CLI to get series of inputs. Stops till Negative.
	def get_input(self):
		data = 0
		while data >= 0:
			data = int(input())
			self.insert(data)
 










