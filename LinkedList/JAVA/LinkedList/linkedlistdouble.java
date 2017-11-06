package LinkedList;

public class linkedlistdouble {
	private int data;
	private linkedlistdouble next;
	private linkedlistdouble prev;
	
	
	public linkedlistdouble(int datainput){
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


	public linkedlistdouble getNext() {
		return next;
	}


	public void setNext(linkedlistdouble next) {
		this.next = next;
	}


	public linkedlistdouble getPrev() {
		return prev;
	}


	public void setPrev(linkedlistdouble prev) {
		this.prev = prev;
	}

public static void main(String s[]){
	
	linkedlistdouble first = new linkedlistdouble(10);
	first.setNext(new linkedlistdouble(20));
	first.getNext().setNext(new linkedlistdouble(30));
	
	linkedlistdouble loopdata=first;
	while(true){
		System.out.println(loopdata.getData());
		if(loopdata.getNext() == null)
			break;
		loopdata=loopdata.getNext();
		
	}
}
	
	
	
}
