package server;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import blockchain.Record;
import blockchain.Blockchain;

public class Server {

	public static void main(String[] args) throws IOException {
		Blockchain block = new Blockchain();
		try (
	            ServerSocket serverSocket = new ServerSocket(6019);
	            Socket clientSocket = serverSocket.accept();
	            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);                   
	            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));//Reads from socket
	        ) {
				System.out.println("Connection made");
				while(true) {
					String clientOption = in.readLine();
					if(clientOption.equals("N") || clientOption.equals("n")) {
						String firstName = in.readLine();
						String lastName = in.readLine();
						int ssn = Integer.parseInt(in.readLine());
						String provider = in.readLine();
						Record clientRecord = generateClientRecord(firstName, lastName, ssn, provider);
						
						System.out.println("===================================");
						System.out.println("Creating Record:");
						System.out.println("  First Name: " + firstName);
						System.out.println("  Last Name: " + lastName);
						System.out.println("  SSN: " + ssn);
						System.out.println("  Provider: " + provider);
						System.out.println("===================================");
						
						block.addRecord(clientRecord);
					}
					else if(clientOption.equals("G") || clientOption.equals("g")) {
						String name = in.readLine();
						System.out.println("===================================");
						System.out.println("Requested Info: " + name);
						System.out.println("Info: " + block.getListByPatient(name));
						System.out.println("===================================");
						System.out.println();
						out.println(block.getListByPatient(name));
					}
					else if(clientOption.equals("Q") || clientOption.equals("q")) {
						in.close();
						out.close();
						clientSocket.close();
						serverSocket.close();
					}
				}
	        } catch (IOException e) {
	            System.out.println(e.getMessage());
	        }
	}
	
	private static Record generateClientRecord(String firstName, String lastName, int ssn, String provider) {
		return new Record(firstName, lastName, ssn, provider);
	}

}
