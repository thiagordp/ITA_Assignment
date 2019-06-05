package algorithm;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			
		Queue<Integer> Qgood = new LinkedList<Integer>();
		

		Random random = new Random();
		
		int n = 10;
		int  i =0, j = 0, k=0;
		
		int half =(int) Math.ceil(n/2)+1;
		
		Chip[] chip = new Chip[n]; 
		
		while((j+k) < n) {
			
			if(k < half & random.nextInt((int) Math.pow(n,3)+1) % 2 == 0) {
				GoodChip good = new GoodChip();
				chip[i] = good;
				k++;
				i++;
			}
			else {
				if(j < n - half) {
					BadChip bad = new BadChip();
					chip[i] = bad;
					j++;
					i++;
				}
			}
			
		}
		
		for (int m = 0; m < chip.length; m++) {
			System.out.println("C"+m+": "+chip[m].status);
		}
		
		int count = 0;
		
		for(i = 0; i < chip.length; i++) {
			count = 0;
			
			for(j = 0; j < chip.length; j++) {
			
				if(i != j && chip[j].testOther(chip[j], chip[i])) {
					count++;
				}
			}
			
			if(count >= half-1) {
				System.out.println("Good: "+i);
				Qgood.add(i);
			}
		}

	}

}
