

class Client:

	def __init__(self, f, l, ssn, p):

		pass


	def displayMenu(self):

		print("===================================")
		print("Please Enter an Option:")
		print("(N) - New User")
		print("(G) - Getting Info")
		print("(Q) - Quit")
		print("===================================")


	def getUserOption(self, stdIn):

		option = ""
        while True:
            print("Option:")
            option = stdIn.readLine()
            if not option.equals("N") and not option.equals("n") and not option.equals("Q") and not option.equals("q"):
                break

		return option


	def getUserInfo(self, stdIn, out):

		self.getUserFirstName(stdIn, out)
        self.getUserLastName(stdIn, out)
        self.getUserSSN(stdIn, out)
        self.getUserProvider(stdIn, out)


	def getUserFirstName(self, stdIn, out):

		firstName = ""
        while True:
            print("Enter your first name:")
            firstName = stdIn.readLine()
            if len(firstName) != 0:
                break

		print(firstName)


	def getUserLastName(self, stdIn, out):

		lastName = ""
        while True:
			print("Enter your last name:")
			lastName = stdIn.readLine()
		    if len(lastName) != 0:
                break

		print(lastName)


	def getUserSSN(self, stdIn, out):

		ssn = ""
        while True:
			print("Enter your social security number:")
			ssn = stdIn.readLine()
		    if len(ssn) == 0:
                break

		print(ssn)


	def getUserProvider(self, stdIn, out):

		provider = ""
        while True:
            print("Enter your medical provider:")
			provider = stdIn.readLine()
		    if len(provider) == 0:
                break

		print(provider)


	def main(self, args):

		try:
			_sock = Socket("localhost", 6019)
			_out = PrintWriter(_sock.getOutputStream(), True)
			_in = BufferedReader(InputStreamReader(_sock.getInputStream()))
			_stdIn = BufferedReader(InputStreamReader(System.in))

			self.displayMenu()
			option = self.getUserOption(_stdIn)
			print(option)

			if option.equals("N") or option.equals("n"):
				self.getUserInfo(stdIn, _out)
				_stdIn.close()
				_in.close(
				_out.close()
				_sock.close()

			elif option.equals("Q") or option.equals("q"):
				_stdIn.close()
				_in.close()
				_out.close()
				_sock.close()
