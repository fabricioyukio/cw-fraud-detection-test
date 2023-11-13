# Solution to questions

1. Explain the money flow and the information flow in the acquirer market and the role of the main players.
**Cardholder**: Makes a request for a purchase from a merchant, enters and authorizes cardholder information to initiate the transaction.

**Payment Gateway**: Forwards transaction information from cardholder to payment processor.

**Processor**: Serves as a facilitator on behalf of the acquirer, forwards transaction information from the payment gateway to the card network.

**Card Network**(like VISA, MasterCard, Amex): Routes the transaction information to the correct issuing bank in order to receive the bank’s authorization.

**Issuer** (Issuing Bank): Receives and verifies the transaction information; if the credit or debit is available, the issuer sends an authorization code for the transaction back to the card network.

**Card Network**: Receives the authorization approval from the issuing bank, then forwards the authorization to the processor.

**Processor**: Receives the issuer’s authorization approval from the card network, then forwards that information to the payment gateway.

**Payment Gateway**: Receives the issuer’s authorization approval from the processor, forwards it to the merchant to complete the transaction.

**Merchant**: Receives the authorization, fulfills the order, and batches the transaction information along with the rest of the day’s sales.

**Acquirer**: Receives the batched transactions at the end of the day (some doesn't need to expect the end of the day, or to all the transactions for the day batched), then deposits an amount into the merchant’s account equal to the total of the batch, **minus applicable fees**.

### The money flow
When an operation is authorized, if it's a debit, then the proper amount of money (amount transactioned + taxes, and some may have taxes amount like ZERO) from the Cardholder. If it was a credit operation, the institution marks it for "provision"(roughly "a promise of payment") and operates towards the credit limit.

The same goes for the Merchant, as it is promised the amount of related money (minus taxes).

When the Cardholder pays for the credit operation, it is received the issuing bank, which splits that amount Acquirer, the bank and the merchant (wich most the time, there are proper days for that compensations)



2. Explain the difference between acquirer, sub-acquirer and payment gateway and how the flow explained in question 1 changes for these players.

The Acquirer is an institution that acts on behalf of a Card Network, and provides mechanisms and connectivity for receiving transaction requests.

A Sub-Acquirer might exist for acting on behalf of an Acquirer. Usually, an institution that gives special advantages or something like for the Merchant or the Cardholder. Most of the time, they will have specific connectivity and services, and some services that are only forwarding the request to the Acquirer. Mostly acting as the Processor.

The Payment Gateway offers connectivity/technology for the Merchant to consume the various services related to e-payments, thus facilitating the transactions of selling goods and services, safeguarding Cardholder sensitive information and ensuring ordered operations.



3. Explain what chargebacks are, how they differ from cancellations and what is their connection with fraud in the acquiring world.

A **Chargeback** is a charge that is returned, after a card payment is issued and was disputed by the Cardholder or the Cardholder's Issuing Bank.
Merchants, usually receive some fee or penalties from the Acquirer when that happens.
The disputes may occur for many reasons, most commonly:
- Cardholder being charged for items that weren't delivered
- Duplicate charges by mistake.
- Technical issues
- Fraudulent charges from credit or debit card information that has been compromised

A **Cancellation** is a method that simply cancels the main payment and the related order. Sometimes as it never happened. Say it is like a reversal/rollback for the transaction. And is usually available only before daily report for batching the day's transactions.

