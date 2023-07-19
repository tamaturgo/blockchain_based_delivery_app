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
    data = request.get_json()
    product = data['product']
    product_id = data['product_id']
    sender = data['sender']
    receiver = data['receiver']
    amount = data['amount']
    new_block = service.add_product_delivery(
        product, product_id, sender, receiver, amount)
    return jsonify(new_block.to_dict()), 201


@app.route('/delivery/<int:block_index>', methods=['GET'])
def get_product_delivery(block_index):
    block = service.search_by_product_id(str(block_index))
    if block:
        return jsonify({'block': str(block)}), 200
    else:
        return jsonify({'message': 'Bloco não encontrado.'}), 404


@app.route('/delivery/<string:block_product_name>', methods=['PUT'])
def update_product_delivery_status(block_product_name):
    new_status = request.args.get('status')
    print (new_status + " " + block_product_name)
    blocks = service.search_by_name(block_product_name)
    product_id_pattern = re.compile(r"'product_id': '(.+?)'")
    block_index = product_id_pattern.search(str(blocks[0].data)).group(1)
    block = service.update_product_delivery_status(block_index, new_status)
    if block:
        return jsonify(block.to_dict()), 200
    else:
        return jsonify({'message': 'Bloco não encontrado.'}), 404
 


@app.route('/delivery/search', methods=['GET'])
def search_by_name():
    product = request.args.get('product')
    blocks = service.search_by_name(product)
    if len(blocks) > 0:
        return jsonify([block.to_dict() for block in blocks]), 200
    blocks = service.search_by_product_id(product)
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
    app.run(host='0.0.0.0', port=80, debug=True)
