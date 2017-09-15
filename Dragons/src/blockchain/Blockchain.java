package blockchain;

import java.util.Date;
import java.util.LinkedList;

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
	
	public LinkedList<Record> getListByPatient(String name) {
		LinkedList<Record> l = list;
		LinkedList<Record>  listWithName = new LinkedList<Record>();
		for(int i = 0; i < l.size(); i++) {
			if (l.get(i).getFirstName().equals(name)) {
				listWithName.add(l.get(i));
			}
		}
		return listWithName;
	}
	
	public LinkedList<Record> getListByProvider(String provider) {
		LinkedList<Record> l = list;
		LinkedList<Record> listWithProvider = new LinkedList<Record>();
		for(int i = 0; i < l.size(); i++) {
			if (l.get(i).getProvider().equals(provider)) {
				listWithProvider.add(l.get(i));
			}
		}
		return listWithProvider;
	}
	
	//TODO
	public LinkedList<Record> getListByDateWindow(Date start, Date end) {
		return new LinkedList<Record>();
	}
	
	public void print() {
		System.out.println("Records: ");
		System.out.println(list);
	}
}
