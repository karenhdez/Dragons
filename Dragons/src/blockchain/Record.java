package blockchain;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.sql.Timestamp;

public class Record {
	public String firstName;
	public String lastName;
	public int SSN;
	public String provider;
	public int blockID;
	public String SHA256String;
	public String signedSHA256;
	public int verificationProcessID;
	//public String timeStamp;
	public Timestamp timestamp;
	
	public Record next;
	
	public Record(String f, String l, int ssn, String p) {
		this.firstName = f;
		this.lastName = l;
		this.SSN = ssn;
		this.provider = p;
		this.blockID = this.generateBlockID();
		this.SHA256String = this.generateSHA256();
		this.signedSHA256 = this.generateSignedSHA256();
		this.verificationProcessID = this.generateProcessId();
		//String time = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss").format(new Date());
		this.timestamp = new Timestamp(System.currentTimeMillis());
	}
	
	//Temporary: for now generates random string
	public String generateSHA256() {
		String sHA256 = "WELKFRLEA";
		return sHA256;
		
	}
	
	//Temporary: for now generates random id
	//TODO: This can be fixed now
	public int generateBlockID() {
		return 1;
		
	}
	
	//Temporary: for now generates a random string representation of the signed SHA256
	public String generateSignedSHA256(){
		String signedSHA256 = "LKEFALEKFALEK";
		return signedSHA256;
	}
	
	//TODO: check how process Id is selected and used
	public int generateProcessId() {
		return 2;
	}
	
	//TODO: Add more attributes to return
	public String toString(){
		return "Name: " + this.firstName + " " + this.lastName + " Provider: " + this.provider + " Time: " + this.timestamp;
	}
	
	public Record getNext() {
		return next;
	}
	
	public String getFirstName() {
		return firstName;
	}
	
	public String getLastName() {
		return lastName;
	}
	
	public String getProvider() {
		return provider;
	}
	
	public Timestamp getTimestamp() {
		return timestamp;
	}
	
	public void setTimestamp(Timestamp ts) {
		this.timestamp = ts;
	}
}
