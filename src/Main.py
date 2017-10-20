import threading
from Handler import Handler
from IO.Client import Client
from IO.Server import Server
from Blockchain.Block import *


def main():

    # r = Record('a', 'b', 1, 'c')
    # b = Block(hashlib.sha224("asdf").hexdigest(), r)
    # print(b.SHA256)

    r = Record('a', 'b', 1, 'c')

    s = Server()
    threading.Thread(target=s.main).start()

    while True:
        if s.port is not None:
            break

    c = Client(s.port)
    threading.Thread(target=c.main).start()

    #s.addClientRecord(r)


main()