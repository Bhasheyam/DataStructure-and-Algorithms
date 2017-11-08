package Sorting;

public class Selectionsort {

	
	public int[] selection(int[] arr){
		
		int i =0;
		while ( i < arr.length){
			int j = i + 1;
			while ( j < arr.length){
				if( arr[i] > arr[j]){
					int temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
				j ++;
			}
		    i ++;
		}
		return arr;
		
	}
	
	public static void main(String s[]){
		Selectionsort  sort = new Selectionsort();
		int[] arr = {64, 25, 12, 22, 11};
		int[] ans = sort.selection(arr);
		
		System.out.println(ans[4]);
	}
}
