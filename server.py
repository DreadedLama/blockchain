from block import *
from flask import Flask
from flask import jsonify
from flask import render_template
import json
import os
import mining
import key_generate

app = Flask(__name__)

@app.route('/mine', methods=['GET'])
def mine():
    # demo block
    blocks = syncBlocks()
    demo_block = Block(len(blocks), 'temporary data', None, blocks[-1]['hash'], str(date.datetime.now())).block
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
    blocks = syncBlocks()
    return render_template('block_display.html', block=blocks[int(number)])
    return jsonify(blocks[int(number)]), 200

@app.route('/key-generator', methods=['GET'])
def generateKey():
    private_key, public_key = key_generate.generate_RSA()
    key = {
        "private": private_key,
        "public": public_key 
    }
    return render_template('rsa_key_display.html', key=key)

app.run(host='0.0.0.0', port=5000)

