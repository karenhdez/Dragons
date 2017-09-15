package blockchain;

import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import java.sql.Timestamp;
import java.util.Date;

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
		Record r3 = new Record("Michael", "Jordan", 345678901, "Provider2");
		block.addRecord(r1);
		block.addRecord(r2);
		block.addRecord(r3);
		
		String differentTime = "2017-09-11 00:00:00";
		Timestamp time = Timestamp.valueOf(differentTime);
		r2.setTimestamp(time);
		
		//Print all records
		block.print();
		
		//Search by first name
		System.out.println("Records with requested name:");
		System.out.println(block.getListByPatient("Mark", "Johnson"));
		System.out.println();
		
		//Search by provider
		System.out.println("Records with requested provider:");
		System.out.println(block.getListByProvider("Provider2"));
		System.out.println();
		
		//Search by time window
		String start = "2017-09-13 00:00:00";
		Timestamp startTimestamp = Timestamp.valueOf(start);
		String end = "2017-09-15 00:00:00";
		Timestamp endTimestamp = Timestamp.valueOf(end);
		
		System.out.println("Records created between the given time window");
		System.out.println(block.getListByDateWindow(startTimestamp, endTimestamp));
		System.out.println();
	}

}
