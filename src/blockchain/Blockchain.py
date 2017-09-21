package blockchain;

import java.util.Date;
import java.util.LinkedList;
import java.sql.Timestamp;

public class Blockchain {

	private LinkedList<Record> list;
	
	public Blockchain() {
		list = new LinkedList<Record>();
	}
	
	public void addRecord(Record r) {
		list.add(r);
	}
	
	public LinkedList<Record> getList() {
		return list;
	}
	
	public LinkedList<Record> getListByPatient(String firstName, String lastName) {
		LinkedList<Record> l = list;
		LinkedList<Record>  results = new LinkedList<Record>();
		for(int i = 0; i < l.size(); i++) {
			if (l.get(i).getFirstName().equals(firstName) && l.get(i).getLastName().equals(lastName)) {
				results.add(l.get(i));
			}
		}
		return results;
	}
	
	public LinkedList<Record> getListByProvider(String provider) {
		LinkedList<Record> l = list;
		LinkedList<Record>  results = new LinkedList<Record>();
		for(int i = 0; i < l.size(); i++) {
			if (l.get(i).getProvider().equals(provider)) {
				results.add(l.get(i));
			}
		}
		return results;
	}
	
	//TODO: fix so also includes input where start or end is current date (ignores the time)
	public LinkedList<Record> getListByDateWindow(Timestamp start, Timestamp end) {
		LinkedList<Record> l = list;
		LinkedList<Record>  results = new LinkedList<Record>();
		for(int i = 0; i < l.size(); i++) {
			if ((l.get(i).getTimestamp().compareTo(start) > 0) && (l.get(i).getTimestamp().compareTo(end) < 0)) { 
				results.add(l.get(i));
			}
		}
		return results;
	}
	
	public void print() {
		System.out.println("Records: ");
		System.out.println(list);
	}
}
