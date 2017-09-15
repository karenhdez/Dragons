package blockchain;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	private static boolean quit = false;
	
	public static void main(String[] args) {
		
		while(!quit) {
			
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			String s = "";
			int i;
			
			/*System.out.println("Enter Integer:");
	        try {
				i = Integer.parseInt(br.readLine());
	        }
	        catch(NumberFormatException nfe){
	            System.err.println("Invalid Format!");
	        }
	        catch (IOException e) {
				e.printStackTrace();
			}*/
			
			System.out.println("Enter String or enter q to quit:");
	        try {
				s = br.readLine();
			} 
	        catch (IOException e1) {
				e1.printStackTrace();
			}
	        
	        quit = s.equals("q");
			
		}
		
	}

}
