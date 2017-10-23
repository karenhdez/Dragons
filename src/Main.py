import threading

#from IO.Server import *
#from IO.Client import *
from Blockchain.Block import *

def main():

    #Return block's personal sha256
    record1 = Record('a', 'b', 1, 'c')
    block1 = Block(record1)
    print(block1.SHA256)

    #Return hash of current and previous block
    record2 = Record('d', 'e', 2, 'f')
    block2 = Block(record2)
    print(block2.generateConcatenatedSHA256(block1))



    # s = Server()
    # threading.Thread(target=s.main).start()
    #
    # c = Client()
    # threading.Thread(target=c.main).start()


main()