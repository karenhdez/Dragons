package client;

import java.io.BufferedReader;
import java.io.Console;
import java.io.IOException;
import java.io.PrintWriter;

public class GetUserInput {
	public void LoginInfo(BufferedReader in, PrintWriter out) throws IOException {
		Console console = System.console();
		System.out.println("Enter your login information:");
		String serverStatus = "";
		do {
			if(serverStatus.equals("FAILED")) {
				System.out.println("Invalid Login");
			}
			String username = console.readLine("Username: ");
			out.println(username);
			String password = String.valueOf(console.readPassword("Password: "));
			out.println(password);
			serverStatus = in.readLine();
		} while (serverStatus.equals("FAILED"));
	}
	
	public void PersonalInfo(BufferedReader stdIn, PrintWriter out) throws IOException {
		getUserFirstName(stdIn, out);
		getUserLastName(stdIn, out);
		getUserSSN(stdIn, out);
		getUserProvider(stdIn, out);
	}
	
	private void getUserFirstName(BufferedReader stdIn, PrintWriter out) throws IOException {
		String firstName;
		String status = "";
		do {
			System.out.println("Enter your first name:");
			firstName = stdIn.readLine();
			if (firstName.equals("")) {
				System.out.println("-----------------------");
				System.out.println("You must enter a name.");
				System.out.println("-----------------------");
				status = "FAILED";
			}
			else if(firstName.contains(" ")) {
				System.out.println("---------------------------------------");
				System.out.println("Your first name cannot contain a space.");
				System.out.println("---------------------------------------");
				status = "FAILED";
			}
			else if(firstName.matches(".*\\d.*")) {
				System.out.println("-------------------------------------------");
				System.out.println("Your first name cannot contain any numbers.");
				System.out.println("-------------------------------------------");
				status = "FAILED";
			}
			else {
				status = "PASSED";
			}
		} while (status.equals("FAILED"));	
		out.println(firstName);
	}
	
	private void getUserLastName(BufferedReader stdIn, PrintWriter out) throws IOException {
		String lastName;
		String status = "";
		do {
			System.out.println("Enter your last name:");
			lastName = stdIn.readLine();
			if (lastName.equals("")) {
				System.out.println("-----------------------");
				System.out.println("You must enter a name.");
				System.out.println("-----------------------");
				status = "FAILED";
			}
			else if(lastName.contains(" ")) {
				System.out.println("---------------------------------------");
				System.out.println("Your last name cannot contain a space.");
				System.out.println("---------------------------------------");
				status = "FAILED";
			}
			else if(lastName.matches(".*\\d.*")) {
				System.out.println("-------------------------------------------");
				System.out.println("Your last name cannot contain any numbers.");
				System.out.println("-------------------------------------------");
				status = "FAILED";
			}
			else {
				status = "PASSED";
			}
		} while (status.equals("FAILED"));
		out.println(lastName);
	}
	
	private static void getUserSSN(BufferedReader stdIn, PrintWriter out) throws IOException {
		String ssn;
		String status = "";
		do {
			System.out.println("Enter your social security number:");
			ssn = stdIn.readLine();
			if (ssn.equals("")) {
				System.out.println("--------------------------------------------");
				System.out.println("Your social security number cannot be blank.");
				System.out.println("--------------------------------------------");
				status = "FAILED";
			}
			else if(ssn.length() < 9 || ssn.length() == 10 || ssn.length() > 11) {
				System.out.println("--------------------------------------------------------");
				System.out.println("Your social security number must contain only 9 numbers.");
				System.out.println("--------------------------------------------------------");
				status = "FAILED";
			}
			else if(ssn.matches("\\d{3}-\\d{2}-\\d{4}")) {
				ssn = ssn.replace("-", "");
				status = "PASSED";
			}
			else if(ssn.matches("\\d{9}")) {
				status = "PASSED";
			}
			else {
				System.out.println("-----------------------------------------");
				System.out.println("Invalid input for social security number.");
				System.out.println("-----------------------------------------");
				status = "FAILED";
			}
		} while (status.equals("FAILED"));
		out.println(ssn);
	}
	
	private void getUserProvider(BufferedReader stdIn, PrintWriter out) throws IOException {
		String provider;
		do {
			System.out.println("Enter your medical provider:");
			provider = stdIn.readLine();
		} while (provider.length() == 0);
		out.println(provider);
		System.out.println();
	}
	
	public void requestRecordByPatientName(BufferedReader stdIn, PrintWriter out) throws IOException {
		String name;
		do {
			System.out.println("Enter your name:");
			name = stdIn.readLine();
		} while(name.length() == 0);
		out.println(name);
	}
	
	public void requestRecordByProvider(BufferedReader stdIn, PrintWriter out) throws IOException {
		String provider;
		do {
			System.out.println("Enter provider's name:");
			provider = stdIn.readLine();
		} while(provider.length() == 0);
		out.println(provider);
	}
}
