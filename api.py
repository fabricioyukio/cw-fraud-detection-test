from datetime import datetime

import joblib
import pandas as pd
from flask import Flask, jsonify, request

from utils import to_integer

# loading model and label encoder
loaded_model = joblib.load('model.sav')
loaded_le = joblib.load('label_encoder.sav')


# Set the threshold for the model, if this is exceeded, the transaction is APPROVED
# If you are using the regression model, the possible values for this, fall between 0 and 99.9...(but not 100)
# If you are using the classifier model, the only possible value for this is 0
TRANSACTION_THRESHOLD = 60
MAX_USER_OPERATIONS_IN_A_ROW = 3
LATE_HOURS={
    'start': 22,
    'end': 6,
    'limit': 100
}

app = Flask(__name__)

# a log of user requests in the last 24 hours
user_requests_today = {}

def get_user_requests_today(user_id):
    global user_requests_today
    if user_id not in user_requests_today:
        user_requests_today[user_id] = []
    return user_requests_today[user_id].length

def increment_user_requests_today(user_id, card_number,timestamp):
    global user_requests_today
    user_requests_today[user_id].append({
        'card_number': card_number,
        'timestamp': timestamp
    })
    return user_requests_today[user_id].length

@app.route("/")
def hello_world():
    return "Nothing to do here!"

@app.route('/transaction', methods=['POST'])
def transaction_check():
    transaction = request.get_json()

    # if the transaction is made during late hours, above the limit, deny the transaction
    transaction_date = datetime.fromisoformat(transaction['transaction_date'])
    transaction_amount = transaction['transaction_amount']
    if transaction_date.hour >= LATE_HOURS['start'] or transaction_date.hour <= LATE_HOURS['end']:
        if transaction_amount > LATE_HOURS['limit']:
            return jsonify({
                'transaction_id' : transaction['transaction_id'],
                'recommendation' : 'deny',
                'message': 'Exceeds amount limit during late hours'
            }),406

    # if there are too many requests from the same user, deny the transaction
    if get_user_requests_today(transaction['user_id']) > MAX_USER_OPERATIONS_IN_A_ROW:
        return jsonify({
            'transaction_id' : transaction['transaction_id'],
            'recommendation' : 'deny',
            'message': 'Too many credit card requests'
        }),406

    transaction_data = pd.DataFrame([transaction])
    transaction_data['transaction_date']=transaction_data['transaction_date'].apply(lambda x: to_integer(x))
    transaction_data['card_number'] = loaded_le.fit_transform(transaction_data['card_number'].astype(str))
    prediction = loaded_model.predict(transaction_data)

    # regardless of the outcome, increment the number of requests for this user
    increment_user_requests_today(
        user_id=transaction['user_id'],
        card_number=transaction['card_number'],
        timestamp=datetime.now()
        )

    if prediction[0] > TRANSACTION_THRESHOLD:
        return jsonify({
            'transaction_id' : transaction['transaction_id'],
            'recommendation' : 'approve',
        }), 202

    return jsonify({
        'transaction_id' : transaction['transaction_id'],
        'recommendation' : 'deny',
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)