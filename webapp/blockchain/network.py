from blockchain import Blockchain

import hashlib
import json

import time
from uuid import uuid4

from flask import Flask, request, jsonify
import requests


app = Flask(__name__)

#this will create a random name for the node
node_identifier = str(uuid4()).replace('-', '')

dragoncoin = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    proof, hashed_block = dragoncoin.proof_of_work(dragoncoin.last_block)
    results = {"message": "New block was added to the blockchain",

                "proof": proof,
                "hashed_block": hashed_block}
               
    return jsonify(results), 201

@app.route('/patient_event/new', methods=['POST'])
def new_patient_event():
    ''' Post values should be: 
    patient_id
    timestamp
    SSN
    name
    provider
    '''
    values = request.get_json(force=True)
    
    #Check that the required fields were submitted by POST
    required = ['patient_id', 'ssn', 'name', 'provider']
    
    if not all(k in values for k in required):
        return 'Missing values', 400
    
    #Create a new patient event
    
    index = dragoncoin.add_patient_event(values['patient_id'],
                                        str(time.time()),
                                        values['ssn'],
                                        values['name'],
                                        values['provider'])
    
  
    tender = values
    response = {'message': f'{tender} Patient event will be added to the Block {index}'}
    
    return jsonify(response), 201

@app.route('/blockchain', methods=['GET'])
def full_blockchain():
    

    response = {
        'chain': dragoncoin.blockchain,
        'length': len(dragoncoin.blockchain)
    }
    return jsonify(response)

#Mine and add block
@app.route('/add_block', methods=['GET'])
def add_block():
    proof, hashed_block  = dragoncoin.proof_of_work(dragoncoin.last_block)
    response = dragoncoin.add_block(proof)
    return jsonify(response)
    
if __name__ =='__main__':
    app.run(debug=True,port=5000)