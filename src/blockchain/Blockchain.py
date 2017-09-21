from System import *
from System.Collections.Generic import *
from System.Collections import *
from System.sql.Timestamp import *


class Blockchain(object):

	def __init__(self):
		self._list = LinkedList[Record]()

	def addRecord(self, r):
		self._list.add(r)

	def getList(self):
		return self._list

	def getListByPatient(self, firstName, lastName):
		l = self._list
		results = LinkedList[Record]()
		i = 0
		while i < l.size():
			if l.get(i).getFirstName().equals(firstName) and l.get(i).getLastName().equals(lastName):
				results.add(l.get(i))
			i += 1
		return results

	def getListByProvider(self, provider):
		l = self._list
		results = LinkedList[Record]()
		i = 0
		while i < l.size():
			if l.get(i).getProvider().equals(provider):
				results.add(l.get(i))
			i += 1
		return results

	def getListByDateWindow(self, start, end):
		l = self._list
		results = LinkedList[Record]()
		i = 0
		while i < l.size():
			if (l.get(i).getTimestamp().compareTo(start) > 0) and (l.get(i).getTimestamp().compareTo(end) < 0):
				results.add(l.get(i))
			i += 1
		return results

	def print(self):
		Console.WriteLine("Records: ")
		Console.WriteLine(self._list)
}
