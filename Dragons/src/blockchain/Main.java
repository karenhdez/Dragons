package blockchain;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	private static boolean quit = false;
	private static InputInterface currentInput = Main::inputOptions;
	private static Blockchain medRecords = new Blockchain();

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
	        catch (IOException e) {
				e.printStackTrace();
			}
		}
		
	}
	
	private static void inputAddRecord(BufferedReader br) {
    	
    	System.out.println("Enter record info.");
    	System.out.println("Format: first,last,ssn,provider");
    	System.out.println("Enter q to quit.");
    	
    	while(true) {
			try {
				String s = getString(br);
    	
				if (s.equals("q")) {
		    		currentInput = Main::inputOptions;
					break;
				}
				else {
					
					StringTokenizer tokenizer = new StringTokenizer(s, ",");
					String f = tokenizer.nextToken();
					String l = tokenizer.nextToken();
					int ssn = Integer.parseInt(tokenizer.nextToken());
					String p = tokenizer.nextToken();
					
					medRecords.addRecord(new Record(f, l, ssn, p));
					System.out.println("Record Added.");
					
				}
			}
			catch (java.util.NoSuchElementException e1) {
				System.err.println("Invalid Format!");
			}
			catch (java.lang.NullPointerException e2) {
				System.err.println("Invalid Format!");
			}
			catch (java.lang.NumberFormatException e3) {
				System.err.println("Invalid SSN!");
			}
		}
        
    }
	
	private static void inputRecordName(BufferedReader br) {
    	
    	System.out.println("Enter patient's full name.");
    	System.out.println("Format: first,last");
    	System.out.println("Enter q to quit.");
    	
    	while(true) {
	    	try {
				String s = getString(br);
		
				if (s.equals("q")) {
		    		currentInput = Main::inputOptions;
					break;
				}
				else {
					
					StringTokenizer tokenizer = new StringTokenizer(s, ",");
					String f = tokenizer.nextToken();
					String l = tokenizer.nextToken();
					
					System.out.println("Record retrieved.");
					System.out.println(medRecords.getListByPatient(f, l));
					
				}
			}
			catch (java.util.NoSuchElementException e1) {
				System.err.println("Invalid Format!");
			}
			catch (java.lang.NullPointerException e2) {
				System.err.println("Invalid Format!");
			}
    	}
        
    }
	
	private static void inputRecordProvider(BufferedReader br) {
    	
		System.out.println("Enter provider's name.");
    	System.out.println("Enter q to quit.");
    	
    	while(true) {
	    	try {
				String s = getString(br);
		
				if (s.equals("q")) {
		    		currentInput = Main::inputOptions;
					break;
				}
				else {
					
					System.out.println("Record retrieved.");
					System.out.println(medRecords.getListByProvider(s));
					
				}
			}
			catch (java.util.NoSuchElementException e1) {
				System.err.println("Invalid Format!");
			}
			catch (java.lang.NullPointerException e2) {
				System.err.println("Invalid Format!");
			}
    	}
        
    }
	
    private static void inputOptions(BufferedReader br) {
    	
    	System.out.println("Select an option.");
    	System.out.println("0. Quit");
    	System.out.println("1. Add record");
    	System.out.println("2. Get record by name");
    	System.out.println("3. Get record by provider");
    	
    	int i = getInteger(br);
    	
    	switch (i) {
	        case 0:
	        	quit = true;
	        	break;
	        case 1:
	        	currentInput = Main::inputAddRecord;
	            break;
	        case 2:
	        	currentInput = Main::inputRecordName;
	            break; 
	        case 3:
	        	currentInput = Main::inputRecordProvider;
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
