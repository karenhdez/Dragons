package blockchain;

public class Record {
		
	private String firstName;
	private String lastName;
	private int SSN;
	private String signedSHA256;
	private int blockID;
	private int verificationProcessID;
	private String SHA256String;
	
	public Record next;
	
	public String generateString(int size) {
		
		return "";
		
	}
	
	public int generateID(int size) {
		
		return 0;
		
	}
	
	public Record() {
	}
	
	//Setters
	public void setFirstName(String fName) {
		this.firstName = fName;
	}
	
	public void setLastName(String lName) {
		this.lastName = lName;
	}
	
	public void setSSN(int ssn) {
		this.SSN = ssn;
	}
		
	public void setSignedSHA256(String signedSHA) {
		this.signedSHA256 = signedSHA;
	}
	
	public void setBlockId(int bID) {
		this.blockID = bID;
	}
	
	public void setVerificationProcessID(int vpID) {
		this.verificationProcessID = vpID;
	}
	
	public void setSHA256String(String shaString) {
		this.SHA256String = shaString;
	}
	
	//Getters 
	public String getFirstName() {
		return this.firstName;
	}
	
	public String getLastName() {
		return this.lastName;
	}
	
	public int getSSN() {
		return this.SSN;
	}
	
	public String getSignedSHA256() {
		return this.signedSHA256;
	}
	
	public int getBlockId() {
		return this.blockID;
	}
	
	public int getVerificationProcessID() {
		return this.verificationProcessID;
	}
	
	public String getSHA256String() {
		return this.SHA256String;
	}
}
