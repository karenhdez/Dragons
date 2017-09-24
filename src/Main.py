import threading
from Client import *
from Server import *


def main():

    s = Server()
    threading.Thread(target=s.main).start()

    c = Client()
    threading.Thread(target=c.main).start()


main()