########################## PRAC 1 ##############################################
"""
m=int(input("Enter no of rows in matrix"))
n=int(input("Enter no of columns in matrix1"))
mat1=[]
for i in range(0,m):
      mat1.append([])
      for j in range(0,n):
          mat1[i].append(j)
          mat1[i][j]=0
          print("Entry in row:",i+1,"column:",j+1)
          mat1[i][j]=int(input())
print (mat1)
p=int(input("Enter no of rows in matrix2"))
q=int(input("Enter no of colums in matrix2"))
mat2=[]
for i in range(0,p):
     mat2.append([])
for i in range(0,p):
      for j in range(0,q):
            mat2[i].append(j)
            mat2[i][j]=0
            print("Entry in row:",i+1,"column:",j+1)
            mat2[i][j]=int(input())
print(mat2)
res=[]
for i in range(0,m):
      res.append([])
for i in range(0,m):
    for j in range(0,q):
        res[i].append(j)
        res[i][j]=0
for p in range(len(mat1)):
      for q in range(len (mat2)):
          for r in range(len(mat2)):
                res[p][q]+=mat1[p][r]*mat2 [r][q]
print("Result of Matrix Multiplication is")
print(res)
"""
################## PRAC 2 #########################################

"""
def quick(mylist):
    quicksort(mylist,0,len(mylist)-1)
def quicksort(mylist,first,last):
    if first < last:
        q=partition(mylist,first,last)
        quicksort(mylist,first,q-1)
        quicksort(mylist,q+1,last)
def partition(mylist,first,last):
    pivotelement = mylist[first]
    leftvalue = first+1
    rightvalue = last
    done = False
    while not done:
        while leftvalue <= rightvalue and mylist[leftvalue] <= pivotelement:
            leftvalue = leftvalue+1
        while mylist[rightvalue] >= pivotelement and rightvalue >= leftvalue:
            rightvalue = rightvalue-1
        if rightvalue < leftvalue:
            done = True
        else:
            temp = mylist[leftvalue]
            mylist[leftvalue] = mylist[rightvalue]
            mylist[rightvalue] = temp
    temp = mylist[first]
    mylist[first] = mylist[rightvalue]
    mylist[rightvalue] = temp
    return rightvalue
mylist = ['java','android','cn','laup','foa']
print("before applying quick sort technique:",mylist)
quick(mylist)
print("after applying quick sort technique:",mylist)
"""

################### PRAC 3 ##########################################
"""
def mergeSort(list):
    print("Splitting",list)
    if len(list) > 1:
        mid = len(list)//2
        lefthalf = list[:mid]
        righthalf = list[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i = i+1
            else:
                list[k] = righthalf[j]
                j = j+1
            k = k+1
        while i < len(lefthalf):
            list[k] = lefthalf[i]
            i = i+1
            k = k+1
        while j < len(righthalf):
            list[k] = righthalf[j]
            j = j+1
            k = k+1
        print("merging",list)
list = [54,26,93,17]
mergeSort(list)
print(list)
"""
########################## PRAC 4 ###############################################

"""
class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
class Tree:
    def __init__(self):
        self.root = None
    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)
    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)
    def deleteTree(self):
        self.Node = None
    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)
    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print (str(node.v) + ' ')
            self._printTree(node.r)
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
"""

############################## PRAC 5 #####################################

"""
class Node:

    
	def __init__(self, key):
		self.key = key 
		self.left = None
		self.right = None



def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key,inorder(root.right))


def insert( node, key):

	if node is None:
		return Node(key)

	
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	
	return node


def minValueNode( node):
	current = node

	
	while(current.left is not None):
		current = current.left 

	return current 


def deleteNode(root, key):

	
	if root is None:
		return root 

	
	if key < root.key:
		root.left = deleteNode(root.left, key)

	
	elif(key > root.key):
		root.right = deleteNode(root.right, key)

	
	else:
		
		
		if root.left is None :
			temp = root.right 
			root = None
			return temp 
			
		elif root.right is None :
			temp = root.left 
			root = None
			return temp

		
		temp = minValueNode(root.right)

		
		root.key = temp.key

		
		root.right = deleteNode(root.right , temp.key)


	return root 




root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print ("Inorder traversal of the given tree")
inorder(root)

print ("\nDelete 20")
root = deleteNode(root, 20)
print ("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 30")
root = deleteNode(root, 30)
print ("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 50")
root = deleteNode(root, 50)
print ("Inorder traversal of the modified tree")
inorder(root)

"""

##################### PRAC 6 ##################################################

"""
from collections import defaultdict


class Graph:

	def __init__(self,vertices):
		
		self.V= vertices 
		
		
		self.graph = defaultdict(list) 

	
	def addEdge(self,u,v):
		self.graph[u].append(v)

	
	def printAllPathsUtil(self, u, d, visited, path):

		
		visited[u]= True
		path.append(u)

		
		if u ==d:
			print (path)
		else:
			
			for i in self.graph[u]:
				if visited[i]==False:
					self.printAllPathsUtil(i, d, visited, path)
					
	
		path.pop()
		visited[u]= False


	
	def printAllPaths(self,s, d):

		
		visited =[False]*(self.V)

		
		path = []

		
		self.printAllPathsUtil(s, d,visited, path)




g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

s = 2 ; d = 3
print ("Following are all different paths from %d to %d :" %(s, d))
g.printAllPaths(s, d)
"""

################# PRAC 7 ##########################################
"""
a=[84,25,32,12,44]
print('Array A is',a)
for i in range(len(a)):
    min_ind=i
    for j in range(i+1,len(a)):
        if a[min_ind]>a[j]:
            min_ind=j
    a[i],a[min_ind]=a[min_ind],a[i]
    print('Iteration %d:'%(i+1))
    print(a)
print('smallest element is :%d'%a[0])
print('largest element is :%d'%a[len(a)-1])

""""

############################### PRAC 8 ####################################
"""
def Largest(L):
    global pairs
    if len(L) ==1:
        return L[0]
    else:
        left = Largest(L[:len(L)//2])
        right = Largest(L[len(L)//2:])
        pairs.append((left,right))
        return max(left,right)
def second_Largest(L):
    global pairs
    biggest = Largest(L)
    second_L = [min(item) for item in pairs if biggest in item]
    return biggest,Largest(second_L)

if __name__ == "__main__": 
    pairs = []
    L = [2,-2,10,5,4,3,1,2,90,-98,53,45,23,56,432]


    if len(L) == 0:
        first,second = None,None
    elif len(L) ==1:
        first,second =L[0],None
    else: t number is:' +str(second))
        first,second=second_Largest(L)
    print('the largest number is:' +str(first))
    print('the 2nd larges
"""





























































        


