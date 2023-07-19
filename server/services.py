from chain import Blockchain
from block import Block
import datetime
import re
import hashlib
import random


class Services:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def add_product_delivery(self, product, product_id, sender, receiver, amount):
        data = {
            'product': product,
            'product_id': 0,
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'timestamp': datetime.datetime.now(),
            'status': 'pending',
            'block_version': 1,
        }

        # Generate product_id based on pattern (Product Name + Amout * 3 Alphanumeric Characters)
        product_id_pattern = re.compile(r"([a-zA-Z]+)")
        alphanumeric_random = ''.join(random.choice('0123456789ABCDEF') for i in range(3))
        product_id = product_id_pattern.search(product).group(1).upper() + str(amount) + alphanumeric_random
        data['product_id'] = product_id

        block = Block(len(self.blockchain.chain),
                      datetime.datetime.now(), data)
        self.blockchain.add_block(block)
        return block

    def update_product_delivery_status(self, product_id, new_status):
        search_for_string = "'product_id': '{}'".format(product_id.lower())
        for block in self.blockchain.chain:
            if search_for_string in str(block.data).lower():
                data_copy = block.data
                data_dict = eval(str(data_copy))
                print(data_dict['status'])
                data_dict['status'] = new_status
                data_dict['block_version'] += 1
                data_dict['timestamp'] = datetime.datetime.now()
                data = {
                    'product': data_dict['product'],
                    'product_id': data_dict['product_id'],
                    'sender': data_dict['sender'],
                    'receiver': data_dict['receiver'],
                    'amount': data_dict['amount'],
                    'timestamp': data_dict['timestamp'],
                    'status': data_dict['status'],
                    'block_version': data_dict['block_version'],
                }
                block = Block(len(self.blockchain.chain),
                              datetime.datetime.now(), data)
                self.blockchain.add_block(block)
                return block
        return None

    def search_by_name(self, product):
        blocks_found = []
        for block in self.blockchain.chain:
            search_for_string = "'product': '{}'".format(product.lower())
            if search_for_string in str(block.data).lower():
                blocks_found.append(block)
        return blocks_found

    def search_by_sender(self, sender):
        blocks_found = []
        for block in self.blockchain.chain:
            search_for_string = "'sender': '{}'".format(sender.lower())
            if search_for_string in str(block.data).lower():
                blocks_found.append(block)
        if len(blocks_found) > 0:
            most_recent_block = blocks_found[0]
            for block in blocks_found:
                if block.index > most_recent_block.index:
                    most_recent_block = block
            return most_recent_block
        return None

    def search_by_receiver(self, receiver):
        blocks_found = []
        for block in self.blockchain.chain:
            search_for_string = "'receiver': '{}'".format(receiver.lower())
            if search_for_string in str(block.data).lower():
                blocks_found.append(block)
        if len(blocks_found) > 0:
            most_recent_block = blocks_found[0]
            for block in blocks_found:
                if block.index > most_recent_block.index:
                    most_recent_block = block
            return most_recent_block
        return None

    def search_by_product_id(self, product_id):
        blocks_found = []
        for block in self.blockchain.chain:
            search_for_string = "'product_id': '{}'".format(product_id.lower())
            if search_for_string in str(block.data).lower():
                blocks_found.append(block)
        return blocks_found
