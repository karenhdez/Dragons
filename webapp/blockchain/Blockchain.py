from Block import Block
import datetime


class Blockchain:

    def create_genesis_block(self):
        '''The first block of the blockchain.
        We will start the index at 0. '''
        return Block(0, datetime.datetime.now(), "Genesis Block","0")

    def next_block(last_block):
        next_block_index = last_block.index + 1 #increment index by 1
        next_block_timestamp = datetime.datetime.now()
        next_block_data = "Hello my block ID is " + str(next_block_index) #TODO this data will be in json
        next_block_hash = last_block.hash()
        return Block(next_block_index, next_block_timestamp, next_block_data, next_block_hash)


honeybadgercoin = Blockchain()

#Start Genesis Block
honeybadgercoin.create_genesis_block()

