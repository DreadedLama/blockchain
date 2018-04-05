from peersinfo import *
import requests
from chain import *
from block import syncBlocks

def broadcastBlock(block):
    for peer in PEERS:
        url = peer + '/mined'
        try:
            requests.post(url, json=block)
        except requests.exceptions.ConnectionError:
            print(url+" is not running")

def getBlockchain():
    bestChain = syncBlocks()
    for peer in PEERS:
        url = peer+'/blockchain'
        try:
            res = requests.get(url)
            chain = res.json()
            chain = chain["chain"]
            #print(chain)
            print(is_valid_chain(chain))
            if is_valid_chain(chain) and len(chain) > len(bestChain):
                bestChain = chain
                print('here')
        except requests.exceptions.ConnectionError:
            print(url+" is not running")

    print('Syncing remote chain')
    saveChain(bestChain)