from block import *

def is_valid_chain(chain):
    
    prevBlock = chain[0]
    for curBlock in chain[1:]:
        if prevBlock['index']+1 != curBlock['index']:
            return False
        if not is_valid_block()
          