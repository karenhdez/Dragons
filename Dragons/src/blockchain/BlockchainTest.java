package blockchain;

import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.Collection;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

@RunWith(Parameterized.class)
public class BlockchainTest {
	
	private String input;
	private String expectedOutput;
	private String actualOutput;

    @Before
    public void initialize() {
    }
	
    public BlockchainTest(String input, String expectedOutput) {
    	this.input = input;
    	this.expectedOutput = expectedOutput;
    }
    
    @Parameterized.Parameters
    public static Collection testParams() {
    	return Arrays.asList(new Object[][] {
    		//{ "key", "keys" },										Sample input
    	});
    }
    
    @Test
    public void test() {

	    try {
	    	System.out.println("Testing input : " + input);
	    	actualOutput = "";//Blockchain(input);						Run blockchain
	    	try {
	    		assertEquals(expectedOutput, actualOutput);
	    	} catch (ClassCastException e) {
	    		assertEquals(expectedOutput, actualOutput);
	    	}
	    }
	    catch (IllegalArgumentException e) {
	    	assertEquals(true, e.toString().contains(expectedOutput));
	    }
	    
    }

}
