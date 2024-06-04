# Blockchain Based Delivery App

This repository contains a blockchain-based application for managing product deliveries. The application provides a RESTful API to add, update, and retrieve delivery information, ensuring data integrity and transparency by leveraging blockchain technology. The frontend is built using Svelte.
Table of Contents

- Features
- API Endpoints
    - Add Product Delivery
    - Get Product Delivery
    - Update Product Delivery Status
    - Search by Name
    - Search by Sender
    - Search by Receiver
    - Get Blockchain
- Running the API
    - Requirements
    - Installation
    - Run the API

##Frontend

Features

- Add Product Delivery: Add new delivery information to the blockchain.
- Get Product Delivery: Retrieve details of a specific delivery using its block index.
- Update Delivery Status: Update the status of an existing delivery.
- Search Deliveries: Search for deliveries by product name, sender, or receiver.
- View Blockchain: Access the entire blockchain to see all deliveries.

## API Endpoints

Add Product Delivery

Add a new product delivery to the blockchain.

    URL: /delivery
    Method: POST
    Request Body:
        product (string, required): Product name
        product_id (string, required): Product ID
        sender (string, required): Sender name
        receiver (string, required): Receiver name
        amount (float, required): Delivery amount
    Response:
        Status: 201 Created
        Body: JSON object containing the newly created block

Get Product Delivery

Retrieve information about a specific product delivery.

    URL: /delivery/{block_index}
    Method: GET
    Parameters: block_index (int): Index of the block
    Response:
        Status: 200 OK
        Body: JSON object containing the block information
    Error Response:
        Status: 404 Not Found
        Body: JSON object with an error message if the block is not found

Update Product Delivery Status

Update the status of a product delivery.

    URL: /delivery/{block_index}
    Method: PUT
    Parameters: block_index (int): Index of the block
    Request Body:
        status (string, required): New status of the delivery
    Response:
        Status: 200 OK
        Body: JSON object containing the updated block
    Error Response:
        Status: 404 Not Found
        Body: JSON object with an error message if the block is not found

Search by Name

Search for product deliveries by product name.

    URL: /delivery/search
    Method: GET
    Parameters: product (string, required): Product name
    Response:
        Status: 200 OK
        Body: JSON array containing the matching blocks
    Error Response:
        Status: 404 Not Found
        Body: JSON object with an error message if no blocks are found

Search by Sender

Search for product deliveries by sender name.

    URL: /delivery/sender/{sender}
    Method: GET
    Parameters: sender (string): Sender name
    Response:
        Status: 200 OK
        Body: JSON array containing the matching blocks
    Error Response:
        Status: 404 Not Found
        Body: JSON object with an error message if no blocks are found

Search by Receiver

Search for product deliveries by receiver name.

    URL: /delivery/receiver/{receiver}
    Method: GET
    Parameters: receiver (string): Receiver name
    Response:
        Status: 200 OK
        Body: JSON array containing the matching blocks
    Error Response:
        Status: 404 Not Found
        Body: JSON object with an error message if no blocks are found

Get Blockchain

Get the full blockchain.

    URL: /chain
    Method: GET
    Response:
        Status: 200 OK
        Body: JSON array containing the blockchain

Running the API
Requirements

    Python 3.6+

The frontend of this application is built using Svelte. To run the frontend, navigate to the frontend directory and follow the instructions in its own README.

This repository provides a secure and transparent way to manage product deliveries using blockchain technology, ensuring all transactions are immutable and traceable.
