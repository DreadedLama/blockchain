from block import *
import shutil

def is_valid_chain(chain):

    if len(chain) is 0: # in case if other peer has no blocks
        return False
 
    prevBlock = chain[0]
    for curBlock in chain[1:]:
        if prevBlock['index']+1 != curBlock['index']:
            return False
        if curBlock['previousHash'] != prevBlock['hash']:
            return False

        if curBlock['hash'] != calculateBlockHash(curBlock): #in case if somone alters hash
            return False
        sha256hash = curBlock['hash']
        noOfZeros = 0
        '''Difficulty to be checked'''
        # for i in sha256hash:
        #     if i == '0':
        #         noOfZeros += 1
        #     else:
        #         break

        # if noOfZeros < minZeros:
        #     return False
        prevBlock = curBlock
    return True

def saveChain(chain):
    # first block
    try:
        shutil.rmtree('blockchaindata')
    except FileNotFoundError:
        pass

    saveBlock(chain[0], 5, isFirstBlock=True)
    for block in chain:
        saveBlock(block, 5)
          