
class FixBraces:
	def __init__(self,input_string):
		self.unbalanced = input_string

	def fixing(self):
		stack,index,remove,result = [],[],[],[]
		unbalanced = self.unbalanced

		for i,j in enumerate(unbalanced):
			if j is ')':
				if stack[len(stack)-1] is '(':
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
		print result








