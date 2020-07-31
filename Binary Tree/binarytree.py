'''Queue imported for Reverse order traversals and Level order traversals.'''
import queue 
'''Stack imported fo Level order traversals'''
import stack 
'''Node class initialisation for binary tree'''			
class node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class binarytree:	
	def __init__(self,root):
		self.root = node(root)
	# Binary tree representation.
	
	'''
	   First,	
	   Depth first traversals,
	   they are Pre-order traversals,
	   Post order traversals, In- order traversals. 	
	'''
	def preorder(self, start, string):
		'''Root->Left Subtree->Right Subtree'''
		if start:
			string += (str(start.value) + "-")
			string = self.preorder(start.left, string)
			string = self.preorder(start.right, string)
		return string		
	
	def inorder(self, start , string):	
		'''Left Subtree->Root->Right Subtree'''
		if start:
			string = self.inorder(start.left, string)
			string += (str(start.value) + '-')
			string = self.inorder(start.right , string)
		return string	
	
	def postorder(self, start, string):
		''''Left Subtree->Right Subtree->Root'''
		if start:
			string = self.postorder(start.left, string)
			string = self.postorder(start.right, string)
			string += (str(start.value) + "-")
		return string		
	'''
	   Second,
	   Breadth First Traversals(BFS Traversals)
	   or Level-order Traversals
	'''
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

	def reverselevelorder(self, start):
		'''We print tree from bottom level 
			to top level from left to right fashion
			And we stack and queue both in this problem.
		'''
		if start is None:
			return "Empty Binary Tree or Subtree" 
		Queue = queue.queue()
		Stack = stack.stack()
		Queue.enqueue(start)
		while (len(Queue.items) > 0):
			
			printable = Queue.dequeue()

			if (printable.right != None):
				Queue.enqueue(printable.right)
			
			if (printable.left != None):	
				Queue.enqueue(printable.left)

			Stack.push(printable.value)	
		return Stack.show()

	def height(self, start):
		'''
		   Height of a node is 1 + 
		   max(height(left subtree), height(right subtree)) 
		'''
		'''
		   If node is empty return its height as -1, so that leaves have height 0
		'''
		if start is None:
			return -1
		else:	
			Height = 1 + max(self.height(start.left), self.height(start.right))
			return Height		
if __name__ == "__main__":
	tree = binarytree(3)
	tree.root.left = node(4)
	tree.root.right = node(5)
	tree.root.left.left = node(6)
	tree.root.left.right = node(7)
	tree.root.right.left = node(8)
	tree.root.left.left.left = node(9)

	print("Array representation: ", [3,4,5,6,7,8,9])
	print('-------------')
	print("Preorder: ", tree.preorder(tree.root, ""))
	print("Inorder: ", tree.inorder(tree.root, ""))
	print("Postorder: ", tree.postorder(tree.root, ""))
	print("Level-order: ", tree.levelorder(tree.root))
	print("Reverse Level-order: ", tree.reverselevelorder(tree.root))
	print('--------------')
	print("Height of tree: ", tree.height(tree.root))