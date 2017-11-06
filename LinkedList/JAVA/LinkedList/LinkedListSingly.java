package LinkedList;

public class LinkedListSingly {
	
	private Node head;  // head of the List 
    
	public LinkedListSingly(){
		this.head =null;
	}
	
	public void append(int data){
		if(this.head == null){
			this.head =  new Node(data);
		}
		else{
			Node temp = this.head;
			while( temp.getNext() != null ){
				temp = temp.getNext();
			}
			temp.setNext(new Node(data));
		}
	}
	
	
	public void insert(int data){
		Node temp = new Node(data);
		temp.setNext(this.head);
		this.head = temp;
	}
	
	public void pop(){
		if(this.head == null){
			System.out.println("the list is null");
		}
		else{
			
		    if (this.head.getNext() == null)
		           this.head = null;
		   else{
			  Node temp =this.head;
		      while(true){
			     if (temp.getNext().getNext() == null){
			                                   temp.setNext(null);
			                                   break;
			     									 }
			     temp = temp.getNext();
		                 }
		       }
		   }
	}
	
	public void removefirst(){
		if(this.head == null){
			System.out.println("the list is null");
		}
		else{
			
			   this.head = this.head.getNext();
		   
		   }

		}
		
	public void printlist(){
		Node loop = this.head;
		while(loop != null){
			System.out.println(loop.getData());
			loop = loop.getNext();
		}
	}
	
	class Node{
	
		 
		// Data and Next reference  
		private int data;
		private Node next;
		
		// Constructor to intialise the node
		Node(int d){
			 data=d;
			 next=null;
		 }
		
		public void setData(int data) {
			this.data = data;
		}
		 public int getData(){
			 return data;
		 }
		 public Node getNext(){
			return next;
			 
		 }
		 public void setNext(Node next) {
				this.next = next;
			}


	 }
	 
public static void main(String s[]){
	
	LinkedListSingly listfirst = new LinkedListSingly();
	listfirst.append(10);
	listfirst.append(20);
	listfirst.append(30);
	listfirst.printlist();
	listfirst.insert(5);
	listfirst.printlist();
	listfirst.pop();
	listfirst.printlist();
	listfirst.removefirst();
	listfirst.printlist();
	listfirst.removefirst();
	listfirst.printlist(); 
	listfirst.pop();
	System.out.println("finished");
	listfirst.printlist() ;
		
	}
	
	
}

