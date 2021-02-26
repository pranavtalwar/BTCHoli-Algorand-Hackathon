from flask_restful import Resource, reqparse
from datetime import datetime
from app import db
import json 

parser = reqparse.RequestParser()
parser.add_argument('bondName', help = 'This field cannot be blank', required = True)
parser.add_argument('couponRate', help = 'This field cannot be blank', required = True)
parser.add_argument('issuerName', help = 'This field cannot be blank', required = True)
parser.add_argument('faceValue', help = 'This field cannot be blank', required = True)
parser.add_argument('issueDate', help = 'This field cannot be blank', required = True)
parser.add_argument('maturityDate', help = 'This field cannot be blank', required = True)
parser.add_argument('numberOfAnnualPayments', help = 'This field cannot be blank', required = True)
parser.add_argument('natureOfBond', help = 'This field cannot be blank', required = True)

class get_bond_data(Resource):
    def post(self):
        form = db.form
        data = parser.parse_args()
        bond_info = {
            'bond_name': data['bondName'],
            'coupon_rate': data['couponRate'],
            'issuer_name': data['issuerName'],
            'face_value': data['faceValue'],
            'issue_date': data['issueDate'],
            'maturity_date': data['maturityDate'],
            'number_of_annual_payments': data['numberOfAnnualPayments'],
            'nature_of_bond': data['natureOfBond']
        }
        bond_id = form.insert_one(bond_info)
        
        return {
            "message": "done",
            # "bond_id": bond_id.inserted_id
        }

