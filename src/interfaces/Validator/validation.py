from common.logger import Logger
from interfaces.Validator.validation_factory import GatewayValidation
import re
from datetime import datetime
import os

class InputValidation(GatewayValidation):

    def __init__(self):
        pass

    def post_method_validation(self,request):
        is_ok, msg = check_CreditCardNumber(request)
        if not is_ok: return is_ok,msg
        is_ok, msg = check_CardHolder(request)
        if not is_ok: return is_ok,msg
        is_ok, msg = check_ExpirationDate(request)
        if not is_ok: return is_ok,msg
        is_ok, msg = check_SecurityCode(request)
        if not is_ok: return is_ok, msg
        is_ok, msg = check_Amount(request)
        if not is_ok: return is_ok,msg
        return True, "validation successful."

def validate_CreditCardNumber(credit_number):
    pattern = r'^[973][0-9]{15}|[973][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
    result = re.match(pattern,credit_number)
    if not result: 
        Logger.log_info(f"Invalid CreditCardNumber. Please pass correct CreditCard Number.")
        return (False,{
            'error': True,
            'msg': 'Invalid CreditCardNumber. Please pass correct CreditCard Number.',
            'error_request': 400
        })
    return (True, None)

def check_CreditCardNumber(request):
    Logger.log_info("Validating Credit Card Number.")
    if 'CreditCardNumber' not in request:
        Logger.log_info(f"No CreditCardNumber field found incoming POST request.")
        return (False,{
            'error': True,
            'msg': 'No CreditCardNumber field found incoming POST request.',
            'error_request': 400
        })
    return validate_CreditCardNumber(request['CreditCardNumber'])  

def validate_CardHolder(name):
    if not isinstance(name, str):
        Logger.log_info(f"Invalid CardHolder. Please pass correct CardHolder Number.")
        return (False,{
            'error': True,
            'msg': 'Invalid CardHolder. Please pass correct CardHolder Number.',
            'error_request': 400
        })
    return (True,None)

def check_CardHolder(request):
    Logger.log_info("Validating Card Holder name.")
    if 'CardHolder' not in request:
        Logger.log_info(f"No CardHolder field found incoming POST request.")
        return (False,{
            'error': True,
            'msg': 'No CardHolder field found incoming POST request.',
            'error_request': 400
        })
    return validate_CardHolder(request['CardHolder'])  

def validate_ExpirationDate(date):
    
    curr_date = datetime.today()
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
    except:
        Logger.log_info(f"Invalid ExpirationDate Format. Please pass ExpirationDate in format yyyy-mm-dd.")
        return (False,{
            'error': True,
            'msg': 'Invalid ExpirationDate Format. Please pass ExpirationDate in format yyyy-mm-dd.',
            'error_request': 400
        })
    if input_date < curr_date:
        Logger.log_info(f"Incorrect ExpirationDate. Please pass correct ExpirationDate. ")
        return (False,{
            'error': True,
            'msg': 'Incorrect ExpirationDate . Please pass correct ExpirationDate. ',
            'error_request': 400
        })
    return (True,None)

def check_ExpirationDate(request):
    Logger.log_info("Validating Expiration Date.")
    if 'ExpirationDate' not in request:
        Logger.log_info(f"No ExpirationDate field found incoming POST request.")
        return (False,{
            'error': True,
            'msg': 'No ExpirationDate field found incoming POST request.',
            'error_request': 400
        })
    return validate_ExpirationDate(request['ExpirationDate'])  

def check_SecurityCode(request):
    Logger.log_info("Validating Security Code.")
    if 'SecurityCode' in request:
        result = type(request['SecurityCode']) == str and len(request['SecurityCode']) == 3 and request['SecurityCode'].isdigit()
        if not result:
            Logger.log_info(f"SecurityCode is not in correct format")
            print(f"SecurityCode is not in correct format")
            return (True,None) 
        else:
            Logger.log_info(f"SecurityCode is in correct format")
            print(f"SecurityCode is  in correct format")
            return (True,None) 
    else:
            Logger.log_info(f"No SecurityCode field found incoming POST request.")
            print(f"No SecurityCode field found incoming POST request.")
            return (True,None) 

def validate_Amount(amt):
    # amt = str(amt)
    try:
        float(amt)
    except:
        Logger.log_info(f"Invalid Amount. Please pass correct Amount Number.")
        return (False,{
            'error': True,
            'msg': 'Invalid Amount. Please pass correct Amount Number.',
            'error_request': 400
        })
    res = type(amt) == float
    if not res:
        Logger.log_info(f"Invalid Amount. Please pass correct Amount Number.")
        return (False,{
            'error': True,
            'msg': 'Invalid Amount. Please pass correct Amount Number.',
            'error_request': 400
        })
    return (True,None)

def check_Amount(request):
    Logger.log_info("Validating Amount .")
    if 'Amount' not in request:
        Logger.log_info(f"No Amount field found incoming POST request.")
        return (False,{
            'error': True,
            'msg': 'No Amount field found incoming POST request.',
            'error_request': 400
        })
    return validate_Amount(request['Amount'])  

