from block import *
from flask import Flask
from flask import jsonify
import json
import os
import mining

app = Flask(__name__)
blocks = syncBlocks()

@app.route('/mine', methods=['GET'])
def mine():
    # demo block
    demo_block = Block(len(blocks), 'temporary data', None, blocks[-1].block['hash'], str(date.datetime.now())).block
    hashString = str(demo_block['index'])+demo_block['data']+str(demo_block['previousHash'])+str(demo_block['timestamp'])
    nonce, hash = mining.mine(hashString , 5)
    demo_block['nonce'] = nonce
    demo_block['hash'] = hash
    saveBlock(demo_block)

    return "Mined a new block"

@app.route('/', methods=['GET'])
def welcome():
    return "WELCOME!"

@app.route('/block/<number>', methods=['GET'])
def displayBlocks(number):
    return jsonify(blocks[int(number)].block), 200

app.run(host='0.0.0.0', port=5000)

