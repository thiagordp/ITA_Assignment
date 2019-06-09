package algorithm;

public class Chip {
	
	boolean status;
	
	public Chip() {};

	
	public Chip(boolean status) {
		this.setStatus(status);
	}

	public boolean getStatus() {
		return status;
	}

	public void setStatus(boolean status) {
		this.status = status;
	}
	
	public boolean testOther(Chip self, Chip other) {
		
		return this.status;
	}
	
}


