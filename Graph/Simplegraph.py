class graph:
    def __init__(self,size):
        i = 0
        self.graph = []
        while i < size:
            self.graph.append([])
            i += 1
       
        self.size = size
        
    def addedge(graph, src, des):
        
        
            graph.graph[src].insert(0,des)
            graph.graph[des].insert(0,src)
         
    def printgraph(graph):
        i = 0
        print graph.graph
        while i < graph.size:
            
            j = 0
            print " Vertex - ",i , " Adjacent Index"
            while j < len(graph.graph[i]):
                print "--> ",graph.graph[i][j]
                j += 1 
            i += 1
g = graph(5)
g.addedge(0,1)
g.addedge(0,2)
g.addedge(0,3)
g.addedge(1,2)
g.addedge(2,3)
g.addedge(1,4)
g.printgraph()   
        
    
        
        
        
        
        