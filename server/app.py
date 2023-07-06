from chain import *
from services import *
from flask import Flask, request, jsonify 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
chain = Blockchain()
service = Services(chain)

@app.route('/delivery', methods=['POST'])
def add_product_delivery():
    product = request.form['product']
    product_id = request.form['product_id']
    sender = request.form['sender']
    receiver = request.form['receiver']
    amount = request.form['amount']
    new_block = service.add_product_delivery(product, product_id, sender, receiver, amount)

    return jsonify(new_block.to_dict()), 201

@app.route('/delivery/<int:block_index>', methods=['GET'])
def get_product_delivery(block_index):
    block = service.search_by_product_id(str(block_index))
    if block:
        return jsonify({'block': str(block)}), 200
    else:
        return jsonify({'message': 'Bloco não encontrado.'}), 404

@app.route('/delivery/<int:block_index>', methods=['PUT'])
def update_product_delivery_status(block_index):
    new_status = request.form['status']
    block = service.update_product_delivery_status(block_index, new_status)
    if block:
        return jsonify(block.to_dict()), 200
    else:
        return jsonify({'message': 'Bloco não encontrado.'}), 404
    
@app.route('/delivery/search', methods=['GET'])
def search_by_name():
    product = request.form['product']
    blocks = service.search_by_name(product)
    if len(blocks) > 0:
        return jsonify([block.to_dict() for block in blocks]), 200
    else:
        return jsonify({'message': 'Bloco não encontrado.'}), 404
    
@app.route('/delivery/sender/<string:sender>', methods=['GET'])
def search_by_sender(sender):
    blocks = service.search_by_sender(sender)
    if len(blocks) > 0:
        return jsonify([block.to_dict() for block in blocks]), 200
    else:
        return jsonify({'message': 'Bloco não encontrado.'}), 404

@app.route('/delivery/receiver/<string:receiver>', methods=['GET'])
def search_by_receiver(receiver):
    blocks = service.search_by_receiver(receiver)
    if len(blocks) > 0:
        return jsonify([block.to_dict() for block in blocks]), 200
    else:
        return jsonify({'message': 'Bloco não encontrado.'}), 404
    
@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify([block.to_dict() for block in chain.chain]), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
