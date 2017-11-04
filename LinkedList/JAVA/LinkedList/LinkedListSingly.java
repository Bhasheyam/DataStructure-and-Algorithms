package LinkedList;

public class LinkedListSingly {
	
	private Node head;  // head of the List 

	
	// gettters and setters for the list
	public void sethead(Node n){
		 head=n;
	 }
	
	public Node head(){
		 return head;
	 }
	
	// Node generators
	 static class Node{
		 
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
		 public int getdata(){
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
	
	// sample to test how it works
	LinkedListSingly l= new LinkedListSingly();
	l.sethead(new Node(10));
	Node sec= new Node(20);
	Node third= new Node(30);
	Node linked= l.head();
	linked.setNext(sec);
	sec.setNext(third);
	Node loopdata=linked;
	
	// run the loop to see the lis created properly
	while(true){
		System.out.println(loopdata.getdata());
		if(loopdata.getNext() == null)
			break;
		loopdata=loopdata.getNext();
		
	}
	
	
}
}
