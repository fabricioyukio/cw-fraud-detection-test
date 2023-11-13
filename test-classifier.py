from datetime import datetime

import joblib
import pandas as pd

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

# Preprocess new data in the same way as your training data
# new_data['device_id'] = loaded_le.transform(new_data['device_id'].astype(int))
# new_data['merchant_id'] = loaded_le.fit_transform(new_data['merchant_id'].astype(int))
# new_data['user_id'] = loaded_le.fit_transform(new_data['user_id'].astype(int))
new_data['card_number'] = loaded_le.fit_transform(new_data['card_number'].astype(str))
# new_data['transaction_date'] = loaded_le.fit_transform(new_data['transaction_date'].astype(int))


# Use the loaded model to make a prediction
prediction = loaded_model.predict(new_data)

print(f'The predicted has_cbk score for the transaction is: {prediction[0]}')
