import threading

#from IO.Server import *
#from IO.Client import *
from Blockchain.Block import *

def main():

    r = Record('a', 'b', 1, 'c')
    b = Block(hashlib.sha224("asdf").hexdigest(), r)
    print(b.SHA256)

    # s = Server()
    # threading.Thread(target=s.main).start()
    #
    # c = Client()
    # threading.Thread(target=c.main).start()


main()