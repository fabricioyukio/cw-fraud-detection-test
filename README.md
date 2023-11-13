# Fraud detection PoC

A very implementation example for an API to validate credit card requests.


## What does it do?

It uses sample credit card transaction data to learn which are the most probable operations to incur in a Chargeback result for a credit payment request. (You can read and learn more about **Chargebacks** in the file ```solution.md```)

Then, whenever there is a request for credit card payment it uses the learned pattern to approve or deny a credit card payment request.

**Example payload**
```json
{
"transaction_id" : 2342357,
"merchant_id" : 29744,
"user_id" : 97051,
"card_number" : "434505******9116",
"transaction_date" : "2019-11-30T23:16:32.812632",
"transaction_amount" : 373,
"device_id" : 285475
}
```

**Example response**
```json
{
"transaction_id" : 2342357,
"recommendation" : "approve"
}
```

## Preparation

Install Python requirements
```bash
pip install -r requirements.txt
```
Then, you must decide one of the models for it to use.
### By Classifier
The simplest, giving 0(FALSE) for "denial" and 1(TRUE) for "approval"
```bash
python by-classifier.py
```

### By Regression
It gives a score associated with the trustability of the transaction.
Near 0 for the most suspicious.
Near 100 for the less likely to be fraud.
The greater, the better.
```bash
python by-regression.py
```

Each one processes the ```transactional-sample.csv``` file and saber the model:
- model.sav
- label_encoder.sav


## Running the API

Just run
```bash
python api.py
```
By default, it uses the port 8080.

Just make some POST requests to ```http://localhost:8080/transaction```, using the above request format.