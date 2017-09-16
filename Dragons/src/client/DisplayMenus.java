package client;

public class DisplayMenus {	
	public void StartMenu() {
		//Displays the start menu to the client.
		System.out.println("===================================");
		System.out.println("Please Enter an Option:");
		System.out.println("(L) - Login");
		System.out.println("(Q) - Quit");
		System.out.println("===================================");
	}
	
	public void MainMenu() {
		//Displays the main menu to the client.
		System.out.println("===================================");
		System.out.println("Please Enter an Option:");
		System.out.println("(N) - New User");
		System.out.println("(G) - Get Info");
		System.out.println("(L) - Logout");
		System.out.println("===================================");
	}
	
	public void GetInfoMenu() {
		//Displays the get info menu to the client.
		System.out.println("===================================");
		System.out.println("How would you like to receive your data?");
		System.out.println("(1) - By Patient Name");
		System.out.println("(2) - By Provider");
		System.out.println("(B) - Back");
	}
}
