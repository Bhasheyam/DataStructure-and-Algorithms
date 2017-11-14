class Tree:
    def __init__(self, rootdata):
        self.root = rootdata
        self.left = None
        self.right = None
    
    def setleft(self,left1):
        self.left = left1

    def setright(self,right1):
        self.right = right1  
        
    def getleft(self):
        return self.left 

    def getright(self):
        return self.right 
    
    def inorderprint(self,root):
        if root:
            self.inorderprint(root.left)
            
            print(root.root)
            
            self.inorderprint(root.right)
        
    def preorderprint(self,root):
        
        if root:
            print(root.root)
            
            self.preorderprint(root.left)
            
            
            
            self.preorderprint(root.right)
    
    def postorderprint(self,root):
        
        if root:
            self.postorderprint(root.left) 
            
            self.postorderprint(root.right)
            
            print(root.root)
t = Tree(10)
t.setleft(Tree(20))
t.setright(Tree(30))
t.getleft().setleft(Tree(40))
t.getleft().setright(Tree(50))
t.getright().setleft(Tree(60))
t.getright().setright(Tree(70))
t.inorderprint(t)
print " "
t.preorderprint(t) 
print " "       
t.postorderprint(t)
    
        