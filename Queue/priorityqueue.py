class prirorityqueue:
    def __init__(self):
        self.queuedata =[]
  
      
    def add(self,data,prority):
        if len(self.queuedata) == 0:
            self.queuedata.insert(0,[prority,data])
        else:
            i = len(self.queuedata) - 1
            while i >= 0:
                if self.queuedata[i][0] >= prority:
                    self.queuedata.insert( i+1,[prority,data] )
                    break
                elif i == 0 :
                    self.queuedata.insert(0,[prority,data])
                i -= 1
   
     
    def pop(self):
        if len(self.queuedata) == 0:
            print "Queue is Empty"
        else:
            return self.queuedata.pop()
  
      
    def printqueue(self):
        
        i =0 
        while i < len(self.queuedata):
            print(self.queuedata[i][1])
            i += 1
queue = prirorityqueue()
queue.add(10,1)
queue.printqueue()
queue.add(20,2)
queue.add(30,3)
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
         