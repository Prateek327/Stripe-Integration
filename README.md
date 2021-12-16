# Stripe-Integration
Stripe integration in Flask(Python)

## Prerequisite
1. In stripe create a sandbox account
2. In test dashboard, create a customer with card information and billing address. This customer information will be required to pass while creating charge.

## Setup
1. Install python 3.x : https://www.python.org/downloads/
2. Install pip : https://pip.pypa.io/en/stable/installation/
3. Git clone this repository. Using commandline, switch to this repository and create a virtual environment (https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments)
4. Install all the dependencies by using this command : pip install -r requirements.txt
5. Open the repository in code editor, in app.py enter the Stripe secret key
6. Start the server by using this command : python -m app. This will open the flask server

## API

### Create Charge
Curl command: 

```
curl --location --request POST 'http://localhost:5000/api/v1/create_charge' \
--header 'Content-Type: application/json' \
--data-raw '{
    "amount": <enter amount>,
    "currency": "<enter customer currency>",
    "description": "<enter description>",
    "customer": "<enter customer id>",
    "capture": <enter true / false>
}'
```

### Capture Charge
Curl command: 

```
curl --location --request POST 'http://localhost:5000/api/v1/capture_charge/<charge_id>'
```

### Get all charge
Curl command: 

```
curl --location --request GET 'http://localhost:5000/api/v1/get_charges'
```

### Refund Charge
Curl command:

```
curl --location --request POST 'http://localhost:5000/api/v1/create_refund/<charge_id>'
```
  

  

