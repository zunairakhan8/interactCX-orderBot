from flask import Flask, request, jsonify
import requests as req

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    
    webhook_request = request.get_json()

    order_id = webhook_request['queryResult']['parameters']['order_id']

    
    response = req.post('https://1a94-39-51-43-125.ngrok-free.app ', json={'order_id': order_id})
    
    
    if response.status_code == 200:
        shipment_date = response.json().get('shipment_date', 'N/A')
    else:
        shipment_date = 'N/A'

    
    webhook_response = {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        f"Your order {order_id} will be shipped on {shipment_date}"
                    ]
                }
            }
        ]
    }

    return jsonify(webhook_response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

