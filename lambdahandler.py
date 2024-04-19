import json
import requests
from flask import Flask, jsonify
import awsgi


def lambda_handler(event, context):
    # Your Flask application code goes here
    app = Flask(__name__)

    # Cache to store responses and avoid excessive API requests
    cache = {}

    @app.route('/get_product_details', methods=['GET'])
    def get_product_details():
        urls = [
            "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json",
            "https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json"
        ]

        product_details = []

        for url in urls:
            # Check if response is cached
            if url in cache:
                response = cache[url]
            else:
                response = requests.get(url)
                # Cache the response for future use
                cache[url] = response

            # Extract product details from the response
            if response.status_code == 200:
                data = response.json()
                records = data.get('contents', [])[0].get('mainContent', [])[0].get('contents', [])[0].get('records', [])
                for record in records:
                    product_display_name = record.get('attributes', {}).get('product.displayName')
                    product_all_AvailableSizes = record.get('attributes', {}).get('product.allAvailableSizes')
                    if product_display_name:
                        product_details.append({'product_display_name': product_display_name, 'sizes_available': product_all_AvailableSizes})
            else:
                # Handle error if request fails
                return jsonify({'error': 'Failed to fetch data from Lululemon API'}), 500

        return jsonify(product_details), 200

    # Run the Flask app
    return awsgi.response(app, event, context)
