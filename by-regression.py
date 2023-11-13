from datetime import datetime

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from utils import to_integer

print('reading data')
data = pd.read_csv('transactional-sample.csv')
print('loaded data')

# Preprocess your data
# Convert boolean to int
data['has_cbk'] = data['has_cbk'].astype(int)

# categorical variables, convert to numerical
# merchant_id,user_id,card_number,transaction_date,transaction_amount,device_id,has_cbk
print('adjusting classifier data')
le = LabelEncoder()
data['merchant_id'] = le.fit_transform(data['merchant_id'].astype(str))
data['user_id'] = le.fit_transform(data['user_id'].astype(str))
data['card_number'] = le.fit_transform(data['card_number'].astype(str))
data['device_id'] = le.fit_transform(data['device_id'].astype(str))
data['transaction_date']=data['transaction_date'].apply(lambda x: to_integer(x))

features = data.drop('has_cbk', axis=1)
target = data['has_cbk']

features = data.drop('has_cbk', axis=1)
target = data['has_cbk']

print('training')
# data into training and testing sets
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.35, random_state=35)

# Training your model
model = RandomForestRegressor()
model.fit(features_train, target_train)

print('saving model and label encoder')
# Save the model and label encoder
filename = 'model.sav'
joblib.dump(model, filename)
filename_le = 'label_encoder.sav'
joblib.dump(le, filename_le)