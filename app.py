from os import name
from flask import Flask
from flask import  request
from flask_restful import Api, Resource
import stripe

INVALID_INPUT_400 = ({"message": "Insufficient information has been passed. Read the docs for required parameters"}, 400)
stripe.api_key = "<stripe secret key>"

class CreateCharge(Resource):
    @staticmethod
    def post():
        currency = request.json.get("currency").strip()
        amount = request.json.get("amount")
        customer = request.json.get("customer")
        description = request.json.get("description").strip()
        capture = request.json.get("capture")
        if currency is None or amount is None or description is None :
                return INVALID_INPUT_400
        try:
            resp = stripe.Charge.create(customer=customer, amount=amount, currency=currency, description=description, capture=capture)
            return resp
        except Exception as e:
            return ({"message": str(e)}, 400)

class CaptureCharge(Resource):
    @staticmethod
    def post(chargeId):
        if chargeId is None :
                return INVALID_INPUT_400
        try:
            resp = stripe.Charge.capture(chargeId)
            return resp
        except Exception as e:
            return ({"message": str(e)}, 400)

class CreateRefund(Resource):
    @staticmethod
    def post(chargeId):
        if chargeId is None :
                return INVALID_INPUT_400
        try:
            resp = stripe.Refund.create(charge=chargeId)
            return resp
        except Exception as e:
            return ({"message": str(e)}, 400)

class GetCharges(Resource):
    @staticmethod
    def get():
        try:
            resp = stripe.Charge.list()
            return resp
        except Exception as e:
            return ({"message": str(e)}, 400)
        

def generate_routes(app):

    # Create api.
    api = Api(app)

    # Add all routes resources.
    # Create Charge.
    api.add_resource(CreateCharge, "/api/v1/create_charge")

    # Capture Charge.
    api.add_resource(CaptureCharge, "/api/v1/capture_charge/<chargeId>")

    # Create Refund.
    api.add_resource(CreateRefund, "/api/v1/create_refund/<chargeId>")

    # Get Charges.
    api.add_resource(GetCharges, "/api/v1/get_charges")

def create_app():
    # Create a flask app.
    app = Flask(__name__)

    # Set debug true for catching the errors.
    app.config['DEBUG'] = True
    
     # Generate routes.
    generate_routes(app)
    return app

if __name__ == '__main__':

    # Create app.
    app = create_app()

    # Run app. For production use another web server.
    # Set debug and use_reloader parameters as False.
    app.run(port=5000, debug=True, host='localhost', use_reloader=True)