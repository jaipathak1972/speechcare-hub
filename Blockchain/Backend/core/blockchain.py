import sys
sys.path.append('/Users/Dell/OneDrive/Desktop/blockchain/bitcoin')

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.core.util.util import hash256
import time
import json

ZERO_HASH = '0' * 64
VERSION= 1

class Blockchain:
    def __init__(self) -> None:
        self.chain = []
        self.GenesisBlock()

    def GenesisBlock(self):
        BlockHeight = 0
        PrevBlockHash = ZERO_HASH
        self.addblock(BlockHeight,PrevBlockHash)

    def addblock(self,BlockHeight, PrevBlockHash):
        timestamp = int(time.time())
        transaction = f"Codies Alert sent {BlockHeight} send to jeo"
        merkleRoot = hash256(transaction.encode()).hex()
        bits = "fFFf001f"
        blockheader = BlockHeader(VERSION,PrevBlockHash,merkleRoot,timestamp,bits) 
        blockheader.mine()
        self.chain.append(Block(BlockHeight,1,blockheader.__dict__,1,transaction).__dict__)
        print(json.dumps(self.chain, indent=4))

    def main(self):
        while True:
            lastBlock = self.chain[::-1]
            blockHeight = lastBlock[0]["Height"] + 1
            preBlockHash = lastBlock[0]['BlockHeader']['blockhash']
            self.addblock(blockHeight,preBlockHash)


if __name__ == "__main__":

    blockchain = Blockchain()
    blockchain.main()  