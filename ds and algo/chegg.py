'''
class glofer:

	def __init__(self,name1,score1):
		
		self.name1=name1
		self.score1=score1
		

	def cmp(self,name,score):

		if self.score1<score:
			return 1
		elif self.score1==score:
			return 0
		else:
			return -1

object_of_glofer=glofer("python",2)
print(object_of_glofer.cmp("java",0))

def readfile(filemane):
	with open(filemane.txt, 'r') as f:  # Open file for read
	    for line in f:           # Read line-by-line
	        line = line.strip()  # Strip the leading/trailing whitespaces and newline
	        # Process the line

def Wordfrolinelist(listt):
	s=set()
	for i in listt.split(" "):
		s.add(i)
	return list(s)

from collection import Counter

def countFrequency(listt):
	dict_1=Counter(listt)
	freq=[]
	for i in dict_1.keys():
		freq.append((i,dict_1[i]))


	return tuple(freq)

def merge_sortase(arr, key=lambda x: x):

	# this the iterative code of thhe merge sort
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sortase(left)
    merge_sortase(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr
def merge_sortdse(arr, key=lambda x: x):

	# this the iterative code of thhe merge sort
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sortdse(left)
    merge_sortdse(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if key(left[i]) > key(right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


def mergesort(arr,n,ascending):
	if (ascending):

		print(merge_sortase(arr, key=lambda x: x[n]))
	else:
		print(merge_sortdse(arr, key=lambda x: x[n]))





def partitionase(arr, low, high,key=lambda x: x[n])): 
    i = (low-1)         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low, high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if arr[j] <= pivot: 
  
            # increment index of smaller element 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
  
  
def quickSortase(arr, low, high): 
    if len(arr) == 1: 
        return arr 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partitionase(arr, low, high,key=lambda x: x[n]) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSortase(arr, low, pi-1,n) 
        quickSortase(arr, pi+1, high,n)

def partitiondes(arr, low, high,key=lambda x: x[n])): 
    i = (low-1)         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low, high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if arr[j] > pivot: 
  
            # increment index of smaller element 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
  
  
def quickSortdes(arr, low, high): 
    if len(arr) == 1: 
        return arr 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partitiondes(arr, low, high,key=lambda x: x[n]) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSortdes(arr, low, pi-1,n) 
        quickSortdes(arr, pi+1, high,n)

def quicksort(arr,n,ascending):
	if (ascending):

		print(quick_sortase(arr,n))
	else:
		print(quick_sortdse(arr, n))



from datetime import datetime,date,time

now = datetime.now()


current_time = now.strftime("%I ")


print("Current Time =", current_time)
age=int(input("Enter your age :"))

if 12<= int(current_time) <= 15:
		print("The cost of the ticket:	$5.00")
elif age<13 or age>65:
	print("The cost of the ticket:	$5.00")
elif 13<=age<=17:
	print("The cost of the ticket:	$7.50")
else:
	print("The cost of the ticket:	$10.00")

from collection import defaultdict

answer = defaultdict(list)
prename = ''
for data in game_data:
	line = data.strip()
	if line.isnumeric():

		answer[prename].append(int(line))
	else:
		prename = line
		answer[prename] = []
print(answer)


class node:


	def __init__(self,data):
		self.data=data

		self.right=None
		self.left=None
		self.up=None

class tree:

	

		
	def out(self,root):

		if root.data is None:
			return 

		print(root.data)
		if root.left is not None:
			self.out(root.left)
		if root.right is not Non
		self.out(root.right)
		self.out(root.up)

root=node("A")
root.right=node("c")
root.left=node("B")
root.right.up=root
root.left.up=root
obj=tree()
obj.out(root)


class node:

	def __init__(self,data=None):
		self.data=data
		self.next=None

newlist=node()
def pair(head1,head2):

	global newlist
	if head2 is None and head1 is None:
		return

	newlist.next=node((head1.data,head2.data))
	pair(head1.next,head2.next)

def printing(head):

	if head is None:
		return

	while head is not None:
		print(head.data)

head1=node("saurabh")
head2=node("saurabh")
pair(head1,head2)
printing(newlist)




def main():

	flag=True
	dict_1={}

	while flag:

		print("add(a),remove(r),find(f)")
		choice=input()

		if choice=="a":
			key=input("key")
			value=input("value")
			if key in dict_1:
				print("'already in the dict")
			else :

				dict_1[key]=value
		elif choice=="r":
			key=input(" key")
			if key not in dict_1:
				print("no such key in the dict")
			else:
				dict_1.pop(key)
		elif choice=="f":
			key=input("key")
			if key not in dict_1:
				print("there is no such key")
			else:
				print(dict_1[key])

		print("More[Y/N]")
		n=input()
		if n=="N":
			flag=False

	print(dict_1)


main()





import is_prime

n=int(input("Enter the number:-"))

for i in range(2,n+1):

	if is_prime.prime(i):
		print(str(i)+" ",end=" ")

'''

