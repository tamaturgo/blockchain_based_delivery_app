import hashlib
import datetime

class Block:

    def __init__(self, index, timestamp, data):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.nonce = 0
        self.previous_hash = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(data.encode('utf-8')).hexdigest()
    
    def mine_block(self, difficulty):
        target = '0'*difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print('Block mined: ', self.hash)

    def __str__(self):
        return 'Block #{}'.format(self.index) + '\n' + \
               'Hash: {}'.format(self.hash) + '\n' + \
               'Previous: {}'.format(self.previous_hash) + '\n' + \
               'Data: {}'.format(self.data) + '\n' + \
               'Timestamp: {}'.format(self.timestamp) + '\n'
    def to_dict(self):
        try:
            data_eval = eval(str(self.data))
        except:
            data_eval = self.data
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': data_eval,
            'nonce': self.nonce,
            'previous_hash': self.previous_hash,
            'hash': self.hash
        }
    