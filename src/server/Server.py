

public class Server {


    def __init__(self):

        pass


    def generateClientRecord(self, firstName, lastName, ssn, provider):

        return Record(firstName, lastName, ssn, provider)


	def main(self, String[] args):

		Blockchain block = Blockchain()
		try:
            _serverSocket = ServerSocket(6019)
            _clientSocket = serverSocket.accept()
            _out = PrintWriter(clientSocket.getOutputStream(), True)
            _in = BufferedReader(InputStreamReader(clientSocket.getInputStream()))

            print("Connection made")
            clientOption = in.readLine()

            if clientOption.equals("N") or clientOption.equals("n"):
                firstName = in.readLine()
                lastName = in.readLine()
                ssn = Integer.parseInt(in.readLine())
                provider = in.readLine()
                clientRecord = self.generateClientRecord(firstName, lastName, ssn, provider)
                block.addRecord(clientRecord)
                print(block.getListByPatient(firstName))
            elif clientOption.equals("Q") or clientOption.equals("q"):
                in.close()
                out.close()
                clientSocket.close()
                serverSocket.close()
	    catch:
	        print()

}
