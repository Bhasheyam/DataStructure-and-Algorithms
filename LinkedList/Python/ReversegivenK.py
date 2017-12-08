class linkedsingly:
    def __init__(self):
        self.head = None
        
   
    # add element in the last
    def append(self,datas):
       
        if  self.head == None:
            self.head = Node(datas);
        else:
            temp=self.head
            while temp.getnext() != None:
                temp = temp.getnext()
            temp.setNext(Node(datas))

    
    
    # add element first
    
    def insert(self, datas):
        temp = Node(datas)
        temp.setNext( self.head )
        self.head =  temp
    
    def deleteDuplicates(self, A):
        seen = []
        temp = A
        prev = None
        while temp:
            if temp.data in seen:
                    prev.next = temp.next
            else:
                seen.append(temp.data)
                prev = temp

            temp = temp.next
        return A
    
    # remove element from first
    def removefirst(self):
        if self.head == None:
            print("List is Empty")
            return 0
        else:
            self.head = self.head.getnext()
    
    
   
    #Remove elementfrom Last
    
    def pop(self):
        if self.head == None:
            print("List is Empty")
            return 0
        if self.head.getnext() == None:
            self.head = None
        else:
            temp = self.head
            while True:
                if temp.getnext().getnext() == None:
                    temp.setNext(None)
                    break
                temp = temp.getnext()
    
    # add element after k
    def addk(self,k,data1):
        
        temp = self.head
        while temp:
            if temp.getdata() == k:
                new = Node(data1)
                new.setNext(temp.getnext())
                temp.setNext(new)
            temp = temp.getnext()
        
    # remove k element in the List
    def removek(self,k):
        if self.head.getdata() == k:
            self.head= self.head.getnext()
        else:
            temp=self.head
            while temp:
                if temp.getnext() == k:
                    temp.setNext( temp.getnext().getnext())
                temp = temp.getnext()           
    # print the list.
    def printlist(self):
        loop =self.head
        while loop:
            print(loop.getdata())
            loop =  loop.getnext()
    def reversek(self,A , k):
        prev = None
        temp = None
        current = A
        i = 0
        while current and i < k:
            temp = current.next
            current.next = prev
            prev = current 
            current = temp
            i += 1
            
        if temp != None:
            A.next = self.reversek(temp,k)
        
        return prev
        
           
        
            
        
        
class Node:
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

listfirst = linkedsingly()
listfirst.append(10)
listfirst.append(20)
listfirst.append(30)
listfirst.append(40)
listfirst.append(50)
listfirst.append(60)
listfirst.append(70)
listfirst.append(80)
listfirst.append(90)

da = listfirst.reversek(listfirst.head,2)
while da:
    print da.data
    da = da.next
  
    