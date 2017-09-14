package blockchain;

public class Record {
		
	public String firstName;
	public String lastName;
	public int SSN;
	public String signedSHA256;
	public int blockID;
	public int verificationProcessID;
	public String SHA256String;
	
	public Record next;
	
	public String generateString(int size) {
		
		return "";
		
	}
	
	public int generateID(int size) {
		
		return 0;
		
	}
	
	public Record() {
	}
		
}
