class doublelink:
    # creating a list
    def __init__(self):
        self.head = None
    
    #append element at last
    def append(self,data1):
        if self.head == None:
            self.head = double(data1)
            print("came to append")
        else:
            temp = self.head
            while( temp.getnext() != None ):
                temp = temp.getnext()
            new = double(data1)
            temp.setnext(new)
            new.setprev(temp)
            
   # insert element at first
    def insert(self, data1):
       new = double(data1)
       new.setnext(self.head)
       self.head.setprev(new)
       self.head = new
  # inset element after k
    def addk(self, k, data1):
        if self.head.getdata() == k :
            new = double(data1)
            new.setnext(self.head.getnext())
            self.head.setnext( new )
            new.setprev(self.head)
            
        else:
            loop = self.head
            while ( loop.getdata() != k ):
                loop = loop.getnext()      
            new = double( data1 )
            new.setprev( loop )
            new.setnext(loop.getnext())
            loop.setnext( new )
    # pop
    def pop(self):
        if self.head == None:
            print " list is empty"
            return 0
        
        if self.head.getnext() == None:
            self.head = None
        else:
            print("came here 1")
            temp = self.head
            while temp.getnext() != None:
                 temp = temp.getnext()
            temp = temp.getprev()
            temp.setnext(None)
       
        
    # remove first lement
    def removefirst(self):
        if self.head == None:
            print " list is empty"
            return 0
        if self.head.getnext() == None:
            self.head == None
        else:
            self.head = self.head.getnext()
            self.head.setprev(None)
    #remove the element k
    def removek(self, k):
        if self.head.getdata() == k:
            self.head == None
        else:
            temp = self.head
            
            while( temp ):
                if temp.getnext().getdata() == k:
                    temp.setnext(temp.getnext().getnext())
                    temp.getnext().setprev(temp)
                    break
                temp = temp.getnext()
    def printlist(self):
        loop = self.head
        while( loop ):
            print loop.getdata()
            loop = loop.getnext()  
                

class double:
    def __init__(self,data1):
        self.data = data1
        self.next = None
        self.prev = None
        
    def getdata(self):
       return self.data
    
    def getnext(self):
       return self.next
       
    def getprev(self):
       return self.prev
    
    def setnext(self,next1):
        self.next = next1
    
    def setprev(self,prev1):
        self.prev = prev1      
    
listfirst = doublelink()
listfirst.append(10)
listfirst.append(20)
listfirst.append(30)
listfirst.printlist()
print " "
listfirst.insert(5)
listfirst.printlist()
print " "
listfirst.pop()
listfirst.printlist()
print " "
listfirst.removefirst()

print " "
listfirst.printlist()
print " "
listfirst.removefirst()

print " "
listfirst.printlist()

print " "
listfirst.pop()
listfirst.printlist()

print("finished")
listfirst.printlist()
print " "

listfirst.append(10)
print " "
listfirst.printlist()
listfirst.insert(20)

print " "
listfirst.printlist()
listfirst.append(30)
print " "
listfirst.printlist()
listfirst.addk(20,45) 

print " "
listfirst.printlist()
print " "
listfirst.removek(20)
listfirst.printlist()   
    


    