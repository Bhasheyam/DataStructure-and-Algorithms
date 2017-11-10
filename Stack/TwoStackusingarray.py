class twostack:
    def __init__(self,n):
        self.maxsize = n
        self.stack = [None] * n
        self.topsize1 = -1
        self.topsize2 = n
    
    def push1(self,item):
        if( self.topsize1 < self.topsize2 -1 ):
            self.topsize1 += 1
            self.stack[self.topsize1] = item
        else : 
            print "Stack Overflow "
            return " "            
    
    def push2(self,item):
        if( self.topsize1 + 1 < self.topsize2  ):
            self.topsize2 -= 1
            self.stack[self.topsize2] = item
        else : 
            print "Stack Overflow "
            return " "   
    def pop1(self):
        if self.topsize1 >= 0:
            x = self.stack[self.topsize1]
            self.topsize1 -= 1
            return x
        else:
            print " Stack underflow"
    
    def pop2(self):
        if self.topsize2 < self.maxsize:
            x = self.stack[self.topsize2]
            self.topsize2 += 1
            return x
        else:
            print " Stack underflow"
            
ts = twostack(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)

ts.push2(7)
 
print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))