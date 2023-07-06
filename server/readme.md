# Delivery API

API for managing product deliveries.

## Add Product Delivery

Add a new product delivery to the blockchain.

- **URL:** `/delivery`
- **Method:** `POST`
- **Request Body:**
    - `product` (string, required): Product name
    - `product_id` (string, required): Product ID
    - `sender` (string, required): Sender name
    - `receiver` (string, required): Receiver name
    - `amount` (float, required): Delivery amount
- **Response:**
    - HTTP Status Code: 201 Created
    - JSON object containing the newly created block

## Get Product Delivery

Get information about a specific product delivery.

- **URL:** `/delivery/{block_index}`
- **Method:** `GET`
- **Parameters:**
    - `block_index` (int): Index of the block
- **Response:**
    - HTTP Status Code: 200 OK
    - JSON object containing the block information
- **Error Response:**
    - HTTP Status Code: 404 Not Found
    - JSON object with an error message if the block is not found

## Update Product Delivery Status

Update the status of a product delivery.

- **URL:** `/delivery/{block_index}`
- **Method:** `PUT`
- **Parameters:**
    - `block_index` (int): Index of the block
- **Request Body:**
    - `status` (string, required): New status of the delivery
- **Response:**
    - HTTP Status Code: 200 OK
    - JSON object containing the updated block
- **Error Response:**
    - HTTP Status Code: 404 Not Found
    - JSON object with an error message if the block is not found

## Search by Name

Search for product deliveries by product name.

- **URL:** `/delivery/search`
- **Method:** `GET`
- **Parameters:**
    - `product` (string, required): Product name
- **Response:**
    - HTTP Status Code: 200 OK
    - JSON array containing the matching blocks
- **Error Response:**
    - HTTP Status Code: 404 Not Found
    - JSON object with an error message if no blocks are found

## Search by Sender

Search for product deliveries by sender name.

- **URL:** `/delivery/sender/{sender}`
- **Method:** `GET`
- **Parameters:**
    - `sender` (string): Sender name
- **Response:**
    - HTTP Status Code: 200 OK
    - JSON array containing the matching blocks
- **Error Response:**
    - HTTP Status Code: 404 Not Found
    - JSON object with an error message if no blocks are found

## Search by Receiver

Search for product deliveries by receiver name.

- **URL:** `/delivery/receiver/{receiver}`
- **Method:** `GET`
- **Parameters:**
    - `receiver` (string): Receiver name
- **Response:**
    - HTTP Status Code: 200 OK
    - JSON array containing the matching blocks
- **Error Response:**
    - HTTP Status Code: 404 Not Found
    - JSON object with an error message if no blocks are found

## Get Blockchain

Get the full blockchain.

- **URL:** `/chain`
- **Method:** `GET`
- **Response:**
    - HTTP Status Code: 200 OK
    - JSON array containing the blockchain


# Run the API

## Requirements

- Python 3.6+

first install the requirements

```bash
pip install -r requirements.txt
```

## Run the API

```bash
python app.py
```

