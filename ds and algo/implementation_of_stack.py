print("this is the implementation of the stack ")
'''
max_size=4
top=0
def enqueue(stack,x):
	global max_size,top
	if len(stack)==max_size:
		print("overflow")

	else:
		print(top)
		stack[top]=x
		top+=1

	return stack 

def dequeue(stack):
	global top
	if len(stack)==0:
		print("underflow")

	else:
		print(f'poped element is->{stack[top]}')
		top-=1

stack=[0]*max_size
enqueue(stack,9)
dequeue(stack)
this is the pure implemetation of the stack but not working 

#simple implementation of the stack using list 

def push(stack,x):

	if len(stack)==4:  # 4 is the sixxe of the stack 
		print("overflow")
		return
	stack.append(x)
		 


def pop(stack):
	if len(stack)==0:
		print("underflow ")
		return 
	stack.pop()


def peek(stack):

	if len(stack)==0:
		print("empty")
		return None

	return stack[len(stack)-1]


stack=[]
push(stack,5)
push(stack,5)
push(stack,6)
print(peek(stack))
pop(stack)
print(stack)


#implementation using deque it privides the insertion and 
#deletion form the both ends 

from collections import deque

stack=deque([9])
print(stack)

#simple append and pop fucntion as like 

#implemeation using lifoqueue

from queue import LifoQueue

stack=LifoQueue(maxsize=8)
stack.put(5)
stack.get()
print(stack) # i added in the queue.py file ownly


# how to implement two stacks in one array
stack1=stack2=[]
array=[None]*10
top1=-1
top2=10
def push(stack,x):
	global  array,top1,top2
	print(stack)
	print(stack == "stack2")
	if stack=="stack1":

		if top1+1==top2:
			print("underflow")
			return


		#in the question this is given that the sum of both
		# stack element is not equal to the whole size of the
		#array
		print(top1)
		top1+=1
		array[top1]=x

	else:

		if top2-1==top1:
			print("overflow")
			return
		array[top2-1]=x
		top2-=1
		return

def pop(stack):
	global array,top1,top2
	# appending in the stack 1
	if stack=="stack1":
		# chekcing for the underflow
		if top1==-1:
			print("underflow")
			return
		# this is the else part 
		print(f'popedd element {array[top1]}')
		array[top1]=None
		top1-=1
	else :

		if top2==10:
			print("underflow ")
			return

		print(f'poped element {array[top2]}')
		array[top2]=None
		top2+=1

push("stack1",4)
print(array )
push("stack2",3)
print(array )
pop("stack1")
print(array )
pop("stack2")
print(array )

# here we make the double ended  circullar
#queue(deque)

array=[None]*10 #sixe of the queue
front=rear=-1
# firstly i am doing the push operations


def isfull():

    return ((front==0 and rear==10) or(front==rear+1))

def isempty():
    return (front==-1)

def head_push(stack,x):
    if isfull():
        print("overflow")
        return
    else
        

def tail_push(stack,x):

    global front ,rear

    if rear>=10:
        print("overflow")
    else:

        if front==-1:
            front+=1
            rear+=1
        else:
            rear+=1
        array[rear]=x

def head_push(stack,x):

    return
'''











