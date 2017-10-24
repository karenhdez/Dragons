import rsa

from block import Block
import time
import hashlib
import json

class Blockchain:

    def __init__(self):
        self.current_patient_events = []
        self.blockchain = []

        #Add genesis block to the blockchain
        self.add_block(previous_hash=1, proof=100)

    def add_patient_event(self, patient_id, timestamp, ssn, name, provider):
        '''
        This function will add a new patient event into the current list of
        patient events to be mined into the next Block

        :param patient_id:
        :param ssn:
        :param name:
        :param provider:
        :return:
        '''

        self.current_patient_events.append({
            'patient_id': patient_id,
            'timestamp': timestamp,
            'ssn': ssn,
            'name': name,
            'provider': provider
        })

        return self.last_block['index'] + 1
    
    def add_block(self, proof, previous_hash=None):
        '''
        Add a new Block into the Blockchain.


        :param last_block:
        :param data:
        :return:
        '''

        block = {
            'index': len(self.blockchain) + 1,
            'timestamp': time.time(),
            'patient_events': self.current_patient_events,
            'proof': proof,
            'previous_hash': previous_hash or self.hash_block(self.blockchain[-1])
        }

        block = json.dumps(block)
        block = block.encode('utf8')

        (pubkey, privkey) = rsa.newkeys(1024)
        block = rsa.encrypt(block, pubkey)

        #Privkey needs to be added to database


        # Reset the current list of patient events array
        self.current_patient_events = []

        self.blockchain.append(block)

        return block

    @staticmethod
    def hash_block(block):
        '''
        Hashes a block using SHA-256
        :param block:
        :return:
        '''


        serialized_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(serialized_block).hexdigest()

    @property
    def last_block(self):
        '''
        Returns the last block in the chain
        '''
        return self.blockchain[-1]
    
    def is_blockchain_valid(self):
        pass

    @staticmethod
    def proof_of_work(block):
        '''
        Hashcash proof of work algorithms will find a nonce such that the hash of the nonce and block
        will give us 4 leading zeros within our new hash.

        This will also prove as valid proof ofwork
        :param block:
        :return:
        '''
        complete = False
        proof = 0

        serialized_block = json.dumps(block, sort_keys=True).encode()

        curr_hash = None
        while complete == False:
            proof = proof + 1
            sha = hashlib.sha256()
            sha.update(serialized_block + str(proof).encode())
            curr_hash = sha.hexdigest()

            # slows performance drastically
            ## print curr_hash

            if curr_hash.startswith('00000'):
                complete = True
        return proof, curr_hash

