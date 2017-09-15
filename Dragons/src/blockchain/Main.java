package blockchain;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	private static boolean quit = false;
	private static InputInterface currentInput = Main::inputOptions;

	private static int getInteger(BufferedReader br) {
		
		while(true) {
			try {
				int i = Integer.parseInt(br.readLine());
				return i;
		    }
		    catch (NumberFormatException nfe) {
		        System.err.println("Invalid Format!");
		    }
		    catch (IOException e) {
				e.printStackTrace();
			}
		}
		
	}
	
	private static String getString(BufferedReader br) {
		
		while(true) {
			try {
				String s = br.readLine();
				return s;
			} 
	        catch (IOException e1) {
				e1.printStackTrace();
			}
		}
		
	}
	
	private static void inputRecord(BufferedReader br) {
    	
    	System.out.println("Enter record info.");
    	System.out.println("Enter q to quit.");
    	
    	String s = getString(br);
    	
    	if (s.equals("q"))
    		currentInput = Main::inputOptions;
        
    }
	
    private static void inputOptions(BufferedReader br) {
    	
    	System.out.println("Select an option.");
    	System.out.println("0. Quit");
    	System.out.println("1. Add record");
    	
    	int i = getInteger(br);
    	
    	switch (i) {
	        case 0:
	        	quit = true;
	        	break;
	        case 1:
	        	currentInput = Main::inputRecord;
	            break;
    	}
        
    }

    @FunctionalInterface
    public static interface InputInterface{
        void input(BufferedReader br);
    }
	
	public static void main(String[] args) {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
        while(!quit) {
        	
        	currentInput.input(br);
        	
        }
        
    }

}
