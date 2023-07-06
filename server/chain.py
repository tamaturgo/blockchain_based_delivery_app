from block import Block
import datetime
from cryptography.fernet import Fernet
import hashlib

try: 
    with open('key.key', 'rb') as f:
        key = f.read()
except FileNotFoundError:
    key = Fernet.generate_key()
    with open('key.key', 'wb') as f:
        f.write(key)
cipher_suite = Fernet(key)


class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 4
        self.load_blockchain()
        
    def load_blockchain(self):
        try:
            with open('blockchain.txt', 'r') as f:
                indexes = []
                hashes = []
                previous_hashes = []
                datas = []
                timestamps = []
            
                for line in f.readlines():
                    line = cipher_suite.decrypt(line.encode('utf-8')).decode('utf-8')
                    if line.startswith('Block #'):
                        indexes.append(int(line[7:].replace('\n','')))
                    elif line.startswith('Hash: '):
                        hashes.append(line[6:])
                    elif line.startswith('Previous: '):
                        previous_hashes.append(line[10:])
                    elif line.startswith('Data: '):
                        datas.append(line[6:])
                    elif line.startswith('Timestamp: '):
                        timestamps.append(line[12:])
                for i in range(len(indexes)):
                    block = Block(indexes[i], timestamps[i].replace('\n',''), datas[i].replace('\n',''))
                    block.hash = hashes[i].replace('\n','')
                    block.previous_hash = previous_hashes[i].replace('\n','')
                    self.chain.append(block)

        except FileNotFoundError:
            print('Blockchain file not found. Creating new blockchain...')
            self.chain = [self.create_genesis_block()]
            self.save_blockchain()
        except Exception as e:
            print('Error loading blockchain: {}'.format(e))
            self.chain = [self.create_genesis_block()]
            self.save_blockchain()

    def create_genesis_block(self):
        genesis = Block(0, datetime.datetime.now(), 'Genesis Block')
        genesis.hash = genesis.calculate_hash()
        return genesis

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.save_blockchain()

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.previous_hash != previous_block.hash:
                print('Previous hash is not equal')
                print ('Current block hash: {}'.format(current_block.previous_hash))
                print ('Previous block hash: {}'.format(previous_block.hash))
                return False
        return True

    def save_blockchain(self):
        print('Saving blockchain...')
        if self.is_chain_valid():
            with open('blockchain.txt', 'w') as f:
                for block in self.chain:
                    f.write(cipher_suite.encrypt('Block #{}'.format(block.index).encode('utf-8')).decode('utf-8') + '\n')
                    f.write(cipher_suite.encrypt('Hash: {}'.format(block.hash).encode('utf-8')).decode('utf-8') + '\n')
                    f.write(cipher_suite.encrypt('Previous: {}'.format(block.previous_hash).encode('utf-8')).decode('utf-8') + '\n')
                    f.write(cipher_suite.encrypt('Data: {}'.format(block.data).encode('utf-8')).decode('utf-8') + '\n')
                    f.write(cipher_suite.encrypt('Timestamp: {}'.format(block.timestamp).encode('utf-8')).decode('utf-8') + '\n')
        else:
            print('Blockchain is not valid')

    def __str__(self):
        return 'Blockchain:\n{}'.format('\n'.join(str(block) for block in self.chain))
