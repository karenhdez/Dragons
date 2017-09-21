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
	            String clientOption = in.readLine();
	            if(clientOption.equals("N") || clientOption.equals("n")) {
	            	String firstName = in.readLine();
	            	String lastName = in.readLine();
	            	int ssn = Integer.parseInt(in.readLine());
	            	String provider = in.readLine();
	            	Record clientRecord = generateClientRecord(firstName, lastName, ssn, provider);
	            	block.addRecord(clientRecord);
	            	System.out.println(block.getListByPatient(firstName));
	            }
	            else if(clientOption.equals("Q") || clientOption.equals("q")) {
	            	in.close();
	            	out.close();
	            	clientSocket.close();
	            	serverSocket.close();
	            }
	            
	        } catch (IOException e) {
	            System.out.println(e.getMessage());
	        }
	}
	
	private static Record generateClientRecord(String firstName, String lastName, int ssn, String provider) {
		return new Record(firstName, lastName, ssn, provider);
	}

}
