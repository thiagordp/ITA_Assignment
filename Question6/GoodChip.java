package algorithm;

public class GoodChip extends Chip {

	public GoodChip() {
		// TODO Auto-generated constructor stub
		this.setStatus(true);
	}

	@Override
	public boolean testOther(Chip self, Chip other) {
					
			if(self.equals(other))
				return self.getStatus();
			else
				return other.getStatus();
	}
}
