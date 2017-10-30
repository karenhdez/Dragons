# Dragoncoin
SE394/IS376 Team Dragon blockchain project. <br>
<br>
A blockchain solution to sharing patient information.


``` bash
$ 
$ python network.py
```



##Install Requirements
You must have <br>

pip install -r requirements.txt


##How to Run the app
1.) Install docker from docs.docker.com<br>
2.) Run the following command from the command line


## Endpoints


### Requesting the Blockchain of a node

* `GET 127.0.0.1:5000/blockchain`

### Mining blocks and adding it to the blockchain

* `GET 127.0.0.1:5000/mine`

### Adding a new transaction

* `POST 127.0.0.1:5000/patient_event/new`

* __Body__: A transaction to be added

  ```json
  {
    "sender": "sender-address-te33412uywq89234g",
    "recipient": "recipient-address-j3h45jk23hjk543gf",
    "amount": 1000
  }
  ```

### Register a new node in the network
Currently you must add each new node to each running node.

* `POST 127.0.0.1:5000/nodes/register`

* __Body__: A list of nodes to add

  ```json
  {
     "nodes": ["http://127.0.0.1:8001", <more-nodes>]
  }
  ```

### Resolving Blockchain differences in each node

* `GET 127.0.0.1:8000/nodes/resolve`
