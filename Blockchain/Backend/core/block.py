class Block :
    """
    Block is a storage container that stores transactions
    """

    def __init__(self,Height,Blocksize, BlockHeader,TxCount, Txs) -> None:
        self.Height = Height
        self.Blocksize = Blocksize
        self.BlockHeader = BlockHeader
        self.TxCount = TxCount
        self.Txs = Txs