class node:

    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


def max(root):

    queue=[]

    return


def tree_Count(root):

    if root is None:
        return 0

    queue = []

    queue.append(root)

    count = 0
    while (len(queue) > 0):
        node = queue.pop(0)

        if node.left is not None and node.right is not None:
            count = count + 1

        if node.left is not None:
            queue.append(node.left)

            # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

    return count

def tree_print(root):

    if root is None:
        return

    print(root.data)
    tree_print(root.left)
    tree_print(root.right)

single_child_nodes = []
def tree_count_1_child(root):
    # Base Case
    if not root:
        return

    # Condition to check if the node
    # is having only one child
    if not root.left and root.right:
        single_child_nodes.append(root)
    elif root.left and not root.right:
        single_child_nodes.append(root)

    # Traversing the left child
    tree_count_1_child(root.left)

    # Traversing the right child
    tree_count_1_child(root.right)
    return


def tree_sum(root):
    if (root == None):
        return 0
    return (root.key + tree_sum(root.left) +tree_sum(root.right))


def tree_print_leaves(root):
    # If node is null, return
    if (not root):
        return

    # If node is leaf node,
    # print its data
    if (not root.left and
            not root.right):
        print(root.data,
              end=" ")
        return

    # If left child exists,
    # check for leaf recursively
    if root.left:
        tree_print_leaves(root.left)

    # If right child exists,
    # check for leaf recursively
    if root.right:
        tree_print_leaves(root.right)


def bst_search(root, key):
    # Traverse untill root reaches
    # to dead end
    while root != None:

        # pass right subtree as new tree
        if key > root.data:
            root = root.right

            # pass left subtree as new tree
        elif key < root.data:
            root = root.left
        else:
            return True  # if the key is found return 1
    return False

def tree_search(root, key):
    # Traverse untill root reaches
    # to dead end
    while root != None:

        # pass right subtree as new tree
        if key > root.data:
            root = root.right

            # pass left subtree as new tree
        elif key < root.data:
            root = root.left
        else:
            return True  # if the key is found return 1
    return False


def tree_bst_max(root):
    if root is None:
        print("Tree is empty")
        return

    current = root
    pre = node(0)

    # Max variable for storing maximum value
    max_value = -999999999999999

    # Min variable for storing minimum value


    while current is not None:

        # If left child does nor exists
        if current.left is None:
            max_value = max(max_value, current.key)


            current = current.right
        else:

            # Find the inorder predecessor of current
            pre = current.left
            while pre.right is not None and pre.right != current:
                pre = pre.right

                # Make current as the right child
            # of its inorder predecessor
            if pre.right is None:
                pre.right = current
                current = current.left

                # Revert the changes made in the 'if' part to
            # restore the original tree i.e., fix the
            # right child of predecessor
            else:
                pre.right = None
                max_value = max(max_value, current.key)


                current = current.right

                # End of if condition pre->right == NULL

        # End of if condition current->left == NULL

    # End of while

    # Finally print max and min value
    print("Max value is :", max_value)

def tree_max(root):
    if root is None:
        print("Tree is empty")
        return

    current = root
    pre = node(0)

    # Max variable for storing maximum value
    max_value = -999999999999999

    # Min variable for storing minimum value


    while current is not None:

        # If left child does nor exists
        if current.left is None:
            max_value = max(max_value, current.key)


            current = current.right
        else:

            # Find the inorder predecessor of current
            pre = current.left
            while pre.right is not None and pre.right != current:
                pre = pre.right

                # Make current as the right child
            # of its inorder predecessor
            if pre.right is None:
                pre.right = current
                current = current.left

                # Revert the changes made in the 'if' part to
            # restore the original tree i.e., fix the
            # right child of predecessor
            else:
                pre.right = None
                max_value = max(max_value, current.key)


                current = current.right

                # End of if condition pre->right == NULL

        # End of if condition current->left == NULL

    # End of while

    # Finally print max and min value
    print("Max value is :", max_value)


