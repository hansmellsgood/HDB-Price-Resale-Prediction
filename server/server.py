from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    location = request.form['location']
    flat_type = float(request.form['flat_type'])
    storey_range = float(request.form['storey_range'])
    sqm = float(request.form['sqm'])
    remaining_lease = float(request.form['remaining_lease'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, flat_type, storey_range, sqm, remaining_lease)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Flask Server for Home Price Prediction")
    util.load_saved_artifacts()
    app.run()
