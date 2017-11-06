package LinkedList;

public class linkedlistdouble {
	private Node head;
	class Node{
		
	
	private int data;
	private Node next;
	private Node prev;
	
	
	public Node(int datainput){
		this.data = datainput;
		this.next = null;
		this.prev = null;
	}
 

	public int getData() {
		return data;
	}


	public void setData(int data) {
		this.data = data;
	}


	public Node getNext() {
		return next;
	}


	public void setNext(Node node) {
		this.next = node;
	}


	public Node getPrev() {
		return prev;
	}


	public void setPrev(Node prev) {
		this.prev = prev;
	}
	}

public static void main(String s[]){
	
	Node first = new Node(10);
	first.setNext(new Node(20));
	first.getNext().setNext(new Node(30));
	
	Node loopdata=first;
	while(true){
		System.out.println(loopdata.getData());
		if(loopdata.getNext() == null)
			break;
		loopdata=loopdata.getNext();
		
	}
}
	
	
	
}
