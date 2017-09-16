package server;

import blockchain.Blockchain;

public class DisplayInformation {
	public void GeneratingRecordInformation(String firstName, String lastName, int ssn, String provider) {
		System.out.println("===================================");
		System.out.println("Creating Record:");
		System.out.println("  First Name: " + firstName);
		System.out.println("  Last Name: " + lastName);
		System.out.println("  SSN: " + ssn);
		System.out.println("  Provider: " + provider);
		System.out.println("===================================");
	}
	
	public void RecordInfoByPatientName(String name, Blockchain block) {
		System.out.println("===================================");
		System.out.println("Requested Name Info: " + name);
		System.out.println("Info: " + block.getListByPatient(name));
		System.out.println("===================================");
		System.out.println();
	}
	
	public void RecordInfoByProvider(String provider, Blockchain block) {
		System.out.println("===================================");
		System.out.println("Requested Provider Info: " + provider);
		System.out.println("Info: " + block.getListByProvider(provider));
		System.out.println("===================================");
		System.out.println();
	}
}
