'''
Main program to expose the solution as an API
'''
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from common.logger import Logger
from interfaces.Validator.validation import InputValidation
from paymentgateway.paymentgateway import PaymentGateway

'''
Have all the setup up parts
'''

class APICreator():
    def __init__(self):

        self.BASE_DIR = "./.."
        self.validation = InputValidation()
        self.payment_gateway = PaymentGateway()
        Logger.init(self.BASE_DIR,"payment_logger")

    def process_payment(self, request):
        try:
            is_ok, response = self.validation.post_method_validation(request)
            if not is_ok:
                return jsonify(response)
            is_ok, response = self.payment_gateway.select_payment_provider(request)
        except Exception as e:
            Logger.log_error(f"payment cannot be processed. Reason {str(e)}")
            return jsonify({
                "msg": "Internal server error while processing Payment",
                "error": True,
                "error_request": 500
            })
        return jsonify({
            "error": False,
            "error_request": 200,
            "msg": "Payment Process Successful."
        })
