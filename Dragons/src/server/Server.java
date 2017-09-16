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
		System.out.println("Waiting for a connection.");
		try (
				ServerSocket serverSocket = new ServerSocket(6019);
				Socket clientSocket = serverSocket.accept();
				PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);                   
				BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));//Reads from socket
				) {
			Blockchain block = new Blockchain();
			HandleClientOperations handle = new HandleClientOperations();

			System.out.println("Connection made");
			while(true) {
				String clientStartOption = in.readLine();
				System.out.println("Start Option: " + clientStartOption);
				if(clientStartOption.equals("L") || clientStartOption.equals("l")) {
					handle.Login(in, out);
					while (true) {
						String clientMainMenuOption = in.readLine();
						System.out.println("Main Menu Option: " + clientMainMenuOption);
						if(clientMainMenuOption.equals("N") || clientMainMenuOption.equals("n")) {
							Record clientRecord = handle.NewRecord(in, out);
							block.addRecord(clientRecord);
						}
						else if(clientMainMenuOption.equals("G") || clientMainMenuOption.equals("g")) {
							String clientGetRecordInfoMenuOption = in.readLine();
							System.out.println("Get Info Option: " + clientGetRecordInfoMenuOption);
							if(clientGetRecordInfoMenuOption.equals("1")) {
								handle.GetRecordInformationByPatientName(in, out, block);
							}
							else if(clientGetRecordInfoMenuOption.equals("2")) {
								handle.GetRecordInformationByProvider(in, out, block);
							}
							else if(clientGetRecordInfoMenuOption.equals("B") || clientGetRecordInfoMenuOption.equals("b")) {
								continue;
							}

						}
						else if(clientMainMenuOption.equals("L") || clientMainMenuOption.equals("l")) {
							break;
						}
					}
				}
				else if (clientStartOption.equals("Q") || clientStartOption.equals("q")) {
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
}
