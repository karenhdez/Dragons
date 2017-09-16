package client;

import java.io.BufferedReader;
import java.io.IOException;

public class GetMenuOptions {
	public String StartMenuOption(BufferedReader stdIn) throws IOException {
		String option;
		do {
			System.out.println("Option: ");
			option = stdIn.readLine();
		} while(!option.equals("L") && !option.equals("l") &&
				!option.equals("Q") && !option.equals("q"));
		return option;
	}
	
	public String MainMenuOption(BufferedReader stdIn) throws IOException {
		String option;
		do {
			System.out.println("Option:");
			option = stdIn.readLine();
		} while (!option.equals("N") && !option.equals("n") && 
				 !option.equals("G") && !option.equals("g") &&
				 !option.equals("L") && !option.equals("l"));
		return option;
	}
	
	public String GetInfoMenuOption(BufferedReader stdIn) throws IOException {
		String option;
		do {
			System.out.println("Option:");
			option = stdIn.readLine();
		} while (!option.equals("1") && !option.equals("2") &&
				 !option.equals("B") && !option.equals("b"));
		return option;
	}
}
