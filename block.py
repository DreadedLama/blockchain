import hashlib
import json
# from time import time
import datetime as date
import os
from operator import itemgetter

class Block:

    def __init__(self, index, data, nonce, previousHash, timestamp):
        self.block = {
            "index": index,
            "data": data,
            "previousHash": previousHash,
            "timestamp": timestamp,
            "nonce": nonce, 
            "hash": None
        }

################## INCORRECT WAY
# def calculateBlockHash(block):
#     hashString = json.dumps(block, sort_keys=True).encode()
#     return hashlib.sha256(hashString).hexdigest()
##################
def calculateBlockHash(block):
    hashString = str(block['index'])+block['data']+str(block['previousHash'])+str(block['timestamp'])+str(block['nonce'])
    return hashlib.sha256(hashString.encode()).hexdigest()

def createNewBlock(blockData):
    pass

def createGenesisBlock():
    firstBlock = Block(0, 'Fucking ass block', 0, None, str(date.datetime.now()))
    firstBlock.block['hash'] = calculateBlockHash(firstBlock.block)
    return firstBlock

def saveBlock(block):
    blockchaindata_dir = 'blockchaindata'
    if not os.path.exists(blockchaindata_dir):
        os.mkdir(blockchaindata_dir)

    #saving file
    indexString = str(block['index']).zfill(5)
    filename = "{}/{}.json".format(blockchaindata_dir, indexString)
    with open(filename, 'w') as block_file:
        # !dump vs dumps
        block_string = json.dumps(block)
        json.dump(block_string, block_file)

# fB = createGenesisBlock()
# saveBlock(fB.block)  
# with open('blockchaindata/00000.json', 'r') as rf:
#     data = json.load(rf)
# # print(data)
# data = (json.loads(data))
# print(calculateBlockHash(data))

def syncBlocks():
    blockchaindata_dir = 'blockchaindata'
    blocksList = []
    if os.path.exists(blockchaindata_dir):
        for filename in os.listdir(blockchaindata_dir):
            if filename.endswith('.json'):
                filepath ="{}/{}".format(blockchaindata_dir, filename)
                with open(filepath, 'r') as block_file:
                    blockInfo = json.loads(json.load(block_file))
                    blockObj = Block(blockInfo['index'], blockInfo['data'], blockInfo['nonce'], blockInfo['previousHash'], blockInfo['timestamp'])
                    blockObj.block['hash'] = blockInfo['hash']
                    blocksList.append(blockObj.block)
    blocksList = sorted(blocksList, key=itemgetter('index'))

    return blocksList

# a = syncBlocks()
# print(len(a))