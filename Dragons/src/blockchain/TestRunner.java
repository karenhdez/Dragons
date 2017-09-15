package blockchain;

import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class TestRunner {

	public static void main(String[] args) {
		
		Result result = JUnitCore.runClasses(BlockchainTest.class);

		for (Failure failure : result.getFailures())
			System.out.println(failure.toString());
		
		if (result.wasSuccessful())
			System.out.println("Success");
		else
			System.out.println("Failure");
		
		//Add records
		Blockchain block = new Blockchain();
		Record r1 = new Record("Sally", "Sanchez", 123456789, "Provider1");
		Record r2 = new Record("Mark", "Johnson", 234567890, "Provider2");
		Record r3 = new Record("Michael", "Jordan", 345678901, "Provider3");
		block.addRecord(r1);
		block.addRecord(r2);
		block.addRecord(r3);
		
		//Print all records
		block.print();
		
		//Print by first name
		System.out.print(block.getListByPatient("Mark"));
	}

}
