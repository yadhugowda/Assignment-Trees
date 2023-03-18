
class Node:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None
		

def findDepth(root, x):
	
	
	if (root == None):
		return -1

	
	dist = -1


	if (root.data == x):
		return dist + 1

	dist = findDepth(root.left, x)
	if dist >= 0:
		return dist + 1
	dist = findDepth(root.right, x)
	if dist >= 0:
		return dist + 1
	return dist


def findHeightUtil(root, x):
	global height

	
	if (root == None):
		return -1


	leftHeight = findHeightUtil(root.left, x)

	rightHeight = findHeightUtil(root.right, x)

	
	ans = max(leftHeight, rightHeight) + 1

	
	if (root.data == x):
		height = ans

	return ans


def findHeight(root, x):
	global height


	maxHeight = findHeightUtil(root, x)

	
	return height


if __name__ == '__main__':
	
	
	height = -1
	root = Node(5)
	root.left = Node(10)
	root.right = Node(15)
	root.left.left = Node(20)
	root.left.right = Node(25)
	root.left.right.right = Node(45)
	root.right.left = Node(30)
	root.right.right = Node(35)

	k = 25

	
	print("Depth: ",findDepth(root, k))

	
	print("Height: ",findHeight(root, k))

	
