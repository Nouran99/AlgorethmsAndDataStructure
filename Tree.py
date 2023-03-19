class node:
    def __init__(self,data,left,right):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        return f"{self.data}"

class tree:
    def __init__(self, root):
        self.grroot = root

    def preorder (self, myroot):
        if myroot != None :
            print (myroot)
            self.preorder(myroot.left)
            self.preorder(myroot.right)

    def postorder (self, myroot):
        if myroot != None :
            self.postorder(myroot.left)
            self.postorder(myroot.right)
            print(myroot)

    def inorder (self, myroot):
        if myroot!= None:
            self.inorder (myroot.left)
            print(myroot)
            self.inorder (myroot.right)



node11 = node(11,None,None)
node12 = node(12,None,None)
node8 = node(8,None,None)
node7 = node(7,None,None)
node9 = node(9,node11,None)
node5 = node(5,node8,None)
node4 = node(4,node7,None)
node10 = node(10,node12,None)
node6 = node(6,node9,node10)
node2 = node(2,node4,node5)
node3 = node(3,None,node6)
node1 = node(1,node2,node3)

my_tree = tree(node1)
print ("inorder")
my_tree.inorder(my_tree.grroot)
print ("postorder")
my_tree.postorder(my_tree.grroot)
print ("preorder")
my_tree.preorder(my_tree.grroot)