package client;

import java.io.BufferedReader;
import java.io.Console;
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
			DisplayMenus display = new DisplayMenus();
			GetMenuOptions optionInput = new GetMenuOptions();
			GetUserInput userInput = new GetUserInput();
			DisplayRequestedInfo requested = new DisplayRequestedInfo();
			
			while(true) {
				display.StartMenu();
				String startOption = optionInput.StartMenuOption(stdIn);
				out.println(startOption);
				if (startOption.equals("L") || startOption.equals("l")) {
					userInput.LoginInfo(in, out);
					while(true) {
						display.MainMenu();
						String mainMenuOption = optionInput.MainMenuOption(stdIn);
						out.println(mainMenuOption);
						if(mainMenuOption.equals("N") || mainMenuOption.equals("n")) {
							userInput.PersonalInfo(stdIn, out);
						}
						else if(mainMenuOption.equals("G") || mainMenuOption.equals("g")) {
							display.GetInfoMenu();
							String getInfoMenuOption = optionInput.GetInfoMenuOption(stdIn);
							out.println(getInfoMenuOption);
							if (getInfoMenuOption.equals("1")) {
								userInput.requestRecordByPatientName(stdIn, out);
								requested.RecordByPatientName(in);
							}
							else if (getInfoMenuOption.equals("2")) {
								userInput.requestRecordByProvider(stdIn, out);
								requested.RecordByProvider(in);
							}
							else if (getInfoMenuOption.equals("B") || getInfoMenuOption.equals("b")) {
								continue;
							}
						}
						else if(mainMenuOption.equals("L") || mainMenuOption.equals("l")) {
							break;
						}
					}
				}
				else if (startOption.equals("Q") || startOption.equals("q")) {
					stdIn.close();
					in.close();
					out.close();
					sock.close();
					break;
				}
			}
		}		
	}
}
