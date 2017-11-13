class queue:
    def __init__(self):
        self.queuedata =[]
  
      
    def add(self,data):
        self.queuedata.insert(0,data)
   
     
    def pop(self):
        if len(self.queuedata) == 0:
            print "Queue is Empty"
        else:
            return self.queuedata.pop()
  
      
    def printqueue(self):
        
        i =0 
        while i < len(self.queuedata):
            print(self.queuedata[i])
            i += 1

queue = queue()
queue.add(10)
queue.printqueue()
queue.add(20)
queue.add(30)
print " "
queue.printqueue()
queue.pop()        
print " "
queue.printqueue()       
queue.pop()        
print " "
queue.printqueue()      
queue.pop()        
print " "
queue.printqueue()      
queue.pop()        
     