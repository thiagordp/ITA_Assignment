package algorithm;

import java.util.Random;

public class BadChip extends Chip {
	
	Random gerador = new Random();

	public BadChip() {
		// TODO Auto-generated constructor stub
		this.setStatus(false);
	}
	
	@Override
	public boolean testOther(Chip self, Chip other) {
		return gerador.nextBoolean();
	}

}
