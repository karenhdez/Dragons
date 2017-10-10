import hashlib


class Block:
    '''
    Block Structure
    ----------------
    * index
    * timestamp
    * data (encrypted key-value pairs)
    * link to previous hash
    * hash of the block

    '''

    def __init__(self, index, timestamp, data, previous_hash):
        '''
        Initialize the Block
        Block(index,timestamp,data,previous_hash)

        '''

        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()


    def hash_block(self):
        '''
        Python's build-in hash is not a true hash,
        we'll be using hashlib for true 256 hashing functionality

        For Python's unicode you must use utf-8 for all string types.
        '''
        sha = hashlib.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash)).encode('utf-8'))

        return sha.hexdigest()
