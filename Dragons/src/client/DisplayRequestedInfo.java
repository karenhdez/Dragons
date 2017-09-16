package client;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.Scanner;

public class DisplayRequestedInfo {
	private Scanner scan = new Scanner(System.in);
	
	public void RecordByPatientName(BufferedReader in) throws IOException {
		String info = in.readLine();
		System.out.println("===================================");
		System.out.println("Received: " + info);
		System.out.println("===================================");
		System.out.println("Press Enter to Continue.");
		scan.nextLine();
	}
	
	public void RecordByProvider(BufferedReader in) throws IOException {
		String info = in.readLine();
		System.out.println("===================================");
		System.out.println("Received: " + info);
		System.out.println("===================================");
		System.out.println("Press Enter to Continue.");
		scan.nextLine();
	}
}
