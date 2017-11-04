class linkedsingly:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    # accessing the node    
    def getdata( self ):
        return self.data
        
    def getnext( self ):
        return self.next
        
    def setdata( self, data1 ):
        self.data = data1
        
    def setNext( self, next1 ):
        self.next = next1

loop = linkedsingly(10)
sec = linkedsingly(20)
third = linkedsingly(30)

loop.next=sec
sec.next=third
temp = loop
while True:
    print(temp.getdata())
    if temp.next == None:
        break
    temp = temp.next

  
    
    