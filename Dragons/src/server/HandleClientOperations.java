package server;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.PrintWriter;

import blockchain.Blockchain;
import blockchain.Record;

public class HandleClientOperations {
	private DisplayInformation display;
	
	public HandleClientOperations() {
		display = new DisplayInformation();
	}
	public void Login(BufferedReader in, PrintWriter out) throws IOException {
		String status;
		do {
			String username = in.readLine();
			String password = in.readLine();
			if (username.equals("Dragon") && password.equals("Dragon")) {
				System.out.println("Valid User: " + username);
				status = "PASSED";
				out.println(status);
			} 
			else {
				status = "FAILED";
				out.println(status);
			}
		} while(status.equals("FAILED"));
	}
	
	public Record NewRecord(BufferedReader in, PrintWriter out) throws IOException {
		String firstName = in.readLine();
		String lastName = in.readLine();
		int ssn = Integer.parseInt(in.readLine());
		String provider = in.readLine();
		display.GeneratingRecordInformation(firstName, lastName, ssn, provider);
		return new Record(firstName, lastName, ssn, provider);
	}
	
	public void GetRecordInformationByPatientName(BufferedReader in, PrintWriter out, Blockchain block) throws IOException {
		String name = in.readLine();
		display.RecordInfoByPatientName(name, block);
		out.println(block.getListByPatient(name));
	}
	
	public void GetRecordInformationByProvider(BufferedReader in, PrintWriter out, Blockchain block) throws IOException {
		String provider = in.readLine();
		display.RecordInfoByProvider(provider, block);
		out.println(block.getListByProvider(provider));
	}
}
