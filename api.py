import joblib
from flask import Flask, jsonify, request

from utils import to_integer

# loading model and label encoder
loaded_model = joblib.load('model.sav')
loaded_le = joblib.load('label_encoder.sav')

# Your new transaction data
transaction_data = {
    "transaction_id" : 2342357,
    "merchant_id" : 29744,
    "user_id" : 97051,
    "card_number" : "434505******9116",
    "transaction_date" : "2019-11-30T23:16:32.812632",
    "transaction_amount" : 373,
    "device_id" : 285475
}

# Convert the transaction data to DataFrame
new_data = pd.DataFrame([transaction_data])
new_data['transaction_date']=new_data['transaction_date'].apply(lambda x: to_integer(x))


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/incomes', methods=['POST'])
def check():
    transaction = request.get_json()
    return jsonify({
        'transaction_id' : '',
        'recommendation' : '',
    }), 204