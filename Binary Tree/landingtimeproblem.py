import queue 
class node(object):

	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None


class BST(object):

	def __init__(self, root):
		self.root = node(root)

	def left_child(self, node):
		return	node.left

	def right_child(self, node):
		return node.right			

	def levelorder(self, start):
		'''We use queue to print this.
		   We print nodes from top level
		   to bottom level from left to right fashion.'''
		if start is None:
			return "Empty Binary Tree or Subtree" 
		arr = []	
		Queue = queue.queue()
		Queue.enqueue(start)
		while (len(Queue.items) > 0):
			
			printable = Queue.dequeue()

			if (printable.left != None):
				Queue.enqueue(printable.left)
			
			if (printable.right != None):	
				Queue.enqueue(printable.right)

			arr.append(printable.value)	
		return arr	

	def insert(self, value, k):
		if self.root == None:
			self.root = node (value)		

		else:	
			temp = self.root
			while True:
				if abs(temp.value - value) >= k:
					if temp.value > value :
						if temp.left == None:
							temp.left = node(value)
							return "Value added to set R"
						temp = temp.left	

					else:
						if temp.right == None:
							temp.right = node(value)
							return "Value added to set R"

						temp = temp.right		
				else:
					return "The landing time you request was not fulfilling our criteria. "	

	def find_min(self):
		temp = self.root
		while (temp.left != None):
			temp = temp.left
		return temp.value

	def find_max(self):
		temp = self.root
		while (temp.right != None):
			temp = temp.right
		return temp.value		
	def find_value(self, value):
		temp = self.root
		while True:
			try:
				if temp.value == value:
					break
				elif temp.value >value:
					temp = temp.left
				else:
					temp = temp.right
			except:
				break		
			
		if temp == None:
			return "Not found"
		else:
			return "Found"				

if __name__ == "__main__":
	bst = BST(5)
	bst.insert(15,3)
	bst.insert(1,3)
	bst.insert(-9,3)
	bst.insert(-14,3)
	bst.insert(20,3)
	print(bst.levelorder(bst.root))
	print(bst.find_min())
	print(bst.find_max())
	print(bst.find_value(-9))

