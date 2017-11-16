class binarytree:
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
        
    def insert(self,root,item):
        if root.root < item:
            if root.right == None:
                root.right = binarytree(item)
            else:
                self.insert(root.right,item)
           
        else:
             if root.left == None:
                root.left = binarytree(item)
             else:
                self.insert(root.left,item)
             
          
        
    
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
t = binarytree(10)
t.insert(t,5)
t.insert(t,20)
t.insert(t,30)
t.preorderprint(t)
