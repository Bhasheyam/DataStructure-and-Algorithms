class double:
    def __init__(self,data1):
        self.data = data1
        self.next = None
        self.prev = None
    def getData(self):
       return self.data
    
    def getNext(self):
       return self.next
       
    def getprev(self):
       return self.prev
    
    def setnext(self,next1):
        self.next = next1
    
    def setprev(self,prev1):
        self.prev = prev1      
    
first = double(10)
sec =  double(20)
third = double(30)

first.next = sec
sec.next = third
third.prev = sec
sec.prev = first

loop = first
while(True):
    print( loop.getData() )
    if loop.getNext() == None:
        break
    loop = loop.next

    