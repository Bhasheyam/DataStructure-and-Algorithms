class stack:
    def __init__(self):
        self.stack = []
        
    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        if len( self.stack ) == 0:
            print "stack is empty"
            return ""
        return self.stack.pop()
    
    
    def printstack(self):
        
        temp =self.stack
        for a in temp:
            print(a)
            
    def stacksize(self):
        return len(self.stack)

test = stack()
print(test.pop())
test.push(10)
test.printstack()
print(" ")
test.push(20)
test.printstack()
print(" ")
test.push(30)
test.printstack()
print(" ")
print( test.pop())
print " "
test.printstack()
test.pop()
print " "
test.printstack()
        