package client;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class Client {

	public static void main(String[] args) throws UnknownHostException, IOException {		
		try (Socket sock = new Socket("localhost", 6019);
			 PrintWriter out = new PrintWriter(sock.getOutputStream(), true);
			 BufferedReader in = new BufferedReader(new InputStreamReader(sock.getInputStream()));
			 BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in))//Reads user input
			 ) {
			displayMenu();
			String option = getUserOption(stdIn);
			out.println(option);
			if(option.equals("N") || option.equals("n")) {
				getUserInfo(stdIn, out);
				stdIn.close();
				in.close();
				out.close();
				sock.close();
			}
			else if(option.equals("Q") || option.equals("q")) {
				stdIn.close();
				in.close();
				out.close();
				sock.close();
			}
		}		
	}
	
	private static void displayMenu() {
		System.out.println("===================================");
		System.out.println("Please Enter an Option:");
		System.out.println("(N) - New User");
		System.out.println("(G) - Getting Info");
		System.out.println("(Q) - Quit");
		System.out.println("===================================");
	}
	
	private static String getUserOption(BufferedReader stdIn) throws IOException {
		String option;
		do {
			System.out.println("Option:");
			option = stdIn.readLine();
		} while ( !option.equals("N") && !option.equals("n") && !option.equals("Q") && !option.equals("q") );
		return option;
	}
	
	private static void getUserInfo(BufferedReader stdIn, PrintWriter out) throws IOException {
		getUserFirstName(stdIn, out);
		getUserLastName(stdIn, out);
		getUserSSN(stdIn, out);
		getUserProvider(stdIn, out);
	}
	
	private static void getUserFirstName(BufferedReader stdIn, PrintWriter out) throws IOException {
		String firstName;
		do {
			System.out.println("Enter your first name:");
			firstName = stdIn.readLine();
		} while (firstName.length() == 0);	
		out.println(firstName);
	}
	
	private static void getUserLastName(BufferedReader stdIn, PrintWriter out) throws IOException {
		String lastName;
		do {
			System.out.println("Enter your last name:");
			lastName = stdIn.readLine();
		} while (lastName.length() == 0);
		out.println(lastName);
	}
	
	private static void getUserSSN(BufferedReader stdIn, PrintWriter out) throws IOException {
		String ssn;
		do {
			System.out.println("Enter your social security number:");
			ssn = stdIn.readLine();
		} while (ssn.length() == 0);
		out.println(ssn);
	}
	
	private static void getUserProvider(BufferedReader stdIn, PrintWriter out) throws IOException {
		String provider;
		do {
			System.out.println("Enter your medical provider:");
			provider = stdIn.readLine();
		} while (provider.length() == 0);
		out.println(provider);
	}
}
