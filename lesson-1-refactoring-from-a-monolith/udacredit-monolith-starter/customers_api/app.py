from flask import Flask, jsonify, make_response

from .services.customers import get_customers

app = Flask(__name__)

@app.route('/api/customers', methods=['GET'])
def customers():
    """Return a JSON response for all customers."""
    sample_response = {
        "customers": get_customers()
    }
    # JSONify response
    response = make_response(jsonify(sample_response))

    # Add Access-Control-Allow-Origin header to allow cross-site request
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'

    return response

if __name__ == '__main__':
    app.run(host="localhost", port=5001, debug=True)
